# selenium/webpage_open.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_experimental_option("detach", True) # 브라우저가 자동으로 닫히지 않도록 설정
opts.add_argument("--headless=new") # 최신 버전의 headless 모드 사용
opts.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options = opts)

try:
    driver.get("https://www.python.org")
    print(f"title: {driver.title}")
finally:
    # driver.quit()
    pass