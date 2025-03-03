import requests
import pandas as pd
from bs4 import BeautifulSoup

# Base URL
base_url = "https://ndre.sreda.gov.bd/index.php?id=28&i=3&pg="

def fetch_data(page_number):
    url = base_url + str(page_number)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_number}: {e}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    if not table:
        return None
    
    # Extract headers only from first page
    headers = [header.text.strip() for header in table.find_all('th')]
    
    # Extract rows and ensure consistent column count
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = [cell.text.strip() for cell in row.find_all('td')]
        # Pad row with empty strings if needed
        while len(cells) < len(headers):
            cells.append('')
        rows.append(cells)
    
    return headers, rows

# Initialize variables
all_data = []
headers = None

# Fetch data from all pages
for page_number in range(1, 88):
    print(f"Fetching page {page_number}...")
    result = fetch_data(page_number)
    if not result:
        continue
        
    page_headers, rows = result
    
    # Set headers from first page
    if headers is None:
        headers = page_headers
        print(f"Headers ({len(headers)}): {headers}")
    
    # Validate and add rows
    for row in rows:
        if len(row) == len(headers):
            all_data.append(row)
        else:
            print(f"Skipping row with incorrect length: {len(row)} columns")

# Create DataFrame and export
print(f"Total rows collected: {len(all_data)}")
df = pd.DataFrame(all_data, columns=headers)
df.to_excel('output.xlsx', index=False)
print("Data has been exported to output.xlsx")