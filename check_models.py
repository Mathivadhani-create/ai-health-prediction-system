import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("HF_TOKEN")

if token:
    print("Token loaded successfully")
    print("Starts with:", token[:5])
    print("Length:", len(token))
else:
    print("HF_TOKEN not found")