import googleapiclient.discovery
import pandas as pd
from datetime import datetime
from googleapiclient.discovery import build
import s3fs 


# Define YouTube API key

api_key = ""

def run_youtube_etl(api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    channel_id = ''
    max_results = 50

    response = youtube.search().list(
        part='snippet',  
        channelId=channel_id,
        type='video',
        maxResults=max_results
    ).execute()

    video_list = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        video_description = item['snippet']['description']
        video_published_at = item['snippet']['publishedAt']

        # Use the 'videos().list' method to retrieve video statistics
        video_response = youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

        statistics = video_response['items'][0]['statistics']
        view_count = statistics.get('viewCount', 0)
        like_count = statistics.get('likeCount', 0)
        dislike_count = statistics.get('dislikeCount', 0)
        comment_count = statistics.get('commentCount', 0)

        video_info = {
            'Video ID': video_id,
            'Title': video_title,
            'Description': video_description,
            'Published At': video_published_at,
            'View Count': view_count,
            'Like Count': like_count,
            'Dislike Count': dislike_count,
            'Comment Count': comment_count
        }

        video_list.append(video_info)

    df = pd.DataFrame(video_list)
    return df

# Call the function to retrieve the DataFrame
retrieved_df = run_youtube_etl(api_key)

# Now you can access the DataFrame and print its contents
print(retrieved_df.head)
