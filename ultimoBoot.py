import subprocess
import re

saida = subprocess.check_output(['last', '-x', '-F'], text=True, errors='ignore')

for linha in saida.splitlines():
    if 'system boot' in linha:
        busca = re.search(r'([A-Z][a-z]{2}\s+[A-Z][a-z]{2}\s+\d+\s+\d+:\d+:\d+\s+\d{4})', linha)
        if busca:
            print(busca.group(1))
            break
