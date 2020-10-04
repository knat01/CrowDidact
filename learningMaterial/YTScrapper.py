#NOTE: use command pip install --upgrade google-api-python-client to use API

from googleapiclient.discovery import build 
#google import

API_KEY = 'AIzaSyCmcZAUUECqzVu3QzP1oO3YiSfZvMddqmM' 
#API Key

youtube = build('youtube' , 'v3' , developerKey=API_KEY)
#Build object using Key


Topic = input('Enter the topic to search for: ')
Range = int(input('Enter the number of links to search for: '))
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

while (Range != 0):
#Walmart brand do while loop

    Topic = input('Enter the topic to search for: ')
    Range = int(input('Enter the number of links to search for: '))

    if(Range == 0 or Topic == '0'):
        exit()
        #exit condition
    
    request2 = youtube.search().list( q=Topic , part='snippet' , type='video', videoEmbeddable='true' , maxResults=Range )

    response2 = request2.execute()
    
    for item in response2['items']:
        print('')
        print('Video name: '+ item['snippet']['title'])
        print('Embed url: '+ 'https://www.youtube.com/embed/'+item['id']['videoId'])
        print('')

    