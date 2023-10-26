class ContaBancaria:

    def __init__(self, numero, saldo, nome, tipo, status, limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.limite = limite

    def depositar(self, ValorDeposito):

        if self.status == True:
            self.saldo += ValorDeposito
        else:
            print("Conta Invalida")

    def sacar(self, ValorSaque):

        if self.status == True:
            if self.saldo < ValorSaque:
                print("Saldo invalido")
            else:
                self.saldo -= ValorSaque
                print(f"Saque no valor de {ValorSaque} realizado com sucesso")
        else:
            print("Conta Invalida")

    def ativarconta(self):
        if self.status == True:
            print("Sua conta já está ativa")
        else:
            self.status = True
            print("Conta Ativada!!")

    def verificarsaldo(self):

        if self.status == True:
            print(f"Seu saldo atual é de R${self.saldo}")
        else:
            print("Conta Invalida")