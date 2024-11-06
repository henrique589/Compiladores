from AutomatoLexico import AutomatoLexico
from pathlib import Path

TESTE_FILE = Path(__file__).parent / 'testes/t.p'

automatoLexico = AutomatoLexico()

with open(TESTE_FILE, 'r') as arquivo:
    for line in arquivo:
        for caractere in line:
            automatoLexico.processar_caractere(caractere)

for token in automatoLexico.tokens:
    print(token)