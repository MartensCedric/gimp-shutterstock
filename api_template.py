import requests



# the search box needs to fill this value
# remove the input() function when implementing, it's there just for console testing purposes
query = input('query: ')

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic ZTYzSGxneHlXTFpVM3BtcXBqcVpWU0FLWUZhTW1OODQ6bThGTEZiUTJFdEw4cVdobg=='
}

url = "https://api.shutterstock.com/v2/images/search?query="
# response is in JSON format
response = requests.request("GET", url+query, headers=headers)
print(response.text)
