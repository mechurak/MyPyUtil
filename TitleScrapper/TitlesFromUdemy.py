# 강의 섹션 다 펼친 후, 개발자모드(F12)에서 강의 목록들 다 포함되도록 복사해서 udemy.html 로 같은 폴더에 저장 후 요 스크립트 실행


from bs4 import BeautifulSoup

source = open('udemy.html', 'r', encoding='UTF-8')
soup = BeautifulSoup(source, 'html.parser')
sections = soup.select('.section--section--BukKG')

# css-o78dt4 챕터
# css-1o6lxsj 소제목

for section in sections:
    section_title = section.select_one('h3 > button > span > span').get_text().strip()
    print(f'## === {section_title} ===')
    chapters = section.select('.curriculum-item-link--curriculum-item-title-content--1SLoR')
    for chapter in chapters:
        title = chapter.select_one('span > span').get_text().strip()  # ex) 'CHAPTER 1'
        print(f'## {title}')

