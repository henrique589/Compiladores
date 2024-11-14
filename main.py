class Lexema:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Token:
    def __init__(self, tipoToken, lexema, numLinha):
        self.lexema = lexema
        self.tipoToken = tipoToken
        self.numLinha = numLinha
    
    @staticmethod
    def palavras_reservadas():
        ReserveWords = {
            "fn": "FUNCTION",
            "main": "MAIN",
            "let": "LET",
            "int": "INT",
            "float": "FLOAT",
            "char": "CHAR",
            "if": "IF",
            "else": "ELSE",
            "while": "WHILE",
            "println": "PRINTLN",
            "return": "RETURN"
        }
        return ReserveWords

    @staticmethod
    def simbolos_especiais():
        symbols = {
            "(": "LBRACKET",
            ")": "RBRACKET",
            "{": "LBRACE",
            "}": "RBRACE",
            ":": "COLLON",
            ",": "COMMA",
            ";": "PCOMMA",
            "+": "PLUS",
            "*": "MULT",
            "/": "DIV"
        }
        return symbols
    
    def __repr__(self):
        return f"Token(tipo={self.tipoToken}, lexema={self.lexema.start}, {self.lexema.end} linha={self.numLinha})"

class AutomatoLexico:
    def __init__(self):
        self.estado = 0
        self.lexema = []
        self.tokens = []
        self.linha_atual = 1
        self.posicao_atual = 1
        self.inicio_lexema = 1
        self.reserveWords = Token.palavras_reservadas()
        self.symbols = Token.simbolos_especiais()

    def cria_token(self, tipoToken, inicio, fim):
        lexema = Lexema(inicio, fim)
        token = Token(tipoToken, lexema, self.linha_atual)
        self.tokens.append(token)
        self.estado = 0
        self.lexema = []

    def processar_caractere(self, caractere: str):
        if self.estado == 0:
            if caractere in self.symbols:
                self.inicio_lexema = self.posicao_atual
                tipoToken = self.symbols[caractere]
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            elif caractere == '=':
                self.inicio_lexema = self.posicao_atual
                self.estado = 1
                self.lexema.append(caractere)
            elif caractere == '!':
                self.inicio_lexema = self.posicao_atual
                self.estado = 2
                self.lexema.append(caractere)
            elif caractere == '>':
                self.inicio_lexema = self.posicao_atual
                self.estado = 3
                self.lexema.append(caractere)
            elif caractere == '<':
                self.inicio_lexema = self.posicao_atual
                self.estado = 4
                self.lexema.append(caractere)
            elif caractere == '-':
                self.inicio_lexema = self.posicao_atual
                self.estado = 5
                self.lexema.append(caractere)
            elif caractere.isnumeric():
                self.inicio_lexema = self.posicao_atual
                self.estado = 6
                self.lexema.append(caractere)
            elif caractere == ' ':
                ...
            elif caractere == '\n':
                self.linha_atual += 1
                self.posicao_atual = 0
        elif self.estado == 1:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'EQ'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            else:
                tipoToken = 'ASSIGN'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual-1)
                self.processar_caractere(caractere)  # Reprocessa o caractere atual
        elif self.estado == 2:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'NE'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            else:
                tipoToken = 'ERROR'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
                self.processar_caractere(caractere)  # Reprocessa o caractere atual
        elif self.estado == 3:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'GE'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            else:
                tipoToken = 'GT'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
                self.processar_caractere(caractere)
        elif self.estado == 4:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'LE'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            else:
                tipoToken = 'LT'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
                self.processar_caractere(caractere)
        elif self.estado == 5:
            if caractere == '>':
                self.lexema.append(caractere)
                tipoToken = 'ARROW'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            else:
                tipoToken = 'MINUS'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
                self.processar_caractere(caractere)
        elif self.estado == 6:
            if caractere.isnumeric():
                self.lexema.append(caractere)
            elif caractere == '.':
                self.lexema.append(caractere)
                self.estado = 7
            else:
                tipoToken = 'INT_CONST'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual - 1)
                self.processar_caractere(caractere)
        elif self.estado == 7:
            if caractere.isnumeric():
                self.lexema.append(caractere)
                self.estado = 8
            else:
                tipoToken = 'ERROR'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
                self.processar_caractere(caractere)
        elif self.estado == 8:
            if caractere.isnumeric():
                self.lexema.append(caractere)
            else:
                tipoToken = 'FLOAT_CONST'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual - 1)
                self.processar_caractere(caractere)
        self.posicao_atual += 1

from pathlib import Path

TESTE_FILE = Path(__file__).parent / 't.p'

automatoLexico = AutomatoLexico()

with open(TESTE_FILE, 'r') as arquivo:
    for line in arquivo:
        for caractere in line:
            automatoLexico.processar_caractere(caractere)

for token in automatoLexico.tokens:
    print(token)