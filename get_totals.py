import requests
import bs4 as bs

url = 'https://www.myfitnesspal.com/food/diary/troybrewer1167'
page = requests.get(url)
soup = bs.BeautifulSoup(page.text, 'html.parser')

table = soup.find("tr", {"class": "total"})
data = table.find_all("td")

print(f"Cal: {data[1].find(text=True)}")

macros = table.find_all("span", {"class": "macro-value"})
carbs = macros[0].find(text=True)
fat = macros[1].find(text=True)
protein = macros[2].find(text=True)
print(f"Carbs: {carbs}")
print(f"Fat: {fat}")
print(f"Protein: {protein}")

# Goals
goal_table = soup.find("tr", {"class": "total alt"})
goal_data = goal_table.find_all("td")

print(f"Goal Cals: {goal_data[1].find(text=True)}")

goal_macros = goal_table.find_all("span", {"class": "macro-value"})
goal_carbs = goal_macros[0].find(text=True)
goal_fat = goal_macros[1].find(text=True)
goal_protein = goal_macros[2].find(text=True)
print(f"Goal Carbs: {goal_carbs}")
print(f"Goal Fat: {goal_fat}")
print(f"Goal Protein: {goal_protein}")
