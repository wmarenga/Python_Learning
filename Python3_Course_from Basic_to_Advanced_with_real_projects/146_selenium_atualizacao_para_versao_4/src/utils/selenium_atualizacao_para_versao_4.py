from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent

# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'

# *options == *args


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    # Example
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')
    browser.find_element(By.CLASS_NAME, 'FYXSad').click()
    browser.find_element(
        By.CSS_SELECTOR, '#tbTubd > div > li:nth-child(35)').click()
    browser.find_element(By.CSS_SELECTOR, '#W0wltc > div').click()

    input_element = browser.find_element(By.NAME, 'q')
    input_element.send_keys('Python')
    sleep(5)
    # Para pressionar o "ENTER"
    input_element.send_keys(Keys.ENTER)
    sleep(5)
    browser.quit()
