# selenium/4.wait.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

opts = Options()
opts.add_experimental_option("detach", True)
# opts.add_argument("--headless==new")
opts.add_argument("--window-size=1280,900")
driver = webdriver.Chrome(options = opts)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.melon.com")
    wait.until(lambda d: d.title != "" )
    print(f"title:{driver.title}")

    elem= wait.until(
        EC.visibility_of_element_located((By.ID, "top_search")))
    elem.clear()
    elem.send_keys("exo")
    elem.send_keys(Keys.ENTER)

    #[앨범] 탭으로 이동
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="앨범 - 페이지 이동"]'))).click()
    
    # 첫 번째 앨범 클릭
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frm"]/div/ul/li[1]/div/div/dl/dt/a'))).click()
    
    # 첫 번째 곡 가사 클릭
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frm"]/div/table/tbody/tr[1]/td[3]/div/a'))).click()

    # 곡 제목 출력
    title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="downloadfrm"]/div/div/div[2]/div[1]/div[1]/text()'))).text
    print(f"곡 제목: {title}")
    
finally:
    #driver.quit()
    pass