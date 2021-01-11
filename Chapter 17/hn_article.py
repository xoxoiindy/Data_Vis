import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
# from the response r we call the json method and store it in response_dict
response_dict = r.json()
# string stores directory of json file we are creating
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    # call dump method, dump response_dict into the f file,
    json.dump(response_dict, f, indent=4)

