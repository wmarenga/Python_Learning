from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class EdgeAuto:
    def __init__(self):
        self.driver_path = '145_selenium_automatizando_tarefas_no_navegador/msedgedriver.exe'
        self.options = webdriver.EdgeOptions()
        self.options.add_argument(
            r'user-data-dir=C:\Users\wmare\AppData\Local\Microsoft\Edge\User Data\Default')
        self.edge = webdriver.Edge(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.edge.find_element(By.LINK_TEXT, 'Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def acessa(self, site):
        self.edge.get(site)

    def sair(self):
        self.edge.quit()

    def faz_login(self):
        try:
            input_login = self.edge.find_element(
                By.ID, 'login_field')  # Achar o id do campo HTML
            input_login.send_keys('email@yahoo.ca')

            input_password = self.edge.find_element(
                By.ID, 'password')
            input_password.send_keys('1234')

            btn_login = self.edge.find_element(By.LINK_TEXT, 'Sign in')
            btn_login.click()

        except Exception as e:
            print('Erro ao fazer login:', e)


"""
    def clica_perfil(self):
        try:
            perfil = self.edge.find_element(By.CSS_SELECTOR,
                                            'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            perfil = self.edge.find_element(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro fazer logout:', e)

    def verifica_usuario(self, usuario):
        profile_link = self.edge.find_element('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html
"""

if __name__ == '__main__':
    edge = EdgeAuto()
    edge.acessa('https://github.com')

    # edge.clica_perfil()
    # edge.faz_logout()

    edge.clica_sign_in()
    edge.faz_login()

    sleep(15)
    edge.sair()
    # edge.clica_perfil()
    # edge.verifica_usuario('otaviomirandabr')
