#셀레늄: 웹 자동화 및 웹의 소스코드를 수집하는 모듈
# cmd -> pip install selenium (셀레늄 라이브러리 다운로드)

#셀레늄 임포트
import time as t
from selenium import webdriver
# XPath 등을 통해 요소를 지목하기 위한 클래스
from selenium.webdriver.common.by import By

#from webdriver_manager.chrome import ChromeDriverManager

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 이용하게 해주는 코드
#service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
#driver = webdriver.Chrome(options=option, service=service)
driver = webdriver.Chrome(options=option)

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')

t.sleep(1.5)

# 자동으로 버튼이나 링크 클릭 제어하기
# XPath -> XML Path Language
# -> 문서의 특정 요소나 속성에 접근하기 위한 경로로 지정하는 언어
# -> 요소를 중복 없이 정확하게 표현하기 쉬운 언어
login_btn = driver.find_element(By.XPATH, '//*[@id="account"]/div/a')
login_btn.click()

t.sleep(1)
# 자동으로 텍스트를 입력하기
id_input = driver.find_element(By.XPATH, '//*[@id="id"]')
id_input.send_keys('pineapple')

t.sleep(1)
driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys('aaa1111!')

t.sleep(1)
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()