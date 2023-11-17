from selenium import webdriver
from selenium.webdriver.common.by import By
from Dado import Dado
from Grafo import Grafo

class Principal:
    def run(self):
        url = 'file:///C:/Users/VAIO/Desktop/API/indexManuela.html'
        dados_selenium = self.seleniumScraper(url)
        dados = Dado(*dados_selenium)
        lista_dados_encontrados = dados.lista_dados_coletados()
        lista_dados_ajustados = dados.lista_dados_coletados_alterados()
        grafo_gerado = Grafo()
        print(grafo_gerado.gera_grafo(lista_dados_encontrados, lista_dados_ajustados))


    def seleniumScraper(self, url):
        driver = webdriver.Chrome()
        driver.get(url)

        #primeira aba - sobre
        nome = driver.find_element(By.ID, 'full-name').text
        data_nascimento = driver.find_element(By.ID, 'birthday').text

        #segunda aba - localização
        aba_localizacao = driver.find_element(By.ID, 'location').click()
        rua = driver.find_element(By.ID, 'address').text
        numero_casa = driver.find_element(By.ID, 'number').text
        bairro = driver.find_element(By.ID, 'district').text
        cidade = driver.find_element(By.ID, 'city').text
        estado = driver.find_element(By.ID, 'state').text
        pais = driver.find_element(By.ID, 'country').text
        cep = driver.find_element(By.ID, 'cep').text

        #terceira aba - dados
        aba_dados = driver.find_element(By.ID, 'data').click()
        cpf = driver.find_element(By.ID, 'cpf').text
        cnh = driver.find_element(By.ID, 'cnh').text
        rg = driver.find_element(By.ID, 'rg').text

        #quarta aba - contato
        aba_contact = driver.find_element(By.ID, 'contact').click()
        celular = driver.find_element(By.ID, 'smartphone').text
        telefone = driver.find_element(By.ID, 'telephone').text
        email = driver.find_element(By.ID, 'email').text

        driver.close()

        return nome, data_nascimento, rua, numero_casa, bairro, cidade, estado, \
            pais, cep, cpf, cnh, rg, celular, telefone, email

if __name__ == '__main__':
    main_program = Principal()
    main_program.run()
