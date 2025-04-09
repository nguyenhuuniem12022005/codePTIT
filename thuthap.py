import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from rename import rename_duplicates
import csv
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



header = ['Player', 'Standard_Nation', 'Standard_Pos', 'Standard_Squad',
'Standard_Age','Standard_MP', 'Standard_Starts','Standard_Min',
'Standard_Gls', 'Standard_Ast','Standard_CrdY', 'Standard_CrdR',
'Standard_xG','Standard_xAG','Standard_PrgC', 'Standard_PrgP',
'Standard_PrgR','Standard_Gls_1', 'Standard_Ast_1','Standard_xG_1', 'Standard_xAG_1',
'Goalkeeping_GA90','Goalkeeping_Save%','Goalkeeping_CS%','Goalkeeping_Save%_1',
'Shooting_SoT%','Shooting_SoT/90','Shooting_G/Sh','Shooting_Dist',
'Passing_Cmp','Passing_Cmp%','Passing_TotDist','Passing_Cmp%_1','Passing_Cmp%_2',
'Passing_Cmp%_3','Passing_KP', 'Passing_1/3', 'Passing_PPA',
'Passing_CrsPA', 'Passing_PrgP','GCA_SCA', 'GCA_SCA90','GCA_GCA', 'GCA_GCA90',
'Defense_Tkl','Defense_TklW','Defense_Att','Defense_Lost',
'Defense_Blocks', 'Defense_Sh', 'Defense_Pass', 'Defense_Int',
'Possession_Touches', 'Possession_Def Pen', 'Possession_Def 3rd',
'Possession_Mid 3rd', 'Possession_Att 3rd', 'Possession_Att Pen',
'Possession_Att','Possession_Succ%','Possession_Tkld%',
'Possession_Carries', 'Possession_TotDist', 'Possession_PrgDist',
'Possession_PrgC', 'Possession_1/3', 'Possession_CPA', 'Possession_Mis',
'Possession_Dis','Possession_Rec', 'Possession_PrgR',
'Misc_Fls', 'Misc_Fld', 'Misc_Off', 'Misc_Crs','Misc_Recov',
'Misc_Won','Misc_Lost', 'Misc_Won%']

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
    "Player", "Team", "Nation", "Position", "Age", "Matches_played", "Starts", "Minutes",
    "Goals", "Assists", "Yellow_cards", "Red_cards", "XG", "XAG", "Gls/90", "Ast/90",
    "XG/90", "XGA/90", "SoT%", "SoT/90", "G/sh", "Dist", "Cmp", "Cmp%", "TotDist",
    "Short_Cmp%", "Medium_Cmp%", "Long_Cmp%", "KP", "1/3", "PPA", "CrsPA", "PrgP",
    "Touches", "Def Pen", "Def 3rd", "Mid 3rd", "Att 3rd", "Att Pen", "Att", "Succ%",
    "Tkld%", "Carries", "ProDist", "ProgC", "CPA", "Mis", "Dis", "Rec", "PrgR", "Tkl",
    "TklW", "Lost", "Blocks", "Sh", "Pass", "Int", "SCA", "SCA90", "GCA", "GCA90",
    "Fls", "Fld", "Off", "Crs", "Recov", "Won", "Won%", "GA90", "Save%", "CS%", "PSave%"
]
# Read and modify the CSV file
stats_standard.columns = newheader[:len(stats_standard.columns)]  # Rename columns
stats_standard.to_csv("result.csv", index=False)
print("Header updated and data saved successfully!")




# Close the WebDriver
driver.quit()