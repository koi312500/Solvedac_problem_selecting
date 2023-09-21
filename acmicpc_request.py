from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui
import time

# 로그인할 사이트 목록 딕셔너리 정의

class BOJBot:
    def __init__(self, site):
        # 엣지 웹 드라이버
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)
        
        # 브라우저 해상도 설정
        self.driver.set_window_size(1600, 900)
        # 로그인하려는 사이트로 이동
        try:
            self.driver.get(site)
            # 10초 이하 대기
            self.driver.implicitly_wait(time_to_wait=10)
        except:
            print("Error occured")

    # 크롤러 종료
    def kill(self):
        self.driver.quit()

    # 로그인을 수행하는 메서드입니다.
    def login(self):
        print("Waiting for logining.... 15s")
        time.sleep(15)

    def self_add_problem(self, problem_list):
        print("You Loser")
        BOJ_box = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[3]/form/div/div[2]/div[2]/div/input')
        BOJ_box.send_keys(Keys.ENTER)
        for i in problem_list:
            time.sleep(0.01)
            BOJ_box.send_keys(i)
            time.sleep(0.01)
            BOJ_box.send_keys(Keys.ENTER)
        print("Waiting for finishing.... 15s")
        time.sleep(15)