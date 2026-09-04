import subprocess
import re
from datetime import datetime

saida = subprocess.check_output(['last', '-x', '-F'], text=True, errors='ignore')
boot = None

for linha in saida.splitlines():
    if boot is None and 'system boot' in linha:
        busca = re.search(r'([A-Z][a-z]{2}\s+[A-Z][a-z]{2}\s+\d+\s+\d+:\d+:\d+\s+\d{4})', linha)
        if busca:
            boot = datetime.strptime(busca.group(1), '%a %b %d %H:%M:%S %Y')

if boot:
    print(datetime.now() - boot)
