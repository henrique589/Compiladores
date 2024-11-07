from Token import Token
from Lexema import Lexema

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

    def processar_caractere(self, caractere:str):
        if self.estado == 0:
            if caractere in self.symbols:
                self.inicio_lexema = self.posicao_atual
                tipoToken = self.symbols[caractere]
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            elif caractere == '=':
                self.lexema.append(caractere)
                self.inicio_lexema = self.posicao_atual
                self.estado = 1
            elif caractere == '!':
                self.lexema.append(caractere)
                self.inicio_lexema = self.posicao_atual
                self.estado = 2
            elif caractere == '>':
                self.lexema.append(caractere)
                self.inicio_lexema = self.posicao_atual
                self.estado = 3
            elif caractere == ' ':
                self.lexema = []
                pass
            elif caractere == '\n':
                self.linha_atual += 1
                self.posicao_atual = 0
        elif self.estado == 1:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'EQ'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual) 
            elif caractere is not '=':
                self.lexema.append(caractere)
                tipoToken = 'ASSIGN'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
        elif self.estado == 2:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'NE'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
        elif self.estado == 3:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'GE'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            elif caractere is not '=':
                self.lexema.append(caractere)
                tipoToken = 'GT'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
        self.posicao_atual += 1
                