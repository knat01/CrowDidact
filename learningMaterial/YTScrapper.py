#NOTE: use command pip install --upgrade google-api-python-client to use API

from googleapiclient.discovery import build 
#google import

API_KEY = 'AIzaSyCmcZAUUECqzVu3QzP1oO3YiSfZvMddqmM' 
#API Key

youtube = build('youtube' , 'v3' , developerKey=API_KEY)
#Build object using Key

def YTScrape (Topic, AMT):


    Topic = Topic
    Range = int(AMT)
    #choose range and element


    request = youtube.search().list( q=Topic , part='snippet' , type='video', videoEmbeddable='true' , maxResults=Range )
    #API request


    response = request.execute()
    #return response from API server


    for item in response['items']:
        print('')
        print('Video name: '+ item['snippet']['title'])
        print('Embed url: '+ 'https://www.youtube.com/embed/'+item['id']['videoId'])
        print('')
    #output

