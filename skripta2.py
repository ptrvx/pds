import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
payload = json.dumps({
  "title": "Najnoviji naslov",
  "body": "Najnoviji tekst",
  "userId": 3
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data)

conn.request("POST", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data)
