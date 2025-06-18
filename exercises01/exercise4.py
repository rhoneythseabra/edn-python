print('Calculadora de preço total')

nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade_comprada = int(input("Digite a quantidade comprada: "))

valor_total_da_compra = preco_produto * quantidade_comprada

print(f'O produto comprado foi {nome_produto}, foram {quantidade_comprada} unidades que custam R${preco_produto:.2f} cada.')
print(f'O valor total a ser pago é de: R${valor_total_da_compra:.2f}')