import json

class ContaCorrente:
    def __init__(self, nome_correntista, cpf_correntista, saldo):
        self.nome_correntista = nome_correntista
        self.cpf_correntista = cpf_correntista
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        print("Nome:", self.nome_correntista)
        print("CPF:", self.cpf_correntista)
        print("Saldo:", self.saldo)

    def informacoes(self):
        dados = {
            "nome": self.nome_correntista,
            "cpf": self.cpf_correntista,
            "saldo": self.saldo
        }

        with open("conta.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

        print("Dados salvos em conta.json")


# Criando conta
conta = ContaCorrente("Ana", "202.507.099-00", 1000)

# Usando métodos
conta.depositar(100)
conta.sacar(75)
conta.mostrar_saldo()

# Salvando em JSON
conta.informacoes()