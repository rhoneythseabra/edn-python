print('Calculadora de preço total')

nomeProduto = input("Digite o nome do produto: ")
precoProduto = float(input("Digite o preço do produto: "))
quantidadeComprada = int(input("Digite a quantidade comprada: "))

valorTotalDaCompra = precoProduto * quantidadeComprada

print(f'O produto comprado foi {nomeProduto}, foram {quantidadeComprada} unidades que custam R${precoProduto:.2f} cada.')
print(f'O valor total a ser pago é de: R${valorTotalDaCompra:.2f}')