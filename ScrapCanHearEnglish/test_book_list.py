from unittest import TestCase

from bs4 import BeautifulSoup

import book_list


class Test(TestCase):
    def test_get_book_list(self):
        raw_text = '''
            <div class="book-data">
              <p class="title">
                <a href="/mall/product_ebs_view.donga?product_seq=30849"
                  >입이 트이는 영어 2021/ 6월호</a
                >
              </p>
              <p class="keyword">
                <span>#2021</span>
                <span>#06월</span>
              </p>
              <div class="btn-data-down">
                <p class="btn-down listen">
                  <button
                    type="button"
                    onclick="viewExtraDataList(30849, 'DTTPSDP', '입이 트이는 영어 2021/ 6월호', '듣기자료')"
                  >
                    <span class="title">듣기자료</span
                    ><span class="down-icon all">전체보기</span>
                  </button>
                </p>
              </div>
            </div>
        '''

        div = BeautifulSoup(raw_text, 'html.parser')
        book = book_list.get_book_info(div)
        print(book)
