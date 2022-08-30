from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def logaremail(user, password):
    navegador = webdriver.Chrome(ChromeDriverManager().install())
    navegador.get('https://login.live.com/')
    sleep(3)
    navegador.find_element('xpath', '//*[@id="i0116"]').click()
    sleep(1)
    navegador.find_element('xpath', '//*[@id="i0116"]').send_keys(f'{user}')
    sleep(1)
    navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
    sleep(3)
    navegador.find_element('xpath', '//*[@id="i0118"]').click()
    sleep(1)
    navegador.find_element('xpath', '//*[@id="i0118"]').send_keys(f'{password}')
    sleep(1)
    navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
    sleep(3)
    navegador.find_element('xpath', '//*[@id="KmsiCheckboxField"]').click()
    sleep(1)
    navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
    sleep(20)


usuario = str(input('Digite seu email de login: ')).strip()
senha = str(input('Digite sua senha: ')).strip()

logaremail(usuario, senha)


