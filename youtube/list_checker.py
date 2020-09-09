import json
from pandas import DataFrame

title_list = []
thumbnail_list = []
publish_list = []
link_list = []
category_list = []

file_list = [
    '초보_1.json'
]

for file in file_list:
    with open(file, encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        items = json_data["items"]
        _idx = file.find('_')
        category = file[:-5] if _idx == -1 else file[:_idx]

        for item in items:
            video_id = item['contentDetails']['videoId']
            title = item['snippet']['title'].strip()
            if title.startswith('Private'):
                continue
            # thumbnail = item['snippet']['thumbnails']['standard']['url']
            thumbnail = f'http://img.youtube.com/vi/{video_id}/sddefault.jpg'
            publish = item['contentDetails']['videoPublishedAt'][:10]
            link = f'https://www.youtube.com/watch?v={video_id}'

            title_list.append(title)
            thumbnail_list.append(thumbnail)
            publish_list.append(publish)
            link_list.append(link)
            category_list.append(category)

df = DataFrame({
    "Name": title_list,
    "Cover": thumbnail_list,
    "Publish": publish_list,
    "Link": link_list,
    "Category": category_list
})

print(df)

df.to_csv('temp.csv', header=True, index=False)
