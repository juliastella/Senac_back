# Bibliotecas:
import random
import time


# Bibliotecas:

# Código com as classes:

class Conta_corrente():
    def __init__(self, numeroConta, nomeTitular, saldoCorrente):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.__saldoCorrente = saldoCorrente

    # get e set para o atributo saldoCorrente:
    def get_saldoCorrente(self):
        return self.__saldoCorrente

    def set_saldoCorrente(self, novo_saldoCorrente):
        self.__saldoCorrente = novo_saldoCorrente

    # get e set para o atributo saldoCorrente:
    def sacar(self, valorDeposito):
        self.__saldoCorrente -= valorDeposito

    def depositar(self, valorDeposito):
        self.__saldoCorrente += valorDeposito

    def aplicar(self, investimentoIn):
        self.__saldoCorrente -= investimentoIn


# Area de teste para verificar o funcionamento das classe:
"""valorDeposito = float(input("Qual é o deposito? "))

investimentoIn = float(input("Qual é o investimento? "))

pessoa1 = Conta_corrente(1234,"júlia", 100)
pessoa1.depositar(valorDeposito)
pessoa1.sacar(valorDeposito)
pessoa1.aplicar(investimentoIn)

print(pessoa1.saldoCorrente)"""


# Area de teste para verificar o funcionamento das classe:
class Conta_poupaca(Conta_corrente):
    def __init__(self, saldoPoupaca, numeroConta, nomeTitular, saldoCorrente):
        super().__init__(numeroConta, nomeTitular, saldoCorrente)
        self.__saldoPoupaca = saldoPoupaca

    # get e set para o atributo saldoCorrente:
    def get_saldoPoupaca(self):
        return self.__saldoPoupaca

    def set_saldoPoupanca(self, novo_saldoPoupaca):
        self.__saldoPoupaca = novo_saldoPoupaca

    # Metodo da função  conta poupaça:
    def resgatar(self):
        self.__saldoPoupaca -= self.__saldoCorrente


# Teste do metodo:
"""pessoa2 = Conta_poupaca(1234,"júlia", 50, 200)
pessoa2.resgatar()
print(pessoa2.saldoCorrente, "E", pessoa2.saldoPoupaca)"""

# inicio da construção do menu e das condicionais:

# Variaveis :

dicionario = {}
nome = None
idade = None
senha = None
num_conta = None
deposito = None

# Menu:
while True:
    print("Bem Vindo ao Senac Bank")
    print(""" 

        +------------------------------+
        |         -Senac Bank-         | 
        |                              |
        | [1] Criar conta              |
        | [2] Mostrar dados            |
        | [3] Acessar Conta Corrente   | 
        | [4] Acessar Conta Poupança   |
        | [5] Sair                     |
        |                              | 
        +-------------------------------+                               
                                         \n""")

    opcao = input("Qual a opção que você deseja escolher: ")

    # Funções base:
    def validaIdade(idade):
        if idade < 18:
            print('Você é menor de idade!')
        else:
            print('\nAguarde...')
            time.sleep(2.0)

            print('\nNome: ', nome)

    # Opção 01: criar conta:

    if opcao == 1:
        nome = str(input('\nDigite seu nome: '))
        idade = int(input('Digite sua idade: '))
        num_conta = random.randint(100, 500)
        validaIdade(idade)

        while True:
            senha = int(input('Digite uma senha de 4 digítos: '))

            if len(str(senha)) != 4:
                print("Digite uma senha de apenas 4 digítos, por favor!")
                continue
            else:
                print("Senha cadastrada com sucesso!")
                break

        print("Para concluir o cadastro você precisa deposita o valor minimo de 20!")

        deposito = float(input("Faço o seu deposito: "))

    elif opcao == 2:
        print()
    else:
        break