import requests
from bs4 import BeautifulSoup
import re
import json

# Step 1: Get the page content
URL = "https://devnetproject.netlify.app/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

scripts = soup.find_all("script")

#print(scripts)
realtors = None

for s in scripts:
    if s.string and "const realtors" in s.string:
        realtors = s.string
        break

realtorArray = re.search(r'const realtors = (\[.*?\]);', realtors, re.DOTALL)

data = realtorArray.group(1)

json_data = re.sub(r'(\w+):', r'"\1":', data)
json_data = json_data.replace("'", '"')

realtorDict = json.loads(json_data)

for key in realtorDict:
    
