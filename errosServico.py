import sys
import re

servico = sys.argv[1]
arquivo = '/var/log/syslog'

padrao = re.compile(rf'.*{re.escape(servico)}.*(error|warning)', re.IGNORECASE)

with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
    for linha in f:
        if padrao.search(linha):
            print(linha.strip())
