import requests 
import json
from bs4 import BeautifulSoup
URL = "https://devnetproject.netlify.app/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("body")
body = table.find("script").text.replace(" ","").replace("name", '"name"').replace("phone", '"phone"').replace("specialization",'"speciaization"').replace("experience",'"experience"')[15:-331]
phone = json.loads(body)
name = input().replace(" ","")
for table in phone:
    if table["name"]==name:
        print(f"name: {table["name"]}, phone: {table["phone"]}")