# Variáveis Globais
nome = ''
preco = 0.0
desconto = 0.0
preco_final = 0.0
produtos = []

def CalcularValorFinal(valor_base = 0.0, taxa_desconto = 0.0):
    '''
    Aplica o desconto ao valor base

    Args:
        valor_base (float): valor original do produto
        taxa_desconto (float): taxa de desconto a ser aplicado
    
    Returns:
        float: valor base com desconto
    '''
    valor_com_desconto = valor_base - (valor_base * (taxa_desconto / 100))
    return valor_com_desconto

def ExibirRecibo(nome_produto = '', valor_pago = 0.0):
    print(f'{nome_produto} - {valor_pago:.2f}')

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    desconto = float(input('Digite a taxa de desconto: '))

    preco_final = CalcularValorFinal(preco, desconto)

    produto = [nome, preco, desconto, preco_final]
    produtos.append(produto)

    opcao = input('Deseja incluir um novo produto? s/n: ')

    if opcao.lower() != 's':
        for produto in produtos:
            ExibirRecibo(produto[0], produto[3])
        break
