
import os
import json
import urllib.request
import urllib.error

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise SystemExit("ERROR: GEMINI_API_KEY secret missing")

url = (
    "https://generativelanguage.googleapis.com/"
    "v1beta/models/gemini-2.5-flash:generateContent"
)

payload = {
    "contents": [{
        "parts": [{
            "text": "Reply in simple Hinglish: API test successful."
        }]
    }]
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "x-goog-api-key": api_key
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))
        print(result["candidates"][0]["content"]["parts"][0]["text"])
except urllib.error.HTTPError as e:
    print("API request failed. HTTP status:", e.code)
    raise SystemExit(1)
