import glob
import re

padrao = re.compile(r'^(\d{4}-\d{2}-\d{2}) .* (remove|purge) (\S+)')

for arquivo in glob.glob('/var/log/dpkg.log*'):
    try:
        with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
            for linha in f:
                busca = padrao.search(linha)
                if busca:
                    print(f'{busca.group(3)} {busca.group(1)}')
    except FileNotFoundError:
        pass
