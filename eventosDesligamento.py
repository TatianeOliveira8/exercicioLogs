import subprocess

saida = subprocess.check_output(['last', '-x', '-F'], text=True, errors='ignore')

for linha in saida.splitlines():
    if 'shutdown' in linha or 'reboot' in linha:
        print(linha)
