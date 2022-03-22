import requests
import json

url_posts = "http://jsonplaceholder.typicode.com/posts"
url_users = "http://jsonplaceholder.typicode.com/users"

payload={}
headers = {}

response = requests.request("GET", url_posts, headers=headers, data=payload)

data = json.loads(response.text)

body = data[2].get("body")
title = data[2].get("title")

payload = json.dumps({
  "title": title,
  "body": body,
  "userId": 1
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url_posts, headers=headers, data=payload)

print(response.text)

