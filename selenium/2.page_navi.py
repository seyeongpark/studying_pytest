# selenium/2.page_navi.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_experimental_option("detach", True)
# opts.add_argument("--headless==new")
opts.add_argument("--window-size=1280,900")
driver = webdriver.Chrome(options = opts)

try:
    driver.get("https://www.python.org")
    print(f"title: {driver.title}")

    time.sleep(1)
    driver.get("https://www.naver.com")
    print(f"title: {driver.title}")
    time.sleep(1)

    #page 뒤로가기, 앞으로가기, 새로고침
    driver.back()
    time.sleep(1)
    driver.forward()
    time.sleep(1)
    driver.refresh()
    time.sleep(1)

finally:
    #driver.quit()
    pass