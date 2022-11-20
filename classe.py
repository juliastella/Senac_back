# Código com as classes:

class Conta_corrente():
    def __init__(self, numeroConta, nomeTitular, saldoCorrente):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.saldoCorrente = saldoCorrente 
        pass

    """def sacar(self, ):"""
    """def depositar(self, ):"""
    """def aplicar(self, ):"""


class Conta_poupaca(Conta_corente):
    def __init__(self,saldoPoupaca,numeroConta,nomeTitular):
        super().__init__(numeroConta,nomeTitular)
        self.saldoPoupaca = saldoPoupaca
        pass

    """def resgatar(self, ):"""
    """def transferir(self, ):"""