from unittest import TestCase

import bs4

import lecture_list


class Test(TestCase):
    def test_get_lecture(self):
        raw_text = '''
            <li>
              <span class="text">입이 트이는 영어 06-01</span>
              <p class="btn-data">
                <span class="btn-data-listening"
                  ><button
                    type="button"
                    onclick="downloadFile('EXTRADATAFILE', 'listen_flnm', '48980', '21644');"
                  >
                    AUDIO
                  </button></span
                >
              </p>
            </li>
        '''
        li = bs4.BeautifulSoup(raw_text, 'html.parser')
        lecture = lecture_list.get_lecture(li)
        print(lecture)
