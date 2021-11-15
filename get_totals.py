import requests
import bs4 as bs

# Define URL variables
# TODO add date
user = "troybrewer1167"
url = f"https://www.myfitnesspal.com/food/diary/{user}"

# Get page info and use BS to parse
page = requests.get(url)
soup = bs.BeautifulSoup(page.text, 'html.parser')

# Totals Table
table = soup.find("tr", {"class": "total"})
data = table.find_all("td")

# Get cals from data
cals = data[1].find(text=True)

# Get macros sub-Table
macros = table.find_all("span", {"class": "macro-value"})
carbs = macros[0].find(text=True)
fat = macros[1].find(text=True)
protein = macros[2].find(text=True)

# Output data
print(f"Cal: {cals}")
print(f"Carbs: {carbs}")
print(f"Fat: {fat}")
print(f"Protein: {protein}")

# Same as above but with goals table
goal_table = soup.find("tr", {"class": "total alt"})
goal_data = goal_table.find_all("td")

goal_cals = goal_data[1].find(text=True)

goal_macros = goal_table.find_all("span", {"class": "macro-value"})
goal_carbs = goal_macros[0].find(text=True)
goal_fat = goal_macros[1].find(text=True)
goal_protein = goal_macros[2].find(text=True)

print(f"Goal Cals: {goal_cals}")
print(f"Goal Carbs: {goal_carbs}")
print(f"Goal Fat: {goal_fat}")
print(f"Goal Protein: {goal_protein}")
