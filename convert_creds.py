import json

with open("credentials.json", "r") as f:
    creds = json.load(f)

creds_str = json.dumps(creds)
print(creds_str)
