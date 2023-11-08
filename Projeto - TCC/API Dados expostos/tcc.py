from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import networkx as nx
import matplotlib.pyplot as plt

driver = webdriver.Chrome()

driver.get('file:///C:/Users/VAIO/Desktop/Projeto%20-%20TCC/indexMarcela.html')

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

# armazena os dados em uma lista
dados_pessoais = [nome, data_nascimento, rua, numero_casa, bairro, 
                  cidade, estado, pais, cep, cpf, 
                  cnh, rg, celular, telefone, email]

# relações entre os dados pessoais
relacoes = [
    (numero_casa, rua), (rua, bairro), (bairro, cidade), (cidade, estado), (estado, pais), (cep, estado), (cep, cidade), 
    (cep, bairro), (cep, rua), (cep, nome), (nome, email), (nome, rg), (nome, cpf), (email, data_nascimento), 
    (email, celular), (celular, cpf), (cpf, rg), (cpf, telefone), (cpf, data_nascimento), (rg, data_nascimento), (cpf, cnh)
]

# Cria um grafo
G = nx.Graph()

for dado in dados_pessoais:
    if dado == '[Não encontrado]':
        pass
    else:
        G.add_node(dado)
        for dado_origem, dado_destino in relacoes:
            if dado_origem == '[Não encontrado]' or dado_destino == '[Não encontrado]':
                pass
            else:
                G.add_edge(dado_origem, dado_destino)
        
distancias = (nx.number_of_edges(G) / 21) * 100

print(f"O nível de exposição da {nome} é: {distancias:.2f}")

nx.draw(G, with_labels=True, node_size=100, node_color='yellow')
plt.show()

