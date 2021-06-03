import json

import bs4
import requests


def get_book_list() -> list:
    url = "https://www.bookdonga.com/ebs/extradata_list_ajax.donga"
    data = {
        "pagenum": "1",
        "p_serviceyear": None,
        "fgorder": None,
        "p_extradatatype": None,
        "p_classtype": "MI"
    }
    res = requests.post(url, data=data)
    print(res.text)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    div_list = soup.findAll("div", {"class": "book-data"})
    books = []
    for div in div_list:
        book = get_book_info(div)
        books.append(book)
    return books


def get_book_info(div: bs4.element.Tag) -> dict:
    anchor = div.p.a
    title: str = anchor.string.strip()

    button = div.find("button")
    onclick_raw = button["onclick"]
    open_bracket = onclick_raw.find("(")
    onclick_raw = onclick_raw[open_bracket + 1:]
    close_bracket = onclick_raw.find(")")
    onclick_raw = onclick_raw[:close_bracket]
    raw_texts = onclick_raw.split(",")
    book_id = int(raw_texts[0].strip())

    # print(f"onclick_raw: {onclick_raw}")
    print(f"{title}    book_id: {book_id}")

    return {
        "title": title,
        "book_id": book_id,
    }


if __name__ == "__main__":
    get_book_list()
