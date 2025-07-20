def calcular_desconto(valor_original: float, percentual_desconto: float) -> float:
    """
    Calcula o valor do desconto baseado em uma porcentagem.
    """
    return valor_original * (percentual_desconto / 100)

def calcular_preco_final(valor_original: float, percentual_desconto: float) -> float:
    """
    Calcula o preço final após aplicar o desconto.
    """
    desconto = calcular_desconto(valor_original, percentual_desconto)
    preco_final = valor_original - desconto
    return round(preco_final, 2)

def main():
    print("Calculadora de Preço com Desconto\n")
    try:
        valor = float(input("Digite o valor original do produto: R$ ").replace(",", "."))
        desconto = float(input("Digite o percentual de desconto (%): ").replace(",", "."))
        if valor < 0 or desconto < 0:
            print("Por favor, insira valores positivos.")
            return
    except ValueError:
        print("Entrada inválida! Digite números válidos.")
        return

    preco_final = calcular_preco_final(valor, desconto)
    print(f"\nPreço final após {desconto:.2f}% de desconto: R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()
