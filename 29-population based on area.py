import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
from sklearn.linear_model import LinearRegression

url = "https://scrapethissite.com/pages/simple/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
countries = soup.find_all("div", class_="country")

data = []
for country in countries:
    name = country.find("h3", class_="country-name").text.strip()
    population = country.find("span", class_="country-population").text.strip().replace(",", "")
    area = country.find("span", class_="country-area").text.strip().replace(",", "")
    if population != "" and area != "":
        population = int(population)
        area = float(area)
        data.append((name, population, area))

conn = mysql.connector.connect(
    host="localhost",
    user="alirezza",
    password="",
    database="learningdb"
)
cursor = conn.cursor()
for row in data:
    cursor.execute("INSERT INTO countries (name, population, area) VALUES (%s, %s, %s)", row)
conn.commit()
cursor.close()
conn.close()

conn = mysql.connector.connect(
    host="localhost",
    user="alirezza",
    password="",
    database="learningdb"
)
df = pd.read_sql("SELECT population, area FROM countries", conn)
conn.close()

X = df[["population"]]
y = df["area"]

model = LinearRegression()
model.fit(X, y)

print("Model trained successfully.")
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
