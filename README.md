## How to Run the Script

After completing the TODOs, you can run the script with the following commands:

### Filter by Criticality
- **Critical only:** `python asset_lister.py --critical-only`
- **High only:** `python asset_lister.py --high-only`

### Filter by Owner or Tag
- **By Owner:** `python asset_lister.py --owner "Jordan Freeman"`
- **By Tag:** `python asset_lister.py --tag "web"`

### Custom Files
- **Specify Input:** `python asset_lister.py --infile my_assets.csv`
- **Specify Output:** `python asset_lister.py --outfile results.json`
# Asset Inventory Processor (Python Assignment)

## Goal
This assignment introduces you to **Python scripting for security automation**.  
You’ll complete and improve a script that reads an **asset inventory** from a CSV file, filters it based on various conditions, and writes the filtered results to a JSON file.

When you’re done, your script should:
1. Load data from a CSV file of assets.
2. Allow users to filter assets using command-line options.
3. Output a clean JSON file with only the selected records.

Then, you can tackle **bonus challenges** that make it even more powerful — like pulling data from an API and showing it as a table.

---

## Helpful VSCode Extensions

- Todo Tree by Gruntfuggly (this will allowing organizing and highlighting TODOs and FIXMEs across the repo)
- Python
- Python Debugger
- Pylint

---

## Files Included

codeyou-secops-python-challenge1/  
├── README.md   
├── asset_list.py             # The script you’ll fix and improve  
├── asset_inventory_list.csv  # Local CSV file to test with  
└── docs/  
        └── getting_data_from_the_api.md        # Instructions for the optional API bonus  
        └── displaying_data_in_table_format.md  # Instructions for the optional table bonus  

---

## Getting Started
1. Make sure you have **Python 3.10+** installed.
2. Open a terminal in this folder and run:
```bash
   python asset_lister.py --help
```

You should see usage information for the script.

3. Try running it with the included CSV file:

   ```bash
   python asset_lister.py --infile asset_inventory_list.csv
   ```

You’ll likely hit some issues — that’s intentional!
Your job is to fix the script by following the `# TODO:` comments inside it.

---

## Core Tasks

Follow each `# TODO:` marker inside `asset_lister.py` in order.

1. **Fix type hints**

   * Check the function `load_assets(path: Path) -> list[str]`
   * What should it actually return? (Hint: think about what `csv.DictReader` produces.)

2. **Fix the filtering logic**

   * The `filter_assets()` function has an undefined variable (`own`?)
   * Check each conditional and make sure it behaves as expected.
   * Make sure tag comparison matches the lowercase tokens created earlier.
   * Add support for a `--high-only` argument.

3. **Add argument parsing for `--high-only`**

   * This should work similarly to the existing `--critical-only` argument.
   * Make sure you pass this new value into `filter_assets()`.

4. **Fix file paths and output writing**

   * Ensure the script correctly references `asset_inventory_list.csv`.
   * Confirm the JSON output file is written successfully.

---

## When You’re Done

You should be able to run:

```bash
python asset_lister.py --critical-only --infile asset_inventory_list.csv
```

and see something like:

```
Wrote 12 assets to critical_assets.json
```

---

## Bonus Objectives

### 1. Filtering Enhancements

* Add a `--tag` filter (already partially written).
* Add a new `--hostname` argument to filter by asset hostname.

### 2. Fetch Data from the API (HARD)

Instead of using a downloaded CSV, pull the asset inventory live from the API endpoint:

```
https://my.api.mockaroo.com/cobalt/asset_inventory_list.csv
```

* You’ll be given a **Proton Drive link** in your class assignment containing your `api_key.txt`. The password to the download link will be included as well
* Follow the instructions in `docs/getting_data_from_the_api.md` to use the API key and `requests.get()` to load data.

### 3. Display as a Table (HARD)

Add an optional argument:

```
--format table
```

When used, the script should print the data in a simple table format instead of JSON.
If no format is specified, it should default to JSON.

You can either:

* Build your own simple table printer using `print()` and spacing (see bonus `docs/displaying_data_in_table_format.md`), **or**
* Use a library like `tabulate` for easier formatting.

---

## Tips

* Use `launc.json` and debugging with breakpoints to follow execution
* Use `print()` statements while debugging to inspect variables or use the Debug Console as part of VSCode.
* Commit your progress often.
* Ask yourself what data type each variable holds (`list`, `dict`, `str`, etc.).
* Don’t be afraid to open and read the CSV in a spreadsheet to understand its structure.

---

## Example Run

```bash
python asset_lister.py --owner "Jordan Freeman" --critical-only
```

Output:

```
Wrote 5 assets to critical_assets.json
```

---

## Hint for Overachievers

If you complete everything, try combining multiple filters:

```bash
python asset_lister.py --owner "Jordan Freeman" --tag web --high-only --format table
```

You’re now filtering assets **owned by Jordan**, tagged **web**, that are **high** or **critical**, and printing them in a **table**.

---

Good luck — and remember:  
**Every `# TODO:` comment is a breadcrumb to the next discovery!**
