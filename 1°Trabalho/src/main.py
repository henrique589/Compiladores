from AutomatoLexico import AutomatoLexico
from pathlib import Path

TESTE_FILE = Path(__file__).parent / 'testes/calculadora.p'

automatoLexico = AutomatoLexico()

# Lê o arquivo e processa caractere por caractere
with open(TESTE_FILE, 'r') as arquivo:
    for line in arquivo:
        for caractere in line:
            automatoLexico.processar_caractere(caractere)

automatoLexico.finalizar_analise()
automatoLexico.cria_token_eof()

# Exibe os tokens processados
for token in automatoLexico.tokens:
    print(token)
