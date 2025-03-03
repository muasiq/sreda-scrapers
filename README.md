# SREDA Multi-Page List Scraper

This project is a web scraper designed to extract multi-page tabular data from **SREDA (Sustainable and Renewable Energy Development Authority)** and similar websites. The scraper fetches list data by iterating through paginated URLs and exports the extracted data into an Excel file. The code should work fine for any BD govt's archaic websites! Just know the total page count of the list.

## Features
- Automatically iterates through multiple pages.
- Exports table data to **Excel (.xlsx)**.
- Handles missing or irregular table cells gracefully.
- Easy URL modification to scrape other similar websites.

## How It Works
The core scraping logic is contained in `scraper.py`. The scraper performs the following tasks:
1. Sends HTTP GET requests to the target URL.
2. Parses the HTML content to find tabular data.
3. Extracts table headers and rows.
4. Handles inconsistent row lengths by padding missing cells.
5. Combines all pages into a single dataset.
6. Exports the final dataset to an **Excel file**.

## Prerequisites
- Python 3.x
- Install the following libraries:

```bash
pip install requests pandas beautifulsoup4 openpyxl
```

## How to Run
1. Clone the repository:

```bash
git clone https://github.com/muasiq/sreda-scrapers.git
cd sreda-scrapers
```

2. Modify the `base_url` in `scraper.py` to target the desired website.

3. Run the script:

```bash
python scraper.py
```

4. The exported data will be saved as `output.xlsx` in the same directory.

## Customizing for Other Websites
To scrape other websites:
- Change the `base_url` variable to match the new list URL.
- Ensure the HTML table structure is similar.
- Adjust parsing logic if necessary.

## Error Handling
- Pages without tables are skipped automatically.
- Connection timeouts are handled gracefully.
- Rows with incorrect column counts are skipped with a warning.

## Example Output
```
Fetching page 1...
Headers (5): ['ID', 'Name', 'Location', 'Capacity', 'Date']
Fetching page 2...
Total rows collected: 100
Data has been exported to output.xlsx
```

## Contributing
Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

