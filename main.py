import requests
from bs4 import BeautifulSoup
import re
import json

# basic setup
URL = "https://devnetproject.netlify.app/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

scripts = soup.find_all("script")

#print(scripts)
realtors = None

# find the full dict of realtors
for s in scripts:
    if s.string and "const realtors" in s.string:
        realtors = s.string
        break

# do insane regex magic to actually find the data we're looking for
realtorArray = re.search(r'const realtors = (\[.*?\]);', realtors, re.DOTALL)

data = realtorArray.group(1)

json_data = re.sub(r'(\w+):', r'"\1":', data)
json_data = json_data.replace("'", '"')

# convert the json to a dict so it's easier to work with
realtorDict = json.loads(json_data)

for key in realtorDict:
    print(key)
