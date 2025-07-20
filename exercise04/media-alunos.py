def coletar_notas():
    """
    Solicita ao usuário o número de alunos e depois, para cada um,
    o nome e a nota.  Devolve uma lista de dicionários no formato
    [{'nome': 'Ana', 'nota': 8.5}, ...].
    """
    while True:
        try:
            quantidade = int(input("Quantos alunos deseja cadastrar? "))
            if quantidade <= 0:
                print("Digite um número inteiro positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    alunos = []
    for i in range(1, quantidade + 1):
        nome = input(f"\nAluno {i} – nome: ").strip()
        while True:
            try:
                nota = float(input(f"Aluno {i} – nota: ").replace(",", "."))
                if nota < 0 or nota > 10:
                    print("A nota deve estar entre 0 e 10.")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite a nota usando números (ex.: 7.5).")
        alunos.append({"nome": nome, "nota": nota})
    return alunos


def calcular_media(alunos):
    """Recebe a lista de alunos e devolve a média da turma."""
    if not alunos:  # Evita divisão por zero, caso a lista esteja vazia
        return 0
    soma = sum(aluno["nota"] for aluno in alunos)
    return soma / len(alunos)


def main():
    print("=== Cadastro de Notas ===")
    alunos = coletar_notas()

    # Mostra cada aluno com sua nota
    print("\n--- Notas Cadastradas ---")
    for aluno in alunos:
        print(f"{aluno['nome']}: {aluno['nota']:.2f}")

    # Calcula e exibe a média
    media_turma = calcular_media(alunos)
    print(f"\nMédia da turma: {media_turma:.2f}")

    # Optei por colocar quem ficou acima ou abaixo da média
    print("\n--- Desempenho Relativo ---")
    for aluno in alunos:
        status = "acima" if aluno["nota"] >= media_turma else "abaixo"
        print(f"{aluno['nome']} ficou {status} da média.")


if __name__ == "__main__":
    main()
