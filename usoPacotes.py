import sys
import re

arquivo = '/var/log/auth.log'
if len(sys.argv) == 2:
    arquivo = sys.argv[1]

padrao = re.compile(r'^(\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}) .*?COMMAND=.*?/(apt|apt-get|dpkg)\b.*$')

with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
    for linha in f:
        if 'COMMAND=' in linha and ('apt' in linha or 'apt-get' in linha or 'dpkg' in linha):
            usuario = re.search(r' (\S+): Executing command', linha)
            comando = re.search(r'COMMAND=(.+)$', linha)
            if usuario and comando:
                print(f'{usuario.group(1)} {comando.group(1)}')
