from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

title = soup.find('h1').string
price = soup.find('p', 'price_color').string
availability = soup.find('p', 'instock availability').text.strip()
image = soup.find(alt='A Light in the Attic')

print(title)
print(price)
print(availability)
print(image['src'])
