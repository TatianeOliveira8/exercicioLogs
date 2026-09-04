import sys

arquivo = sys.argv[1]
data = sys.argv[2]

with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
    for linha in f:
        if not linha.startswith(data):
            continue

        partes = linha.split()
        if len(partes) < 3:
            continue

        horario = partes[2]
        if horario.startswith('14:'):
            print(linha.strip())
