Awesome bonus idea. Here’s a student-friendly, step-by-step add-on they can follow with zero prior experience.

# Bonus Objective: Add an option to display output as a **table** instead of **JSON**

### NOTE:
The code referenced below is generic and not specific to this repo. You will need to understand what this code is doing and adapt it to work with your own code, e.g. The `get_args()` function contains code that you already have defined in your `main()` so you will either have to take the code from `get_args()` and place it in your `main()` or refactor by moving the arg parsing code from your `main()` into a new `get_args()` function. Use your own discretion on how you would like to accomplish this.

## What you’ll build

Add a command-line argument so your script can output either:

* **JSON** (the current behavior), or
* a **plain-text table** printed to the terminal.

You’ll do this by:

1. Adding an argument (`--format`) to the script
2. Keeping JSON as the default
3. Implementing a small function to print a table from your CSV data

---

## Step 1 — Add a `--format` command-line option

You’ll use Python’s built-in `argparse` (no extra installs needed).

```python
import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="Read a CSV, process it, and print JSON or a table."
    )
    parser.add_argument(
        "--format",
        choices=["json", "table"],
        default="json",
        help="Output format. Defaults to 'json'. Use 'table' to print a text table."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input CSV file."
    )
    return parser.parse_args()
```

> If your script already has argument parsing, just add the `--format` argument to your existing parser.

---

## Step 2 — Keep your current CSV → list[dict] logic

Assume you already read the CSV into a list of dictionaries, e.g.:

```python
import csv

def load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)  # e.g., [{"name":"Alice","age":"30"}, ...]
```

---

## Step 3 — Add a simple table printer (standard library only)

This function:

* Figures out the columns from the CSV header
* Computes column widths
* Prints a header, a separator line, and each row

```python
def print_table(rows):
    if not rows:
        print("(no rows)")
        return

    # Determine columns (use CSV header keys)
    columns = list(rows[0].keys())

    # Compute width of each column (max of header and cell values)
    widths = []
    for col in columns:
        max_cell = max(len(str(r.get(col, ""))) for r in rows)
        widths.append(max(len(col), max_cell))

    # Helpers to format a row and a separator
    def fmt_row(values):
        return " | ".join(str(v).ljust(w) for v, w in zip(values, widths))

    def sep():
        return "-+-".join("-" * w for w in widths)

    # Print header
    print(fmt_row(columns))
    print(sep())

    # Print rows
    for r in rows:
        print(fmt_row([r.get(c, "") for c in columns]))
```

---

## Step 4 — Wire it up

Choose the output behavior based on `--format`.

```python
import json

def main():
    args = get_args()
    rows = load_csv(args.input)

    if args.format == "json":
        # Keep existing behavior
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:  # "table"
        print_table(rows)

if __name__ == "__main__":
    main()
```

---

## How to run it (examples)

```bash
# JSON output (default)
python script.py --input data.csv

# Explicit JSON
python script.py --input data.csv --format json

# Table output
python script.py --input data.csv --format table
```

---

## Acceptance criteria (what “done” looks like)

* ✅ Running with `--format json` prints well-formatted JSON (same as before).
* ✅ Running with `--format table` prints a readable table: header row, separator, and one line per record.
* ✅ Works on CSVs with different headers and lengths.
* ✅ No third-party packages are required.

---

## Helpful hints & common pitfalls

* **Empty files / no rows:** Your table function should handle an empty CSV gracefully (e.g., print “(no rows)”).
* **Long text values:** If columns are very wide, the table will be wide. That’s okay for now.
* **Numbers vs strings:** Everything from CSVs is read as text. Don’t worry about numeric types for this task.
* **Encoding errors on Windows:** If you get weird characters, make sure you opened the file with `encoding="utf-8"`.

---

## (Optional) Nice extras if you finish early

* Add `--columns name,age` to select which columns to show.
* Right-align numbers and left-align text.
* Add `--max-width 40` to truncate very long cells with “…”.

