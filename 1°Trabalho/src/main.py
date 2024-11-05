from Lexema import Lexema
from Token import Token
from pathlib import Path

TESTE_FILE = Path(__file__).parent / 'testes/calculadora.p'

tokens = []

with open(TESTE_FILE, 'r') as arquivo:
    for line in arquivo:
        buffer = line.rstrip('\n')
        for c in buffer:
            if c == ' ':
                ...

## IMPLEMENTAR CONTADOR PARA INICIAR OS LEXEMAS
## IMPLEMENTAR LÓGICA DO AUTÔMATO