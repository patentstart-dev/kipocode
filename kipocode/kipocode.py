from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import os


def kipocode_get(person_type, socialcode):

    #초기값 설정
    kipocode = "NONE"

    # 드라이버 접속을 위한 option 설정
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ROOT_DIR = os.path.dirname(BASE_DIR)
    CHROME_DIR = os.path.join(BASE_DIR,'chromedriver')

    print(CHROME_DIR)

    # headless 크롬 드라이버를 이용한 접속
    driver = webdriver.Chrome(CHROME_DIR, chrome_options=options)
    #driver = webdriver.Chrome(chrome_options=options)


    # url에 접근한다.
    driver.get('https://www.patent.go.kr/jsp/ka/prestep/codeapp/CodeAppView.do')


    # security, loading 화면이 없어질때까지 대기

    try:
        wait = WebDriverWait(driver, 5)
        element = wait.until(EC.invisibility_of_element_located((By.ID,'nppfs-loading-modal')))
        print("Alert None")
    except:
        alert = driver.switch_to.alert
        alert.dismiss()
        print("Alert Dismissed")


    # 개인인 경우
    if person_type == "individual":

        # 입력 스팟 찾기
        resid1s=driver.find_elements_by_id("ResId1")
        resid2s=driver.find_elements_by_id("ResId2")

        # 입력
        resid1s[0].send_keys(socialcode.split("-")[0])
        resid2s[0].send_keys(socialcode.split("-")[1])

        # 이전 창 데이터
        window_before = driver.window_handles[0]
        print(window_before)

        # 실행버튼
        driver.execute_script("apagtCdCheck(); return false;")


        # 팝업 윈도우 이동
        # window_child=window_before+".0.child"
        window_child=driver.window_handles[1]
        
        try:
            wait3 = WebDriverWait(driver, 1)
            element3 = wait3.until(EC.visibility_of_element_located((By.ID, 'pop_content')))
            print("switch wait")
        except:
            print("switch non wait")


        driver.switch_to.window(window_child)

        # 크롤링
        html=driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        #rint(html)
        #rint(soup)

        try:
            kipocode = soup.find(class_='txtPointS').get_text().strip()
            print(soup.find(class_='txtPointS'))
        except:
            print("KIPOCODE None")

        # 모든 윈도우 종료
        driver.quit()

        #driver.switch_to.window(window_before)
        #driver.close()

        print(kipocode)

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

        # 팝업 윈도우 이동
        # window_child=window_before+".0.child"
        window_child=driver.window_handles[1]

        try:
            wait3 = WebDriverWait(driver, 1)
            element3 = wait3.until(EC.visibility_of_element_located((By.ID, 'pop_content')))
            print("switch wait")
        except:
            print("switch non wait")


        driver.switch_to.window(window_child)

        # 크롤링
        html=driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        try:
            kipocode = soup.find(class_='txtPointS').get_text().strip()
        except:
            print("KIPOCODE None")

        print(kipocode)

        return kipocode


    return "person_type error"



        
