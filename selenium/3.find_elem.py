# selenium/3.find_elem.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.add_experimental_option("detach", True) # 브라우저가 자동으로 닫히지 않도록 설정
# opts.add_argument("--headless=new") # 최신 버전의 headless 모드 사용
opts.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options = opts)

try:
    driver.get("https://www.python.org")
    print(f"title: {driver.title}")
    
    elem_input = driver.find_element(By.ID, "id-search-field")
    elem_input.clear() # 입력창 초기화
    elem_input.send_keys("list")
    elem_input.send_keys(Keys.ENTER)

finally:
    # driver.quit()
    pass