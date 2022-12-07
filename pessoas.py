import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        
    def __repr__(self):
        classe_nome = type(self).__name__
        representado = f'({self.nome!r}, {self.idade!r})'
        return f'{classe_nome}{representado}'
    
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None
        
if __name__ == '__main__':
    c1 = Cliente('Japinha', 84)
    c1.conta = contas.ContaPoupanca(111, 221, 1.50)
    print(c1)
    print(c1.conta)
    