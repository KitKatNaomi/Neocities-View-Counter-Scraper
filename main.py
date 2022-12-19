import requests
import json
from bs4 import BeautifulSoup

# Download the webpage
url = "https://viewcounters.neocities.org/"
html = requests.get(url).text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the table element in the HTML
table = soup.find("table")

# Initialize an empty list to store the data
data = []

# Loop through each row in the table
for row in table.find_all("tr"):
  # Initialize a dictionary to store the data for this row
  row_data = {}
  
  # Loop through each cell in the row
  cells = row.find_all("td")
  if len(cells) == 6:
    # Extract the data for each cell
    row_data["site-name"] = cells[0].text.strip()
    row_data["site-url"] = cells[1].a["href"]
    row_data["site-profile"] = cells[2].a["href"]
    row_data["view-counter-url"] = cells[3].img["src"]
    row_data["text-color"] = cells[4].text.strip()
    row_data["background-color"] = cells[5].text.strip()
    data.append(row_data)
  # Cry if the row doesn't have 6 cells
# Convert the data to JSON and print it
print(json.dumps(data, indent=2))

# Convert the data to JSON and save it
with open("data.json", "w") as f:
  f.write(json.dumps(data, indent=2))
