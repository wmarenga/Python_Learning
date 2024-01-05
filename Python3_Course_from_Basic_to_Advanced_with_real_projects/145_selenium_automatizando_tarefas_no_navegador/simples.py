from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

username = "email@yahoo.ca"
password = "1234"

driver = webdriver.Chrome(
    r'145_selenium_automatizando_tarefas_no_navegador/chromedriver.exe')

driver.get("https://github.com/login")
driver.find_element(By.ID, "login_field").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.NAME, "commit").click()

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
errors = driver.find_elements(By.CLASS_NAME, "flash-error")

if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

driver.find_element(
    By.CSS_SELECTOR, r"body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary").click()
sleep(5)
driver.find_element(
    By.CSS_SELECTOR, r"body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form").click()

sleep(5)
driver.quit()
