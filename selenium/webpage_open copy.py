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

    driver.find_element(By.CSS_SELECTOR, '[href="javascript:melon.link.goTotalSearch(\'exo\',\'album\',\'searchFrm\',\'\',\'\',\'N\');"]').click()

finally:
    #driver.quit()
    input("대기중... 엔터 누르면 종료")