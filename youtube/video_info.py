# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

from typing import List
import pandas as pd

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from pandas import DataFrame

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_id_list(file_name: str) -> List[str]:
    df = pd.read_csv(file_name)
    return df['Id'].to_list()


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    input_df = pd.read_csv('temp.csv')  # DataFrame from the result of video_list.py
    id_list = input_df['Id'].to_list()

    video_id_list = []
    title_list = []
    cover_list = []
    publish_list = []
    link_list = []
    view_count_list = []
    like_count_list = []
    comment_count_list = []
    description_list = []
    tag_list = []

    while id_list:
        cur_list = id_list[:50]  # id 최대 50개 조회 가능 (50개 넘으면 400 에러)
        arg_str = ",".join(cur_list)
        print(len(cur_list), arg_str)
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=arg_str
        )
        response = request.execute()
        items = response["items"]
        for item in items:
            video_id = item['id']
            title = item['snippet']['title'].strip().replace('  ', ' ')
            cover = f'http://img.youtube.com/vi/{video_id}/sddefault.jpg'
            publish = item['snippet']['publishedAt'][:10]
            link = f'https://www.youtube.com/watch?v={video_id}'
            view_count = int(item['statistics']['viewCount'])
            like_count = int(item['statistics']['likeCount'])
            comment_count = int(item['statistics']['commentCount'])
            description = item['snippet']['description']
            tags = item['snippet'].get('tags', [])
            tag_str = ','.join(tags)

            video_id_list.append(video_id)
            title_list.append(title)
            cover_list.append(cover)
            publish_list.append(publish)
            link_list.append(link)
            view_count_list.append(view_count)
            like_count_list.append(like_count)
            comment_count_list.append(comment_count)
            description_list.append(description)
            tag_list.append(tag_str)

        id_list = id_list[len(cur_list):]

    df = DataFrame({
        "Id": video_id_list,
        "Title": title_list,
        "Cover": cover_list,
        "Publish": publish_list,
        "Link": link_list,
        "View": view_count_list,
        "Like": like_count_list,
        "Comment": comment_count_list,
        "Description": description_list,
        "Tags": tag_list
    })
    print(df)
    df.to_csv('output.csv', header=True, index=False)
    print('to_csv(). Done')


if __name__ == "__main__":
    main()
