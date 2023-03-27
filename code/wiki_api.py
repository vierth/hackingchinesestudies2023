import requests


# https://en.wikipedia.org/w/api.php?action=help&modules=query
api_url ='https://en.wikipedia.org/w/api.php'

headers = {"Content-Type":"application/json"}

# search = {
#     "action":"opensearch",
#     "format":"json",
#     "search":"pandas"
# }

search = {
    "action": "query", 
    "format": "json",
    "titles": "Pandas",
    "prop": "contributors"
}


response = requests.post(api_url, params=search, headers=headers)
data = response.json()
print(data)