# Código com as classes:

class Conta_corrente():
    def __init__(self, numeroConta, nomeTitular, saldoCorrente):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.saldoCorrente = saldoCorrente

    def sacar(self, valorDeposito):
        self.saldoCorrente -= valorDeposito
    def depositar(self, valorDeposito):
        self.saldoCorrente += valorDeposito

"""    def aplicar(self, ):"""



valorDeposito = float(input("Qual é o deposito? "))

pessoa1 = Conta_corrente(1234,"júlia", 100)
pessoa1.depositar(valorDeposito)
pessoa1.sacar(valorDeposito)

print(pessoa1.saldoCorrente)

"""class Conta_poupaca(Conta_corrente):
    def __init__(self,saldoPoupaca,numeroConta,nomeTitular):
        super().__init__(numeroConta, nomeTitular)
        self.saldoPoupaca = saldoPoupaca
        pass
"""
"""def resgatar(self, ):"""
"""def transferir(self, ):"""