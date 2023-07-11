from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.login = 'email@yahoo.ca'
        self.password = '1234'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            r'user-data-dir=C:\Users\wmare\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(
            r'145_selenium_automatizando_tarefas_no_navegador/chromedriver.exe')

    def clica_sign_in(self):
        try:
            self.chrome.get("https://github.com/login")
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            self.chrome.find_element(
                By.CSS_SELECTOR, r'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary').click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            self.chrome.find_element(
                By.CSS_SELECTOR, r'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form').click()
        except Exception as e:
            print('Erro fazer logout:', e)

    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element(
            By.CLASS_NAME, 'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def faz_login(self):
        try:
            self.chrome.find_element(
                By.ID, "login_field").send_keys(self.login)
            self.chrome.find_element(
                By.ID, "password").send_keys(self.password)
            self.chrome.find_element(By.NAME, "commit").click()

        except Exception as e:
            print('Erro ao fazer login:', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_perfil()
    chrome.faz_logout()

    chrome.clica_sign_in()
    chrome.faz_login()

    chrome.clica_perfil()
#    chrome.verifica_usuario('wmarenga')
    sleep(7)
    chrome.faz_logout()

    sleep(10)
    chrome.sair()
