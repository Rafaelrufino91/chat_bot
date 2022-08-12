from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Definindo o caminho que vai acessar e baixando o driver do navegador
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
sleep(10)

# Mensagem que vai se enviada e para quem vai ser enviado
mensagem = "Testando o envio de mensagem. Nao precisa responder"
conversas = ["Gui Gui", "Naturfit"]


# Aqui ele vai buscar o contato na pesquisa
def buscar_contato(contato):
    pesquisar_contato = driver.find_element("xpath", '//div[contains(@class, "copyable-text selectable-text")]')
    sleep(3)
    pesquisar_contato.click()
    pesquisar_contato.send_keys(contato)
    sleep(3)
    pesquisar_contato.send_keys(Keys.ENTER)


def enviarmensagem(mensagem):
    chat_box = driver.find_element("xpath", '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div['
                                            '2]/div[1]')
    chat_box.click()
    sleep(3)
    chat_box.send_keys(mensagem)
    chat_box.send_keys(Keys.ENTER)


for conversa in conversas:
    buscar_contato(conversa)
    enviarmensagem(mensagem)
