def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor = 50
porcentagem = 15
gorgeta = calcular_gorjeta(valor, porcentagem)

print(f"O valor da gorgeta é:R${gorgeta: .2f}")