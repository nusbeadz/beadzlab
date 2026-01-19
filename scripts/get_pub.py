import argparse
import json
import requests

ORCID = "0000-0003-2783-303X"   # ← 改成目标 ORCID
OUTPUT_YAML = "_data/publist.yml"

HEADERS = {
    "Accept": "application/json"
}

BASE_URL = f"https://pub.orcid.org/v3.0/{ORCID}"

def yaml_quote(value):
    if value is None:
        return '""'
    return json.dumps(str(value), ensure_ascii=True)

def get_all_works():
    url = f"{BASE_URL}/works"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()["group"]

def get_work_detail(put_code):
    url = f"{BASE_URL}/work/{put_code}"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()

def extract_doi(external_ids):
    for eid in (external_ids or {}).get("external-id", []) or []:
        if (eid or {}).get("external-id-type", "").lower() == "doi":
            return (eid or {}).get("external-id-value")
    return None

def extract_url(external_ids):
    for eid in (external_ids or {}).get("external-id", []) or []:
        url = (eid or {}).get("external-id-url", {}) or {}
        url = url.get("value") if isinstance(url, dict) else None
        if url:
            return url
    return None

def main():
    parser = argparse.ArgumentParser(description="Fetch ORCID works and output publist.yml.")
    parser.add_argument("--orcid", default=ORCID, help="ORCID iD to fetch")
    parser.add_argument("--output", default=OUTPUT_YAML, help="Output YAML path")
    parser.add_argument("--default-image", default="dummy.png", help="Default image name")
    parser.add_argument("--default-highlight", type=int, default=0, help="Default highlight value")
    args = parser.parse_args()

    global BASE_URL
    BASE_URL = f"https://pub.orcid.org/v3.0/{args.orcid}"

    works = get_all_works()
    print(f"Found {len(works)} works")

    entries = []
    seen_doi = set()

    for group in works:
        summary = group["work-summary"][0]
        put_code = summary["put-code"]

        detail = get_work_detail(put_code)

        title = (
            detail.get("title", {})
            .get("title", {})
            .get("value")
        )

        journal = (detail.get("journal-title") or {}).get("value")

        pub_date = detail.get("publication-date") or {}
        year = (pub_date.get("year") or {}).get("value")

        authors = []
        for c in (detail.get("contributors") or {}).get("contributor", []) or []:
            name = (c or {}).get("credit-name", {}) or {}
            name = name.get("value") if isinstance(name, dict) else None
            if name:
                authors.append(name)

        author_str = " and ".join(authors)

        external_ids = detail.get("external-ids", {})
        doi = extract_doi(external_ids)
        if doi:
            if doi in seen_doi:
                continue
            seen_doi.add(doi)

        url = None
        if doi:
            url = f"https://doi.org/{doi}"
        else:
            url = extract_url(external_ids)
        if not url:
            url = (detail.get("url") or {}).get("value")

        display_parts = []
        if journal:
            display_parts.append(journal)
        if year:
            display_parts.append(f"({year})" if journal else str(year))
        display = " ".join(display_parts) if display_parts else "link"

        entry = {
            "title": title or "",
            "image": args.default_image,
            "description": "",
            "authors": author_str,
            "link": {
                "url": url or "",
                "display": display,
            },
            "highlight": args.default_highlight,
            "year": year or "",
        }

        entries.append(entry)

    def sort_key(item):
        try:
            year = int(item.get("year", ""))
        except ValueError:
            year = -1
        return (-year, item.get("title", ""))

    entries.sort(key=sort_key)

    lines = []
    for entry in entries:
        lines.append(f"- title: {yaml_quote(entry['title'])}")
        lines.append(f"  image: {yaml_quote(entry['image'])}")
        lines.append(f"  description: {yaml_quote(entry['description'])}")
        lines.append(f"  authors: {yaml_quote(entry['authors'])}")
        lines.append("  link:")
        lines.append(f"    url: {yaml_quote(entry['link']['url'])}")
        lines.append(f"    display: {yaml_quote(entry['link']['display'])}")
        lines.append(f"  highlight: {entry['highlight']}")
        lines.append("")

    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")

    print(f"YAML saved to: {args.output}")
    print(f"Total YAML entries: {len(entries)}")

if __name__ == "__main__":
    main()
