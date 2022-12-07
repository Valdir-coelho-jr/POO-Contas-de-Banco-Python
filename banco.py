import contas
import pessoas

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
        
    def checar_agencias(self, conta):
        if conta.agencia in self.agencias:
            print('checar_agencias', True)
            return True
        return False
        
    def checar_clientes(self, cliente):
        if cliente in self.clientes:
            print('checar_clientes', True)
            return True
        return False
        
    def checar_contas(self, conta):
        if conta in self.contas:
            print('checar_contas', True)
            return True
        return False
    
    def conta_is_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('conta_is_cliente', True)
            return True
        return False
    
    def autenticador(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self.checar_agencias(conta)   and \
               self.checar_clientes(cliente) and \
               self.checar_contas(conta) and \
               self.conta_is_cliente(cliente, conta)

    def __repr__(self):
        classe_nome = type(self).__name__
        representado = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{classe_nome}{representado}'

if __name__ == '__main__':
    c1 = pessoas.Cliente('João', 22)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Valdir', 28)
    cp1 = contas.ContaPoupanca(112, 222, 0)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])
    
    print(banco.autenticador(c1, cc1))
    print(banco)
    
    if banco.autenticador (c1, cc1):
        cc1.deposito(10)
        print(c1.conta)
