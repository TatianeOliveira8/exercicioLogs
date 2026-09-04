import glob
import re
from datetime import datetime, timedelta

limite = datetime.now() - timedelta(days=7)
padrao = re.compile(r'^(\d{4}-\d{2}-\d{2}) .* install (\S+)')

for arquivo in glob.glob('/var/log/dpkg.log*'):
    try:
        with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
            for linha in f:
                busca = padrao.search(linha)
                if busca:
                    data = datetime.strptime(busca.group(1), '%Y-%m-%d')
                    if data >= limite:
                        print(f'{busca.group(2)} {busca.group(1)}')
    except FileNotFoundError:
        pass
