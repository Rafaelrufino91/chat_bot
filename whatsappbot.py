from selenium import webdriver
from time import sleep


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Testando o envio de mensagem com bot"
        self.conversas = ["Amor", "Naturfit"]
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path='/home/Rafael/Documentos/GitHub/chatbot/chromedriver')

    def enviarmensagem(self):
        self.driver.get("https://web.whatsapp.com/")
        sleep(30)
        for grupo in self.conversas:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            sleep(4)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name("p3_M1")
            sleep(4)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            sleep(4)
            botao_enviar.click()
            sleep(4)

bot = WhatsappBot()
bot.enviarmensagem()


