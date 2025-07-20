def verificar_senha(senha):
    if len(senha) < 8:
        return False, "❌ A senha deve ter pelo menos 8 caracteres."
    
    if not any(char.isdigit() for char in senha):
        return False, "❌ A senha deve conter pelo menos um número."

    return True, "✅ Senha válida!"

def main():
    print("🔐 Verificador de Senha Segura\n")
    senha = input("Digite sua senha: ")
    
    eh_valida, mensagem = verificar_senha(senha)
    print("\nResultado:")
    print(mensagem)

if __name__ == "__main__":
    main()
