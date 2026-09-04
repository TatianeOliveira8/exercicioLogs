import sys
import re

arquivo = sys.argv[1]
padrao1 = re.compile(r'Failed password for (?:invalid user )?(\S+) from .*?sshd')
padrao2 = re.compile(r'authentication failure; .*?user=(\S+)')

with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
    for linha in f:
        busca = padrao1.search(linha)
        if busca:
            print(f'ssh {busca.group(1)}')
            continue
        busca = padrao2.search(linha)
        if busca:
            metodo = 'su'
            if 'gdm' in linha:
                metodo = 'login'
            print(f'{metodo} {busca.group(1)}')
