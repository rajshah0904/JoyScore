#AIzaSyBfNc7E5khZF2eWOVX7Yox14rDpLxOWXjg
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the API client
api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyBfNc7E5khZF2eWOVX7Yox14rDpLxOWXjg" # replace this with your own API key
youtube = build(api_service_name, api_version, developerKey=api_key)

# Specify the video ID for which you want to get the like and dislike counts
#WE WILL NEED TO IMPLEMENT A METHOD WHICH GETS THE ID OF THE VIDEO WHILE A USER IS WATCHING THE VIDEO (REQUIRES CONSTANT SCRAPING)
video_id = "dQw4w9WgXcQ" # replace this with the ID of the video you want to get data for

# Call the API to get the video statistics
try:
    video_response = youtube.videos().list(
        part='statistics',
        id=video_id
    ).execute()
    video_stats = video_response['items'][0]['statistics']
    likes = video_stats.get('likeCount', 0)
    dislikes = video_stats.get('dislikeCount', 0)
    print(f'Likes: {likes}')
    print(f'Dislikes: {dislikes}')
except HttpError as error:
    print(f'An HTTP error {error.resp.status} occurred: {error.content}')

# videostat of 1 represents a positively rated video, videostat of -1 represents a negatively rated video, and a videostat of 0 reflects a neutrally rated video
if(likes - dislikes > 0)
    videoStat = 1
else if(likes - dislikes < 0)
    videoStat = -1
else if(likes - dislikes == 0)
    videoStat = 0
    
print(videoStat)
    