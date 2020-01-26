import requests
import json

# original thumb query
def getImages(query)
    per_page = '12'
    current_page='1'
    url = "https://api.shutterstock.com/v2/images/search?query="+query + '&per_page=' + per_page + '&page=' + current_page
    headers = {'Authorization': 'Basic ZTYzSGxneHlXTFpVM3BtcXBqcVpWU0FLWUZhTW1OODQ6bThGTEZiUTJFdEw4cVdobg=='}

    # response is in JSON format
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)['data']
      
# similar image query
def searchForSimilar(imageList, image):
    url = "https://api.shutterstock.com/v2/cv/similar/images?view=full&per_page="+per_page+"&page="current_page"&asset_id="+imageList[image]['id']
    
    headers = {'Authorization': 'Basic ZTYzSGxneHlXTFpVM3BtcXBqcVpWU0FLWUZhTW1OODQ6bThGTEZiUTJFdEw4cVdobg=='}
    
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)['data']

def getPreview(imageList, image):
    return imageList[image]['assets']['preview']['url']

def getPreview_1500(imageList, image):
    return imageList[image]['assets']['preview_1500']['url']

def downloadImage(imageList, image, directory):
    urllib.request.urlretrieve(url, directory+'/fullSize'+str(img)+'.jpg')
    return str(directory+'/fullSize'+str(img)+'.jpg')
    
