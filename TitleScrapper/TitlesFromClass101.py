# 개발자모드(F12)에서 강의 목록들 다 포함되도록 복사해서 class101.html 로 같은 폴더에 저장 후 요 스크립트 실행


from bs4 import BeautifulSoup

source = open('class101.html', 'r', encoding='UTF-8')
soup = BeautifulSoup(source, 'html.parser')
chapters = soup.select('.css-o78dt4')

# css-o78dt4 챕터
# css-1o6lxsj 소제목

for chapter in chapters:
    chapter_number = chapter.select_one('.css-16x1nq5').get_text().strip()  # ex) 'CHAPTER 1'
    chapter_title = chapter.select_one('.css-2mmje1').get_text().strip()  # ex) 'DataScience/인공지능이란?'
    print(f'## {chapter_number}. {chapter_title}')

    subtitles = chapter.select('.css-1o6lxsj')
    for subtitle in subtitles:
        sub = subtitle.get_text().strip()
        print(f'🔶 {sub}')
