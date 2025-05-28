import requests
from bs4 import BeautifulSoup
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="alirezza",
    password="",
    database="learningdb"
)

with conn.cursor() as cursor:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            capital VARCHAR(100),
            population BIGINT,
            area FLOAT
        )
    ''')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
url = "https://scrapethissite.com/pages/simple/"
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to fetch data from the website.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
country_divs = soup.find_all("div", class_="col-md-4 country")

with conn.cursor() as cursor:
    for i, country in enumerate(country_divs[:20]):
        name = country.find("h3", class_="country-name").text.strip()
        capital = country.find("span", class_="country-capital").text.strip()
        population = country.find("span", class_="country-population").text.strip().replace(",", "")
        area = country.find("span", class_="country-area").text.strip().replace(",", "")

        population = int(population) if population else 0
        area = float(area) if area else 0.0

        cursor.execute('''
            INSERT INTO countries (name, capital, population, area)
            VALUES (%s, %s, %s, %s)
        ''', (name, capital, population, area))

        print("%d. %s - Capital: %s Population: %s Area: %s km" % (i+1, name, capital, population, area))

conn.commit()
conn.close()
