# 개발자모드(F12)에서 플레이페이지의 목록들 다 포함되도록 복사해서 playlist.html 로 같은 폴더에 저장 후 요 스크립트 실행


from bs4 import BeautifulSoup

source = open('playlist.html', 'r', encoding='UTF-8')
soup = BeautifulSoup(source, 'html.parser')
items = soup.select('a#video-title')

for i, video in enumerate(items, start=1):
    title = video.attrs['title'].strip()
    md_title = f'## {i}. {title}'
    md_title = md_title.replace('[ComputerGraphics] ', '')
    print(md_title)
