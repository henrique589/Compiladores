from Lexema import Lexema
from Token import Token
from pathlib import Path

TESTE_FILE = Path(__file__).parent / 'testes/calculadora.p'

lexema = []
tokens = []
num_linha = 1
estado = 0

with open(TESTE_FILE, 'r') as arquivo:
    for line in arquivo:
        buffer = line.rstrip('\n')
        for c in buffer:
            if c == ' ':
                print(lexema)
                lexema = []
            # Lógica do automato
            lexema.append(c)

# if estado == 0:
#     pass


        # estado = 0
        # if estado == 0:
        #     if c == '(':
        #         token = Token(c, "LBRACKET", numLinha)