# Código com as classes:

class Conta_corrente():
    def __init__(self, numeroConta, nomeTitular, saldoCorrente):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.saldoCorrente = saldoCorrente

#get e set para o atributo saldoCorrente:
    def get_saldoCorrente(self):
        return self._saldoCorrente
    def set_saldoCorrente(self, novo_saldoCorrente):
        self._saldoCorrente = novo_saldoCorrente

# get e set para o atributo saldoCorrente:
    def sacar(self, valorDeposito):
        self.saldoCorrente -= valorDeposito
    def depositar(self, valorDeposito):
        self.saldoCorrente += valorDeposito

    def aplicar(self,investimentoIn):
        self.saldoCorrente -= investimentoIn



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
    def __init__(self,saldoPoupaca,numeroConta,nomeTitular,saldoCorrente):
        super().__init__(numeroConta, nomeTitular, saldoCorrente)
        self.saldoPoupaca = saldoPoupaca
        pass

# get e set para o atributo saldoCorrente:
    def get_saldoPoupaca(self):
        return self._saldoPoupaca

    def set_saldoCorrente(self, novo_saldoPoupanca):
        self._saldoCorrente = novo_saldoPoupanca

# Metodo da função  conta poupaça:
    def resgatar(self):
        self.saldoPoupaca -= self.saldoCorrente

#Teste do metodo:
pessoa2 = Conta_poupaca(1234,"júlia", 50, 200)
pessoa2.resgatar()
print(pessoa2.saldoCorrente, "E", pessoa2.saldoPoupaca)
