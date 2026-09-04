import sys
import re
from collections import Counter

arquivo = '/var/log/syslog'
if len(sys.argv) == 2:
    arquivo = sys.argv[1]

contagem = Counter()
padrao = re.compile(r'^\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\S+\s+([\w.-]+)')

with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
    for linha in f:
        busca = padrao.search(linha)
        if busca:
            contagem[busca.group(1)] += 1

for servico, total in contagem.most_common():
    print(f'{servico}: {total}')
