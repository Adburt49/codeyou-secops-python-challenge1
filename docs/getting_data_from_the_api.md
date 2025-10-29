#  Bonus Objective 2 — Pull the CSV data from an API instead of a local file

### NOTE:
The code referenced below is generic and not specific to this repo. You will need to understand what this code is doing and adapt it to work with your own code, e.g. The `get_args()` function contains code that you already have defined in your `main()` so you will either have to take the code from `get_args()` and place it in your `main()` or refactor by moving the arg parsing code from your `main()` into a new `get_args()` function. Use your own discretion on how you would like to accomplish this.

## **Goal**

Refactor your script so that instead of reading a local `.csv` file from disk, it retrieves the CSV **directly from a web API** using the provided URL and API key.

You’ll be fetching the asset inventory from this endpoint:

```
https://my.api.mockaroo.com/cobalt/asset_inventory_list.csv
```

Your script will make an HTTP request to the API, download the CSV data, and process it just like before.

---

## **What you’ll learn**

* How to use Python’s `requests` library to talk to APIs
* How to handle an API key safely
* How to parse CSV data directly from a web response
* How to make your code flexible to work with both files and URLs

---

## **Before you start**

You’ll be provided a **Proton Drive link** that contains your **API key file**.

1. Download that file (e.g., `api_key.txt`)
2. Place it in the same folder as your Python script
3. Open the file in a text editor — it should contain a single line like:

   ```
   123abc456def
   ```
4. You’ll read this key inside your script in order to authenticate with the API.

---

## **Step 1 — Install `requests`**

If you don’t already have it, install the `requests` package:

```bash
pip install requests
```

---

## **Step 2 — Create a function to load from the API**

You’ll use `requests.get()` to download the CSV.

```python
import requests
import csv
from io import StringIO

def load_csv_from_api(api_url, api_key_path):
    # Read your API key from the text file
    with open(api_key_path, "r", encoding="utf-8") as f:
        api_key = f.read().strip()

    # Add your API key to the request headers
    headers = {"X-API-Key": api_key}

    # Make the GET request
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Raises an error if something goes wrong

    # Convert response text into a CSV reader
    csv_data = StringIO(response.text)
    reader = csv.DictReader(csv_data)
    return list(reader)
```

---

## **Step 3 — Update your main code**

You can now decide whether to load data from a **local file** or the **API**.
Let’s add another argument called `--source` to your script.

```python
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Process asset inventory data.")
    parser.add_argument("--format", choices=["json", "table"], default="json",
                        help="Choose how to display data: json or table.")
    parser.add_argument("--input", help="Path to the local CSV file (optional).")
    parser.add_argument("--source", choices=["file", "api"], default="file",
                        help="Set to 'api' to load data from the API instead of a file.")
    parser.add_argument("--apikey", default="api_key.txt",
                        help="Path to your API key text file.")
    return parser.parse_args()
```

Now use it inside your `main()`:

```python
def main():
    args = get_args()

    if args.source == "api":
        rows = load_csv_from_api(
            "https://my.api.mockaroo.com/cobalt/asset_inventory_list.csv",
            args.apikey
        )
    else:
        rows = load_csv(args.input)

    if args.format == "json":
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        print_table(rows)
```

---

## **Step 4 — Test it**

### Example 1: Load from local file

```bash
python script.py --input asset_inventory.csv --source file --format json
```

### Example 2: Load from API

```bash
python script.py --source api --format table
```

You should see the same kind of output as before — but now your script is pulling live CSV data from the mock API instead of your computer.

---

## ✅ **Checklist for Success**

* [ ] The script runs without errors using `--source api`.
* [ ] You can see data that looks like an asset inventory (device names, IPs, etc.).
* [ ] Changing between `--format json` and `--format table` works with API data too.
* [ ] Your API key is **not** hardcoded — it’s read from a file.

---

## 💡 **Optional Stretch Ideas**

If you finish early:

* Print an error message if the API returns an HTTP error (e.g., 401 Unauthorized).
* Try using `try`/`except` blocks to handle network errors gracefully.

