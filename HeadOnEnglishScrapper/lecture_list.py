import bs4
import requests
from bs4 import BeautifulSoup


def get_lecture_list(page: int) -> list:
    url = f"https://home.ebse.co.kr/10mins_lee2/replay/3/ajax/list?c.page={page}&searchCondition=&atply=no&searchConditionValue=0&stepId=ET2017H0SPE0101&orderBy=NEW&searchEndDt=&searchStartDt=&searchKeyword=&userId=&searchEndDtValue=0&brdcDsCdFilter=RUN&vodSort=NEW&searchKeywordValue=0&orderBy2=DESC%20&courseId=ER2017H0SPE01ZZ&pagingQuery=LIMIT%200,20&searchStartDtValue=0&_=1620871072843&"

    result = requests.get(url)

    soup = BeautifulSoup(result.text, 'html.parser')
    class_lst = soup.find("ul", {"class": "lst_pro03"})

    tag_li_list = class_lst.find_all('li')
    lectures = []
    for li in tag_li_list:
        lecture = get_lecture(li)
        lectures.append(lecture)
    return lectures


def get_lecture(li: bs4.element.Tag) -> dict:
    anchor = li.div.strong.a
    title: str = anchor.string.strip()
    title = title.replace("  ", " ")

    onclick_raw = anchor["onclick"]
    first_quote = onclick_raw.find("'")
    onclick_raw = onclick_raw[first_quote + 1:]
    first_quote = onclick_raw.find("'")
    lecture_id = onclick_raw[:first_quote]

    span_date = li.div.find("span", {"class": "date_info"})
    span_date_temp_strings = list(span_date.stripped_strings)
    date = span_date_temp_strings[-1]

    return {
        "title": title,
        "lecture_id": lecture_id,
        "date": date
    }
