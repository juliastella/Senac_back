class Conta_corrente():
    def __init__(self, numeroConta, nomeTitular, saldoCorrente):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.__saldoCorrente = 0

    # get e set para o atributo saldoCorrente:
    def get_saldoCorrente(self):
        return self.__saldoCorrente

    def set_saldoCorrente(self, novo_saldoCorrente):
        self.__saldoCorrente = novo_saldoCorrente

    # get e set para o atributo saldoCorrente:
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
        self.saldoCorrente -= investimentoIn
        self.saldoPoupaca += investimentoIn


class Conta_poupaca(Conta_corrente):
    def __init__(self, saldoPoupaca, numeroConta, nomeTitular, saldoCorrente):
        super().__init__(numeroConta, nomeTitular, saldoCorrente)
        self.__saldoPoupaca = 0

    # get e set para o atributo saldoCorrente:
    def get_saldoPoupaca(self):
        return self.__saldoPoupaca

    def set_saldoPoupanca(self, novo_saldoPoupaca):
        self.__saldoPoupaca = novo_saldoPoupaca

    # Metodo da função  conta poupaça:
    def resgatar(self):
        self.__saldoPoupaca -= self.__saldoCorrente
