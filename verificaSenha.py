import sys
import re
from collections import defaultdict

if len(sys.argv) != 2:
    print('Uso: python3 verificaSenha.py <arquivo_log>')
    sys.exit(1)

caminho_arquivo = sys.argv[1]
contador_por_usuario = defaultdict(int)

padrao = re.compile(
    r'Failed password for (?:invalid user )?(\S+) from|authentication failure;.*?user=(\S+)'
)

with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo:
    for linha in arquivo:
        resultado = padrao.search(linha)
        if resultado:
            usuario = resultado.group(1) or resultado.group(2)
            contador_por_usuario[usuario] += 1

for usuario, quantidade in sorted(contador_por_usuario.items()):
    print(f'{usuario}: {quantidade}')