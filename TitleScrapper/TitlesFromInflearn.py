# 개발자모드(F12)에서 강의 목록들 다 포함되도록 복사해서 inflearn.html 로 같은 폴더에 저장 후 요 스크립트 실행


from bs4 import BeautifulSoup

source = open('inflearn.html', 'r', encoding='UTF-8')
soup = BeautifulSoup(source, 'html.parser')
sections = soup.select('.css-1nvk6w3')  # 섹션 + 동영상들 포함

# mantine-ovwq0i 섹션 이름
# css-1d376r6 동영상 하나

for section in sections:
    section_title = section.select_one('.mantine-ovwq0i').get_text().strip()  # ex) '교육 환경 준비'
    print(f'## 📚 {section_title}')

    clips = section.select('.css-1d376r6 > p')
    for clip in clips:
        title = clip.get_text().replace("\n", "").strip()
        print(f'## {title}')
