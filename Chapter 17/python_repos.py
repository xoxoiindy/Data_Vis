import requests

# Make an API call and store the response.
# store api in a string to the url variable
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#GitHub is currently on the third version of its API,
#so we define headers for the API call
headers = {'Accept': 'application/vnd.github.v3+json'}
# used the get requests to make the call to the API
#assign the response object to the variable r
r = requests.get(url, headers=headers)
# print out value of status code to see if response was sucessful
print(f"Status code: {r.status_code}")

# Store API response in a variable.
# use the json method to convert the info to a dictionary and store it in responce_dict variable
response_dict = r.json()
# print the value 'total_count' that represents the total number of repositories on GitHub
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
# value 'items' contains the list of dictionaries, store it in repo_dicts
repo_dicts = response_dict['items']
# print out the lendth of repo_dicts which shows the number if repositories
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
# print the number of keys in the dictionary
print(f"\nKeys: {len(repo_dict)}")
# for loop which sorts the keys alphabetically and prints all the dictionary keys
for key in sorted(repo_dict.keys()):
    print(key)


print("\nSelected information about each repository:")
# wrtie a for loop which loops through every dictionary in repo_dicts
for repo_dict in repo_dicts:
    # prints name of project
    print(f"Name: {repo_dict['name']}")
    # use the key 'owner' to access the dictionary and use the key 'login' to get the owners login name
    print(f"Owner: {repo_dict['owner']['login']}")
    # prints out how many stars the project has earned
    print(f"Stars: {repo_dict['stargazers_count']}")
    # prints out the url for the projects GitHub repository
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")



