from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, element

# user-agent 정보를 변환해 주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
# pip install fake_useragent
from fake_useragent import UserAgent

# 요청 해더 정보를 꺼내올 수 있는 모듈
import urllib.request as req
import codecs

# User Agent 정보 변환 (필수는 아닙니다.)
opener = req.build_opener() # 헤더 정보를 초기화
opener.addheaders = [('User-agent', UserAgent().edge)]
req.install_opener(opener) # 새로운 헤더 정보를 삽입

# 크롬 드라이버에게 전달할 옵션 설정
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# 브라우저 안뜨게 하기
# options.add_argument('--headless')

# 크롬 드라이버를 버전에 맞게 자동으로 지원해주는 객체
# service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버 구동
browser = webdriver.Chrome(options)

# 브라우저 사이즈 조정
browser.set_window_size(800, 600)

# 페이지 이동
browser.get('https://www.melon.com/chart/index.htm')

# 웹 페이지 전체가 로딩될 때 까지 대기 후 남은 시간 무시
browser.implicitly_wait(10)

rank = 1 # 순위

# bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

'''
- with문을 사용하면 with 블록을 벗어나는 순간
  객체가 자동으로 해제됩니다. (자바의 try with resource와 비숫)

- with 작성 시 사용할 객체의 이름을 as 뒤에 작성해 줍니다.
'''
with codecs.open(r'c:\test\멜론순위.txt', 'w', encoding='utf-8') as f:
    f.write('순위\t곡명\t가수명\t앨범명\n')

    div_d_song_list_tbody = soup.select_one('div.d_song_list tbody')
    tr_list = div_d_song_list_tbody.find_all('tr')

    for tr in tr_list:
        tr: element.Tag # type hint

        title = tr.select_one('div.ellipsis.rank01 > span > a').text
        artist = tr.select_one('div.ellipsis.rank02 > span > a').text
        album = tr.select_one('div.ellipsis.rank03 > a').text
        rt = f'{rank}\t{title}\t{artist}\t{album}\n'
        print(rt, end='')
        print('-' * 30)
        f.write(rt)
        rank += 1

browser.close()
print('크롤링 끝')
