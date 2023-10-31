# Testar o sistema contábil
from contas import Contas

# Criação e instância de objetos
receita1 = Contas(1, 'Recebimento de Cliente', 'Receita', '004-01')
receita2 = Contas(2, 'Receita com Juros', 'Receita', '004-02')
despesa1 = Contas(3, 'Pagamento de Fornecedores', 'Despesa', '003-01')
despesa2 = Contas(4, 'Despesa com Salário', 'Despesa', '003-2')

print('\n\t\t\t -- Lista do Plano de Contas de Resultado -- \n')

print(receita1)
print(receita2)
print(despesa1)
print(despesa2)

receita1.setCodigoConta(21)

print(receita1)
