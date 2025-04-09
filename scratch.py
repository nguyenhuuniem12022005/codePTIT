import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

import csv




# Ensure unique column names
def rename_duplicates(columns):
    seen = {}
    new_columns = []

    for col in columns:
        if col in seen:
            seen[col] += 1
            new_columns.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            new_columns.append(col)

    return new_columns
# Set up Chrome options for headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without GUI
options.add_argument("--disable-gpu")  # Required for some systems
options.add_argument("--no-sandbox")  # Helps avoid permission errors in Linux
options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues

# Create the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Links to scrape
links = {
    "https://fbref.com/en/comps/9/stats/Premier-League-Stats#all_stats_standard": "stats_standard",
    "https://fbref.com/en/comps/9/keepers/Premier-League-Stats#all_stats_keeper": "stats_keeper",
    "https://fbref.com/en/comps/9/shooting/Premier-League-Stats#all_stats_shooting": "stats_shooting",
    "https://fbref.com/en/comps/9/passing/Premier-League-Stats#all_stats_passing": "stats_passing",
    "https://fbref.com/en/comps/9/gca/Premier-League-Stats#all_stats_gca": "stats_gca",
    "https://fbref.com/en/comps/9/defense/Premier-League-Stats#all_stats_defense": "stats_defense",
    "https://fbref.com/en/comps/9/possession/Premier-League-Stats#all_stats_possession": "stats_possession",
    "https://fbref.com/en/comps/9/misc/Premier-League-Stats#all_stats_misc": "stats_misc"
}

# Scrape tables
tables = {}
for link, id in links.items():
    driver.get(link)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    table = soup.find("table", id=id)
    if table is None:
        print(f"Table with id '{id}' not found.")
        continue

    table_data = []
    rows = table.find_all("tr")
    for row_idx, row in enumerate(rows):
        cells = row.find_all(["th", "td"])
        row_data = [cell.get_text(strip=True) for cell in cells]
        if row_idx == 0 or row_data[1] == "Rk":
            continue
        else:
            if row_data:
                table_data.append(row_data[1:])

    tables[id] = table_data
    print(f"Fetched table {id}")



stats_standard = pd.DataFrame(columns=tables["stats_standard"][0])

min_index = tables["stats_standard"][0].index("Min")

tables["stats_standard"].sort(key = lambda row: (row[0].split()[0]))

for row in tables["stats_standard"]:
    min_played = row[min_index].replace(",", "")
    if min_played.isdigit() and int(min_played) > 90:
        stats_standard.loc[len(stats_standard)] = row


# Read dataframes directly from the scraped tables
Player_df = stats_standard
goalkeep_df = pd.DataFrame(tables["stats_keeper"][1:], columns=tables["stats_keeper"][0])
shooting_df = pd.DataFrame(tables["stats_shooting"][1:], columns=tables["stats_shooting"][0])
passing_df = pd.DataFrame(tables["stats_passing"][1:], columns=tables["stats_passing"][0])
GCA_df = pd.DataFrame(tables["stats_gca"][1:], columns=tables["stats_gca"][0])
defense_df = pd.DataFrame(tables["stats_defense"][1:], columns=tables["stats_defense"][0])
possession_df = pd.DataFrame(tables["stats_possession"][1:], columns=tables["stats_possession"][0])
misc_df = pd.DataFrame(tables["stats_misc"][1:], columns=tables["stats_misc"][0])


DFs = [Player_df, goalkeep_df, shooting_df, passing_df, GCA_df, defense_df, possession_df, misc_df]
Player_df.columns = [f"Standard_{col}" if col != "Player" else col for col in Player_df.columns]
goalkeep_df.columns = [f"Goalkeeping_{col}" if col != "Player" else col for col in goalkeep_df.columns]
shooting_df.columns = [f"Shooting_{col}" if col != "Player" else col for col in shooting_df.columns]
passing_df.columns = [f"Passing_{col}" if col != "Player" else col for col in passing_df.columns]
GCA_df.columns = [f"GCA_{col}" if col != "Player" else col for col in GCA_df.columns]
defense_df.columns = [f"Defense_{col}" if col != "Player" else col for col in defense_df.columns]
possession_df.columns = [f"Possession_{col}" if col != "Player" else col for col in possession_df.columns]
misc_df.columns = [f"Misc_{col}" if col != "Player" else col for col in misc_df.columns]



for df in DFs:
    df.columns = rename_duplicates(df.columns)



header = ['Player', 'Standard_Nation', 'Possession_CPA', 'Possession_Mis']

# Initialize the resulting DataFrame
df = pd.DataFrame(columns=header)

# Iterate through each player in Player_df
for row_idx, row in Player_df.iterrows():
    player = row["Player"]
    player_data = {col:"N/a" for col in header}
    for file in DFs:
        if "Player" in file.columns and player in file["Player"].values:
            matching_row = file.loc[file["Player"] == player]
            for col in header:
                if col in file.columns:
                    value = matching_row[col].values
                    if len(value) > 0 and pd.notna(value[0]) and str(value[0]).strip() != "":
                        player_data[col] = value[0]
                    else:
                        player_data[col] = "N/a"


    df = pd.concat([df, pd.DataFrame([player_data])], ignore_index=True)
# Save the resulting DataFrame to a CSV file
df.to_csv("result.csv", index=False)
#rename header
newheader = [
    "Player", "Nation",  "CPA", "Mis"
]
# Read and modify the CSV file
stats_standard.columns = newheader[:len(stats_standard.columns)]  # Rename columns
stats_standard.to_csv("result.csv", index=False)
print("Header updated and data saved successfully!")




# Close the WebDriver
driver.quit()