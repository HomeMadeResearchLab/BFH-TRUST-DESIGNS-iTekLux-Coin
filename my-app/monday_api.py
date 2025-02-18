import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("MONDAY_API_KEY")

# Monday API URL
MONDAY_API_URL = "https://api.monday.com/v2"

# GraphQL Query to fetch workspaces
query = """{
    workspaces {
        id
        name
    }
}"""

# Make the request
headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(
    MONDAY_API_URL,
    json={"query": query},
    headers=headers
)

# Print the response
if response.status_code == 200:
    print("✅ Success! Workspaces retrieved:")
    print(response.json())
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)
