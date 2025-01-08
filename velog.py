import requests


url = "https://v3.velog.io/graphql"
headers = {
    "Content-Type": "application/json"
}
payload = {
"user": "nibble"        
}

response = requests.post(url, params=payload, headers=headers)

if response.status_code == 200:
    data = response.text
    print(data)
else:
    print(f"Request failed with status: {response.status_code}")