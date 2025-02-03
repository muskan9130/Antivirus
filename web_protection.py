import requests

API_KEY = "YOUR_GOOGLE_SAFE_BROWSING_API_KEY"

def check_url(url):
    payload = {
        "client": {"clientId": "antivirus", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["WINDOWS"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}", json=payload)
    return "🚨 Malicious URL!" if "matches" in response.json() else "✅ Safe URL."

