import requests
from bs4 import BeautifulSoup

word = input("Enter a word: ")

url = 'https://www.dictionary.com/browse/' + word.lower()

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

definition_div = soup.find('div', {'value': '1'})

definition = definition_div.find('span', {'class': 'one-click-content'}).text.strip()

print("The definition of", word, "is:", definition)
