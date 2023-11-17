class Dado:
    def __init__(self, nome, data_nascimento, rua, numero_casa, bairro, cidade, 
                estado, pais, cep, cpf, cnh, rg, celular, telefone, email):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.rua = rua
        self.numero_casa = numero_casa
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.cep = cep
        self.cpf = cpf
        self.cnh = cnh
        self.rg = rg
        self.celular = celular
        self.telefone = telefone
        self.email = email

    def altera_nome(self):
        if self.nome == '[Não encontrado]':
            self.nome = 'nome'
        
        if self.data_nascimento == '[Não encontrado]':
            self.data_nascimento = 'data_nascimento'

        if self.rua == '[Não encontrado]':
            self.rua = 'rua'

        if self.numero_casa == '[Não encontrado]':
            self.numero_casa = 'numero_casa'

        if self.bairro == '[Não encontrado]':
            self.bairro = 'bairro'

        if self.cidade == '[Não encontrado]':
            self.cidade = 'cidade'
        
        if self.estado == '[Não encontrado]':
            self.estado = 'estado'

        if self.pais == '[Não encontrado]':
            self.pais = 'pais'

        if self.cep == '[Não encontrado]':
            self.cep = 'cep'
        
        if self.cpf == '[Não encontrado]':
            self.cpf = 'cpf'

        if self.cnh == '[Não encontrado]':
            self.cnh = 'cnh'

        if self.rg == '[Não encontrado]':
            self.rg = 'rg'

        if self.celular == '[Não encontrado]':
            self.celular = 'celular'

        if self.telefone == '[Não encontrado]':
            self.telefone = 'telefone'

        if self.email == '[Não encontrado]':
            self.email = 'email'

    def lista_dados_coletados(self):
        # Cria uma lista com os dados diferentes de '[Não encontrado]'
        lista_dados_encontrados = [self.nome, self.data_nascimento, self.rua,
                                   self.numero_casa, self.bairro, self.cidade,
                                   self.estado, self.pais, self.cep, self.cpf,
                                   self.cnh, self.rg, self.celular,
                                   self.telefone, self.email]

        # Filtra a lista para remover '[Não encontrado]'
        lista_dados_encontrados = [dado for dado in lista_dados_encontrados if dado != '[Não encontrado]']

        return lista_dados_encontrados

    def lista_dados_coletados_alterados(self):
        self.altera_nome()
        lista_dados = [self.nome, self.data_nascimento, self.rua,
        self.numero_casa, self.bairro, self.cidade, self.estado, 
        self.pais, self.cep, self.cpf, self.cnh, self.rg, self.celular,
        self.telefone, self.email]

        return lista_dados
        

        