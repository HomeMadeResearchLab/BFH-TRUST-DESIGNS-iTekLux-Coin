import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key
api_key = os.getenv("MONDAY_API_KEY")

if api_key:
    print(f"Monday API Key: {api_key[:5]}... (loaded successfully)")
else:
    print("API key not found. Check your .env file!")
