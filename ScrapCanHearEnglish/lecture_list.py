import bs4
import requests


def get_lecture_list(book_id: int) -> list:
    url = "https://www.bookdonga.com/common/extradata_file_list_ajax.donga"
    data = {
        "product_seq": book_id,
        "extradatatype": 'DTTPSDP',
        "viewtype": "LAYER"
    }
    res = requests.post(url, data=data)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    tag_li_list = soup.findAll("li")

    lectures = []
    for li in tag_li_list:
        lecture = get_lecture(li)
        lectures.append(lecture)
    return lectures


def get_lecture(li: bs4.element.Tag) -> dict:
    title = li.span.text
    # print(f"title: {title}")
    temp_idx = title.rfind(" ")
    date = title[temp_idx + 1:]
    temp_idx = date.find("-")
    if temp_idx == 1:
        date = f"2021-0{date}"
    else:
        date = f"2021-{date}"
    # print(f"date: {date}")

    button = li.find("button")
    onclick_raw = button["onclick"]
    open_bracket = onclick_raw.find("(")
    onclick_raw = onclick_raw[open_bracket + 1:]
    close_bracket = onclick_raw.find(")")
    onclick_raw = onclick_raw[:close_bracket]
    raw_texts = onclick_raw.split(",")
    data_seq = raw_texts[2].strip()[1:-1]  # 자료 구분별 식별자
    part_seq = raw_texts[3].strip()[1:-1]  # 자료의 상위 식별자
    # print(f"data_seq: {data_seq}, part_seq: {part_seq}")
    remote_url = f"https://www.bookdonga.com/utility/download.donga?type=EXTRADATAFILE&fieldname=listen_flnm&data_seq={data_seq}&part_seq={part_seq}"
    # print(f"remote_url: {remote_url}")

    print(f"{date},{remote_url},{title}")
    return {
        "title": title,
        "date": date,
        "data_seq": data_seq,
        "part_seq": part_seq,
        "remote_url": remote_url
    }


if __name__ == "__main__":
    '''
    입이 트이는 영어 2021/ 6월호    book_id: 30849
    귀가 트이는 영어 2021/ 6월호    book_id: 30848
    입이 트이는 영어 2021/ 5월호    book_id: 30791
    귀가 트이는 영어 2021/ 5월호    book_id: 30790
    입이 트이는 영어 2021/ 4월호    book_id: 30751
    귀가 트이는 영어 2021/ 4월호    book_id: 30750
    입이 트이는 영어 2021/ 3월호    book_id: 30716
    귀가 트이는 영어 2021/ 3월호    book_id: 30715
    입이 트이는 영어 2021/ 2월호    book_id: 30566
    귀가 트이는 영어 2021/ 2월호    book_id: 30565
    '''
    get_lecture_list(30849)
