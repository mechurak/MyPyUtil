# 개발자모드(F12)에서 강의 목록들 다 연 상태에서 다 포함되도록 복사. fastcampus.html 로 같은 폴더에 저장 후 요 스크립트 실행


from bs4 import BeautifulSoup

source = open('fastcampus.html', 'r', encoding='UTF-8')
soup = BeautifulSoup(source, 'html.parser')
chapters = soup.select('.classroom-sidebar-clip__chapter')

for chapter in chapters:
    chapter_title = chapter.select_one('.classroom-sidebar-clip__chapter__title__text').get_text().strip()  # ex) '01. 모든 산업 분야에 적용되는 Object Detection, Segmentation 마스터'
    print(f'\n\n=== {chapter_title}')

    chapter_parts = chapter.select('.classroom-sidebar-clip__chapter__part')
    for part in chapter_parts:
        part_title = part.select_one('.classroom-sidebar-clip__chapter__part__title').get_text().strip()  # ex) Faster R-CNN
        print(f'## === {part_title}')

        clips = part.select('.classroom-sidebar-clip__chapter__clip__title')
        for clip in clips:
            clip_title = clip.get_text().strip()
            print(f'## {clip_title}')
