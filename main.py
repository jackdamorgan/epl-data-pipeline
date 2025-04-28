import requests
import pandas as pd
import psycopg2
import json
import os
from dotenv import load_dotenv

# Applying the API Token so I can pull new data
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
headers = { 'X-Auth-Token': API_TOKEN }
url = 'https://api.football-data.org/v4/competitions/PL/matches?season=2023'

response = requests.get(url, headers=headers)
data = response.json()

print(data.keys())

# Getting the JSON locally to organize the data better
with open("raw_matches.json", "w") as f:
    json.dump(data, f, indent=4)

##