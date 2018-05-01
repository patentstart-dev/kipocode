from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import os


def kipocode_get(person_type, socialcode):

    #초기값 설정
    kipocode = ""

    # 드라이버 접속을 위한 option 설정
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    #options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ROOT_DIR = os.path.dirname(BASE_DIR)
    CHROME_DIR = os.path.join(BASE_DIR,'chromedriver')

    # headless 크롬 드라이버를 이용한 접속
    #driver = webdriver.Chrome(CHROME_DIR, chrome_options=options)
    driver = webdriver.Chrome(chrome_options=options)


    # url에 접근한다.
    driver.get('https://www.patent.go.kr/jsp/ka/prestep/codeapp/CodeAppView.do')


    #  loading 화면이 없어질때까지 대기

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.invisibility_of_element_located((By.ID,'nppfs-loading-modal')))


    # 개인인 경우
    if person_type == "individual":

        # 입력 스팟 찾기
        resid1s=driver.find_elements_by_id("ResId1")
        resid2s=driver.find_elements_by_id("ResId2")

        # 입력
        resid1s[0].send_keys(socialcode.split("-")[0])
        resid2s[0].send_keys(socialcode.split("-")[1])

        # 이전 창 데이터
        # window_before = driver.window_handles[0]
        # print(window_before)

        # 실행버튼
        driver.execute_script("apagtCdCheck(); return false;")

        # 팝업 윈도우 이동
        driver.switch_to.window("apagtCdCheck")

        # 크롤링
        html=driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        kipocode = ""

        try:
            kipocode = soup.find(class_='txtPointS').get_text().strip()
        except:
            print("KIPOCODE None")

        # 모든 윈도우 종료
        driver.quit()

        #driver.switch_to.window(window_before)
        #driver.close()

        return kipocode



    # 법인인 경우
    if person_type == "corporate":

        # 법인 입력창으로 이동
        driver.find_elements_by_id("ApTp")[1].click()
        select=driver.execute_script("fnCheckApTp('ApTp_2')")

        # 입력 스팟 찾기
        resid1s=driver.find_elements_by_id("ResId1")
        resid2s=driver.find_elements_by_id("ResId2")

        # 입력
        resid1s[1].send_keys(socialcode.split("-")[0])
        resid2s[1].send_keys(socialcode.split("-")[1])

        # 실행버튼
        driver.execute_script("apagtCdCheck(); return false;")

        # 윈도우 이동
        driver.switch_to.window("apagtCdCheck")

        # 크롤링
        html=driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        kipocode = ""

        try:
            kipocode = soup.find(class_='txtPointS').get_text().strip()
        except:
            print("KIPOCODE None")

        # 모든 윈도우 종료
        driver.quit()

        return kipocode


    return "person_type error"
