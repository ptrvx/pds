import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
payload = json.dumps({
  "title": "Novi naslov",
  "body": "Novi tekst",
  "userId": 1
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data)