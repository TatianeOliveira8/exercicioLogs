import sys
import re

arquivo = sys.argv[1]

padrao = re.compile(r'^(\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}) .*?session opened for user (\S+)')

with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
    for linha in f:
        busca = padrao.search(linha)
        if busca:
            data_hora = busca.group(1)
            usuario = busca.group(2)
            print(f'{usuario} {data_hora}')
