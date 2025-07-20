pares = 0
impares = 0

print("Digite números inteiros (digite 'sair' para encerrar):")

while True:
    entrada = input("> ")
    if entrada.lower() == "sair":
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        print("Digite um número inteiro válido ou 'sair' para encerrar.")

print("\nResultado:")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
