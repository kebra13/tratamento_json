import json
import statistics

def ler_arquivo():
    # Lê o arquivo json com todos os dados
    with open('dados.json', 'r') as f:
        dados = json.load(f)
    return dados

# Armazena essa função em uma variável
arquivo = ler_arquivo()

valores = []

for i in arquivo:
    # Adiciono o faturamento do meu arquivo json na minha lista
    valores.append(i['valor'])

def remover_zeros():
    # Adiciono apenas os faturamentos diferentes de 0 na minha lista
    valores_s_zeros = []
    for i in valores:
        if i != 0:
            valores_s_zeros.append(i)
    return valores_s_zeros

# Armazena essa função em uma variável
result = remover_zeros()

def calcular_dias_fat_acima_media():
    # Calcula em quantos dias do mês o faturamento foi maior do que a média
    dias_acima_da_media = 0
    for i in result:
        if i > statistics.mean(result):
            dias_acima_da_media += 1
    return dias_acima_da_media

# Armazena essa função em uma variável
dias_acima_da_media = calcular_dias_fat_acima_media()

print(f'Mínimo faturado em um dia: R${min(result):.2f}')
print(f'Máximo faturado em um dia: R${max(result):,.2f}')
print(f'Dias com faturamento maior que a média: {dias_acima_da_media}')
print(f'Média de faturamento: R${statistics.mean(result):,.2f}') 
# print so de teste
