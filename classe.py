# Bibliotecas:
import random
import time

import self as self


# Bibliotecas:

# Código com as classes:

class Conta_corrente():
    def __init__(self, numeroConta, nomeTitular, saldoCorrente, saldoPoupaca):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.__saldoCorrente = 0
        self.__saldoPoupaca = 0

    # get e set para o atributo saldoCorrente:
    def get_saldoCorrente(self):
        return self.__saldoCorrente

    def set_saldoCorrente(self, novo_saldoCorrente):
        self.__saldoCorrente = novo_saldoCorrente

    # get e set para o atributo saldoPoupaca:
    def get_saldoPoupaca(self):
        return self.__saldoPoupaca

    def set_saldoPoupanca(self, novo_saldoPoupaca):
        self.__saldoPoupaca = novo_saldoPoupaca

   # Metodos:
    def sacar(self, valorDeposito):
        if valorDeposito > self.get_saldoCorrente():
            print("+------------------------------------------------+")
            print(f"| Saldo insuficiente {self.get_saldoCorrente()} |")
            print("+------------------------------------------------+")
        else:
            s_atual = self.get_saldoCorrente()
            s_atual -= valorDeposito
            self.set_saldoCorrente(s_atual)
            print("+-------------------------------+")
            print("| O saque efetuado com sucesso! |")
            print("+-------------------------------+")

    def depositar(self, valorDeposito):
        self.__saldoCorrente += valorDeposito
        print("+----------------------------------+")
        print("| O depósito efetuado com sucesso! |")
        print("+----------------------------------+")

    def aplicar(self, investimentoIn):
        saldoc = self.get_saldoCorrente()
        saldop = self.get_saldoPoupaca()

        if investimentoIn <= saldoc:
            saldoc -= investimentoIn
            saldop -= investimentoIn
            self.set_saldoCorrente(saldoc)
            self.set_saldoPoupanca(saldop)

        print("+----------------------------------+")
        print("| O aplicação efetuada com sucesso! |")
        print("+----------------------------------+")

valorDeposito = float(input("Qual é o deposito? "))

investimentoIn = float(input("Qual é o investimento? "))

pessoa1 = Conta_corrente(1234,"júlia", 100, 50)
pessoa1.depositar(valorDeposito)
pessoa1.sacar(valorDeposito)
pessoa1.aplicar(investimentoIn)

class Conta_poupaca(Conta_corrente):
    def __init__(self, saldoPoupaca, numeroConta, nomeTitular, saldoCorrente):
        super().__init__(numeroConta, nomeTitular, saldoCorrente, saldoPoupaca)

    # Metodo da função  conta poupaça:
    def resgatar(self):
        self.__saldoPoupaca -= self.__saldoCorrente
        print("+----------------------------------+")
        print("| O resgate efetuada com sucesso!  |")
        print("+----------------------------------+")




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
    print("\nBem Vindo ao Senac Bank")
    print(""" 

        +------------------------------+
        |         -Senac Bank-         | 
        |                              |
        | [1] Criar conta              |
        | [2] Mostrar dados            |
        | [3] Aplicar                  |
        | [4] Resgatar                 |
        | [5] Sacar                    | 
        | [6] Mostrar dados            |
        | [7] Sair                     |
        |                              | 
        +-------------------------------+                               
                                         \n""")

    opcao = int(input("Qual a opção que você deseja escolher: "))

    # Funções base:
    def validaIdade(idade):
        if idade < 18:
            print('Você é menor de idade!')
        else:
            print('\nAguarde...')
            time.sleep(2.0)

    # Opção 01: criar conta:
    if opcao == 1:
        nome = str(input('\nDigite seu nome: '))
        idade = int(input('Digite sua idade: '))
        num_conta = random.randint(100, 500)
        validaIdade(idade)

        while True:
            print("\nPara concluir o cadastro você precisa deposita o valor minimo de 20!\n")
            deposito = float(input("\nFaço o seu deposito: \n"))
            senha = int(input('\nDigite uma senha de 4 digítos: \n'))

            if len(str(senha)) != 4 and deposito >= 20.00:
                if deposito >= 20.00:
                  print("Digite uma senha de apenas 4 digítos e deposite o valor igual ou maior que R$ 20,00!")
                continue
            else:
                print("Senha cadastrada e deposito com sucesso!")
                break



# Terminar mostrar os dados:

    elif opcao == 6:
        print("\nOs seus dados no Senac Bank")
        print(f""" 

             +------------------------------+
             |         -Senac Bank-         | 
             |                              |
             | [Nome] {nome}                |
             | [Idade] {idade}              |
             | [Número da conta] {num_conta}| 
             +-------------------------------+                               
                                              \n""")





    else:
        break