# original thumb query
def getImages(query)
    per_page = '12'
    current_page='1'
    url = "https://api.shutterstock.com/v2/images/search?query="
    #api handling
    headers = {
       'Content-Type': 'application/x-www-form-urlencoded',
       'Authorization': 'Basic ZTYzSGxneHlXTFpVM3BtcXBqcVpWU0FLWUZhTW1OODQ6bThGTEZiUTJFdEw4cVdobg=='
    }

    # response is in JSON format
    response = requests.request("GET", url+query + '&per_page=' + per_page + '&page=' + current_page, headers=headers)
    return json.loads(response.text)['data']
        
        
#retrieve all thumbnails
#download previews
#full size

#find similar
directory = '/home/'+ getpass.getuser() + '/Desktop/tempPics'

def getPreview(imageList, image):
    return imageList[image]['assets']['preview']['url']

def getPreview_1500(imageList, image):
    return imageList[image]['assets']['preview_1500']['url']

def downloadImage(imageList, image, directory):
    urllib.request.urlretrieve(url, directory+'/fullSize'+str(img)+'.jpg')
    
def searchForSimilar(image)