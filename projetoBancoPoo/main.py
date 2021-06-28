from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca


banco = Banco()
cliente1 = Cliente ('Gabriel', 32)
cliente2 = Cliente('Tamires', 31)
cliente3 = Cliente('Piccolo Daimaoh', 63)

conta1 = ContaPoupanca(1111, 230489, 0)
conta2 = ContaCorrente(2222, 111289, 0)
conta3 = ContaPoupanca(1212, 110101, 0)

cliente1.inserirConta(conta1)
cliente2.inserirConta(conta2)
cliente3.inserirConta(conta3)

banco.inserirCliente(cliente1)
banco.inserirConta(conta1)

banco.inserirCliente(cliente2)
banco.inserirConta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print('#' * 30)

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')