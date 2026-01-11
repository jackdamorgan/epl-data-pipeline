from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv("API_TOKEN")
url = "https://api.football-data.org/v4/competitions/PL/matches?season=2024"

session = requests.Session()
session.headers.update({
    "X-Auth-Token": api_key
})

response = session.get(url, timeout=10)
data = response.json()

#checking that the response is valid
print(response)


with open("samples/epl_matches_2024.json", "w") as f:
    json.dump(data, f, indent=2)
