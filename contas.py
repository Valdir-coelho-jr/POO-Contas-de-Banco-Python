import abc

class Conta:
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def saque(self):
        ...
        
    def deposito(self, valor: float) -> float:
        self.saldo += valor
        self.conta_info(f'DEPOSITO RALIZADO: R${valor:.2f}')
        return self.saldo
        
    def conta_info(self, msg=''):
        print(f'{msg}\nSALDO ATUAL: R${self.saldo:.2f}\n-------')
    
    def __repr__(self):
        classe_nome = type(self).__name__
        representado = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{classe_nome}{representado}'
        
class ContaPoupanca(Conta):
    def saque(self, valor):
        analisa_valor = self.saldo - valor
        if analisa_valor >= 0:
            self.saldo -= valor
            self.conta_info(f'SAQUE REALIZADO: R${valor:.2f}')
            return self.saldo
        print('Não foi possível realizar a operação')
        self.conta_info(f'SAQUE NEGADO: R${valor:.2f}\n')
        
class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        
    def saque(self, valor):
        analisa_valor = self.saldo - valor
        limite_max = -self.limite
        
        if analisa_valor >= limite_max:
            self.saldo -= valor
            self.conta_info(f'SAQUE REALIZADO: R${valor:.2f}')
            return self.saldo
        print('Não foi possível realizar a operação')
        self.conta_info(f'SAQUE NEGADO: R${valor:.2f}\n')
        print(f'Seu saldo limite é de: R${limite_max:.2f}')
        
if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 2221)
    cp1.deposito(50)
    cp1.saque(40)
    cp1.saque(70)
    print()
    cc1 = ContaCorrente(111, 2221, 1.50)
    cc1.deposito(50)
    cc1.saque(100)
    cc1.saque(55)
