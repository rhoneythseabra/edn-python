def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def calculadora():
    print("Calculadora Simples em Python")
    print("Operações disponíveis:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    operacao = input("Escolha a operação (+, -, *, /): ")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada inválida! Use apenas números.")
        return

    if operacao == "+":
        print("Resultado:", soma(num1, num2))
    elif operacao == "-":
        print("Resultado:", subtracao(num1, num2))
    elif operacao == "*":
        print("Resultado:", multiplicacao(num1, num2))
    elif operacao == "/":
        print("Resultado:", divisao(num1, num2))
    else:
        print("Operação inválida!")

calculadora()
