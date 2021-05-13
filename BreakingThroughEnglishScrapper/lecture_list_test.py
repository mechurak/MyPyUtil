import unittest

from bs4 import BeautifulSoup

import lecture_list


class MyTestCase(unittest.TestCase):
    def test_get_lecture(self):
        raw_text = '''
        <li>
            <div class="txtcon_area replay_table">
                <span class="num_info tbl_td">735</span>
                <strong class="tit_info tbl_td">
                    <a href="#mp4_player" onclick="fnViewPlayer('60037451', '0', 'A', 'VOD', '');" id="lectNm_60037451">발음 강세 Unit 554.  운동</a>
                    </strong>	
                <!-- 																	
                <div class="hits_info tbl_td">									
                    106</div>
                 -->									
                <span class="date_info tbl_td"><i>방영일 : </i>2021.05.13<input type="hidden" class="fBrdcDt" value="2021.05.13.06.30">&nbsp;</span>
                <span class="date_info1 tbl_td"><i>학습일 : </i>&nbsp;</span>																		
                
                <div class="view_info">
                </div>									
                                                                                                
                <div class="view_info2">
                <a href="#this" class="download" onclick="downloadMultiFile('60037451','MP3', '');  return false;">MP3 내려받기</a>
                            </div>										
                                        
            </div>
        </li>
        '''

        tag_li = BeautifulSoup(raw_text, 'html.parser')
        lecture = lecture_list.get_lecture(tag_li)
        print(lecture)
        self.assertEqual("발음 강세 Unit 554. 운동", lecture["title"])
        self.assertEqual("60037451", lecture["lecture_id"])
        self.assertEqual("2021.05.13", lecture["date"])


if __name__ == '__main__':
    unittest.main()
