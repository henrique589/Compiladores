from AutomatoLexico import AutomatoLexico
from pathlib import Path

TESTE_FILE = Path(__file__).parent / 'testes/t.p'

automatoLexico = AutomatoLexico()

# Lê o arquivo e processa caractere por caractere
with open(TESTE_FILE, 'r') as arquivo:
    for line in arquivo:
        for caractere in line:
            automatoLexico.processar_caractere(caractere)

# Finaliza qualquer token remanescente após a última linha do arquivo
automatoLexico.processar_caractere(' ')  # Gatilho para transições de estado pendentes

# Exibe os tokens processados
for token in automatoLexico.tokens:
    print(token)
