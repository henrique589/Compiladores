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

    def processar_caractere(self, caractere: str):
        reprocessar = False
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
            elif caractere.isalpha():
                self.inicio_lexema = self.posicao_atual
                self.estado = 9
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
                reprocessar = True
        elif self.estado == 2:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'NE'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            else:
                tipoToken = 'ERROR'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
                reprocessar = True
        elif self.estado == 3:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'GE'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            else:
                tipoToken = 'GT'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual - 1)
                reprocessar = True
        elif self.estado == 4:
            if caractere == '=':
                self.lexema.append(caractere)
                tipoToken = 'LE'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            else:
                tipoToken = 'LT'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual - 1)
                reprocessar = True
        elif self.estado == 5:
            if caractere == '>':
                self.lexema.append(caractere)
                tipoToken = 'ARROW'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
            else:
                tipoToken = 'MINUS'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
                reprocessar = True
        elif self.estado == 6:
            if caractere.isnumeric():
                self.lexema.append(caractere)
            elif caractere == '.':
                self.lexema.append(caractere)
                self.estado = 7
            else:
                tipoToken = 'INT_CONST'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual - 1)
                reprocessar = True
        elif self.estado == 7:
            if caractere.isnumeric():
                self.lexema.append(caractere)
                self.estado = 8
            else:
                tipoToken = 'ERROR'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual)
                reprocessar = True
        elif self.estado == 8:
            if caractere.isnumeric():
                self.lexema.append(caractere)
            else:
                tipoToken = 'FLOAT_CONST'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual - 1)
                reprocessar = True
        elif self.estado == 9:
            if caractere.isalpha() or caractere.isnumeric() or caractere == '_':
                self.lexema.append(caractere)
            else:
                # Converte `self.lexema` para uma string unida e exibe para depuração
                lexema_str = ''.join(self.lexema) 
                if lexema_str in self.reserveWords:
                    tipoToken = self.reserveWords[lexema_str]
                else:
                    tipoToken = 'ID'
                self.cria_token(tipoToken, self.inicio_lexema, self.posicao_atual - 1)
                reprocessar = True

        if not reprocessar:
            self.posicao_atual += 1
        else:
            self.processar_caractere(caractere)
