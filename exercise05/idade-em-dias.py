from datetime import datetime

def idade_em_dias(ano, mes, dia):

    hoje = datetime.now()
    nascimento = datetime(ano, mes, dia)
    diferenca = hoje - nascimento
    return diferenca.days

dias_de_vida = idade_em_dias(1987, 9, 2)
print(f"Essa pessoa tem aproximadamente {dias_de_vida} dias de vida.")