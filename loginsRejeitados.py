import sys
import re
from collections import defaultdict

arquivo = sys.argv[1]
contagem = defaultdict(int)

padrao = re.compile(
    r'Invalid user (\S+)|user unknown.*?user=(\S+)|authentication failure;.*?user=(\S+)|PAM: Permission denied.*?user=(\S+)'
)

with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
    for linha in f:
        if 'Failed password' in linha:
            continue
        busca = padrao.search(linha)
        if busca:
            usuario = next((g for g in busca.groups() if g), None)
            if usuario:
                contagem[usuario] += 1

for usuario, total in sorted(contagem.items()):
    print(f'{usuario}: {total}')
