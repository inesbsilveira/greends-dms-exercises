from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 

"""
# open the html file
with open("final_assignment\strawberries_html.html", "r", encoding="utf-8") as f:
  doc = BeautifulSoup(f, "html.parser")

#print(doc.prettify())

tags = doc.find_all("strong")
print(tags)

"""
import requests

url = "https://www.healthline.com/nutrition/foods/strawberries#nutrition"

result = requests.get(url)
doc = BeautifulSoup (result.content, "html.parser")
#print(doc.prettify())

# it is necessary to go down through the HTML structure to isolate the block of text that
# is relevant, and then isolate the tags with the values of interest

# this selects the relevant part of the page
doc1 = doc.find("article", class_="article-body")

# this isolates the first block that contains the nutrients list
doc2 = doc1.find("div", class_="css-0")

# this identifies the unordered list
doc3 = doc2.find("ul")

print(doc3) 

# the <li> tag can be used to isolate the values. The <strong> tag is not usefull, can be removed