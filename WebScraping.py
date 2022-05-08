import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://lego--pichar.repl.co/lego.html")

soup = BeautifulSoup(page.text, 'html.parser')

listName = []
listPrice = []
listPieces = []

names = soup.findAll(class_='name')
for name in names:
  cleanName = name.get_text()
  listName.append(cleanName)
  print(cleanName)

print("\n")

pieces = soup.findAll(class_='pieces')
for piece in pieces:
  cleanName = piece.get_text()
  listPieces.append(cleanName)
  print(cleanName)

print("\n")

price = soup.findAll(class_='price')
for cost in price:
  cleanName = cost.get_text()
  listPrice.append(cleanName)
  print(cleanName)

df = pd.DataFrame({'Product Name':listName, 'Pieces':listPieces, 'Price':listPrice})
df.to_csv('Products.csv', index=False, encoding='utf-8')

jumboTron = soup.findAll(class_='jumbotron')
for jumbo in jumboTron:
  cleanName = jumbo.get_text()
  listPrice.append(cleanName)
  print(cleanName)
