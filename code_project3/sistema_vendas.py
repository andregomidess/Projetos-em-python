from abc import ABC, abstractmethod

class vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []

    def get_codigo (self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_vendas(self):
        return self.__vendas

    def adicionaVenda(self, codImovel, mes, ano, valor):
        vendaa = venda(codImovel, mes, ano, valor, self)
        self.__vendas.append(vendaa)

    @abstractmethod
    def getDados(self):
        pass

    @abstractmethod
    def calculaRenda(self, mes, ano):
        pass


class venda:
    def __init__(self, codImovel, mesVenda, anoVenda, valorVenda, vendedor):
        self.__codImovel = codImovel
        self.__mesVenda = mesVenda
        self.__anoVenda = anoVenda
        self.__valorVenda = valorVenda
        self.__vendedor = vendedor

    def get_codImovel(self):
        return self.__codImovel

    def get_mesVenda(self):
        return self.__mesVenda

    def get_anoVenda(self):
        return self.__anoVenda

    def get_valorVenda(self):
        return self.__valorVenda

    def get_vendedor(self):
        return self.__vendedor

class Contratado(vendedor):
    def __init__(self, codigo, nome, salario_fixo, nro_cart_trabalho):
        super().__init__(codigo, nome)
        self.__salario_fixo = salario_fixo
        self.__nro_cart_trabalho = nro_cart_trabalho
        self.__comissao = 0.01
        
    def get_salario_fixo(self):
        return self.__salario_fixo    

    def get_nro_cart_trabalho(self):
        return self.__nro_cart_trabalho


    def getDados(self):
        return 'Nome: ' + self.get_nome() + ' - ' + 'Nro Carteira de trabalho: ' + str(self.__nro_cart_trabalho)


    def calculaRenda(self, mes, ano):
        sal = self.__salario_fixo
        for i in self.get_vendas():
            if i.get_mesVenda() == mes and i.get_anoVenda() == ano:
                sal += self.__comissao * i.get_valorVenda()
        return sal    


class Comissionado(vendedor):
    def __init__(self, codigo, nome, nro_cpf, comissao):
        super().__init__(codigo, nome)
        self.__nro_cpf = nro_cpf
        self.__comissao = comissao

    def get_nro_cpf(self):
        return self.__nro_cpf

    def get_comissao(self):
        return self.__comissao

    def getDados(self):
        return 'Nome: ' + self.get_nome() + ' - ' + 'Nro CPF: ' + str(self.__nro_cpf)

    def calculaRenda(self, mes, ano):
        sal = 0
        for i in self.get_vendas():
            if i.get_mesVenda() == mes and i.get_anoVenda() == ano:
                sal += (self.__comissao/100) * i.get_valorVenda()
        return sal  





funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
funcContratado.adicionaVenda(100, 3, 2022, 200000)
funcContratado.adicionaVenda(101, 3, 2022, 300000)
funcContratado.adicionaVenda(102, 4, 2022, 600000)
funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
funcComissionado.adicionaVenda(200, 3, 2022, 200000)
funcComissionado.adicionaVenda(201, 3, 2022, 400000)
funcComissionado.adicionaVenda(202, 4, 2022, 500000)
listaFunc = {funcContratado, funcComissionado}
for func in listaFunc:
    print (func.getDados())
    print ("Renda no mês 3 de 2022: ")
    print (func.calculaRenda(3, 2022))
