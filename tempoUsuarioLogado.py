import sys
import subprocess
import re
from datetime import datetime

usuario = sys.argv[1]
saida = subprocess.check_output(['last', '-F', usuario], text=True, errors='ignore')
formato = '%a %b %d %H:%M:%S %Y'
total = 0

for linha in saida.splitlines():
    busca = re.search(r'(\w{3}\s+\w{3}\s+\d+\s+\d+:\d+:\d+\s+\d{4}).*-(\s)(\w{3}\s+\w{3}\s+\d+\s+\d+:\d+:\d+\s+\d{4})', linha)
    if busca:
        inicio = datetime.strptime(busca.group(1), formato)
        fim = datetime.strptime(busca.group(3), formato)
        total += int((fim - inicio).total_seconds())

print(total)
