import sys
import re

arquivo = '/var/log/syslog'
if len(sys.argv) == 2:
    arquivo = sys.argv[1]

padrao = re.compile(r'^(\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}) .*? (Started|Stopped|Starting|Stopping) (.+)$')

with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
    for linha in f:
        busca = padrao.search(linha)
        if busca:
            print(f'{busca.group(1)} {busca.group(3)}')
