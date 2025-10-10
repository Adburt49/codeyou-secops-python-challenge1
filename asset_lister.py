#!/usr/bin/env python3
import csv, json, argparse
from pathlib import Path

# TODO: Is the path typehint correct??
def load_assets(path: Path) -> list[str]: # TODO: Is the type hint on the return actually correct?
    rows = []
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            r = {k: (v.strip() if isinstance(v, str) else v) for k, v in r.items()}
            # normalize tags to a list of lowercase tokens
            r["tags"] = [t.strip().lower() for t in (r.get("tags","")).split(",") if t.strip()]
            r["criticality"] = r.get("criticality","").strip().lower()
            rows.append(r)
    return rows


# TODO: Perfectionist - Add type hints for the parameters
def filter_assets(rows, owner=None, tag=None, critical_only=False): # TODO: Make sure we can successfully pass high_only boolean
    def match(r):
        if critical_only and r.get("criticality") != "critical":
            return False
        if own and r.get("owner","").lower() != owner.lower(): # TODO: Something doesn't look right...hmm?
            return False
        if tag and tag.upper() not in r.get("tags", []): # TODO: Are we using the correct string manipulation for tag? What does this do? 
            return False
        
        # TODO: Add condition for high_only
        
        return True
    
    return [r for r in rows if match(r)]


def main():
    ap = argparse.ArgumentParser(description="Filter assets from CSV and export to JSON.")
    ap.add_argument("--owner", help="Filter by owner (exact match)")
    ap.add_argument("--tag", help="Filter by tag (lowercase after normalization)")
    ap.add_argument("--critical-only", action="store_true", help="Only include critical assets")

    # TODO: Add another argument for the user to input `--high-only`. This should pass the string `store_true` to action parameter similar to the critical-only argument 
    
    ap.add_argument("--infile", default="asset_inventory_list.csv", help="Input CSV") # TODO: Fix this to reference the actual asset_inventory_list.csv
    ap.add_argument("--outfile", default="critical_assets.json", help="Output JSON")
    args = ap.parse_args()

    rows = load_assets(Path(args.infile))
    out = filter_assets(rows, owner=args.owner, tag=args.tag, critical_only=args.critical_only) # TODO: You should already have `--high-only` done, how do we pass it to the `filter_assets()`??
    
    Path(args.outfile).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Wrote {len(out)} assets to {args.outfile}")

if __name__ == "__main__":
    main()
