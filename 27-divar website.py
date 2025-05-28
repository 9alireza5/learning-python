import requests
from bs4 import BeautifulSoup

url = 'https://divar.ir/s/tehran'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    ads = soup.find_all('div')

    for ad in ads:
        if 'نردبان' in ad.text:
            print('---')
            print(ad.text.strip())
            print('---')
else:
    print("Error")
