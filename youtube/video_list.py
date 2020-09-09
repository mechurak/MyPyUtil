from bs4 import BeautifulSoup
from pandas import DataFrame

# URL = 'https://www.youtube.com/channel/UCSWPuzlD337Y6VBkyFPwT8g/videos'
# Chrome 으로 위 사이트 들어가서, 맨 밑까지 스크롤
# 개발자도구(F12) 로 body 부분 복사해서 body.txt 로 저장

source = open('body.txt', 'r', encoding='UTF-8')
soup = BeautifulSoup(source, 'html.parser')
items = soup.select('a#video-title')

title_list = []
cover_list = []
link_list = []
id_list = []
view_count_list = []

for video in items:
    title = video.attrs['title'].replace('  ', ' ')
    dot_i = title.find('.')
    try:
        int(title[:dot_i])
    except ValueError:
        print(f'Ignore {title}')
        continue

    raw_text = video.attrs['aria-label']
    raw_text = raw_text.replace('  ', ' ')
    temp_i = raw_text.find('조회수')
    view_count_str = raw_text[temp_i + 3:-1].replace(',', '')
    view_count = int(view_count_str)

    href = video.attrs['href']  # '/watch?v=Y5HjRn0kvYs'
    video_id = href[9:]
    video_id = video_id[:11]
    cover = f'http://img.youtube.com/vi/{video_id}/sddefault.jpg'
    link = f'https://www.youtube.com/watch?v={video_id}'

    title_list.append(title)
    cover_list.append(cover)
    link_list.append(link)
    id_list.append(video_id)
    view_count_list.append(view_count)

df = DataFrame({
    "Name": title_list,
    "Cover": cover_list,
    "Link": link_list,
    "Id": id_list,
    "View": view_count_list
})
print(df)

df.to_csv('temp.csv', header=True, index=False)
print('to_csv(). Done')
