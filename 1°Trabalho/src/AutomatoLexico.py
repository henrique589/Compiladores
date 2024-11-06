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

    def processar_caractere(self, caractere:str):
        if self.estado == 0:
            if caractere in self.symbols:
                self.inicio_lexema = self.posicao_atual
                tipoToken = self.symbols[caractere]
                lexema = Lexema(self.inicio_lexema, self.posicao_atual)
                token = Token(tipoToken, lexema, self.linha_atual)
                self.tokens.append(token)
            elif caractere == ' ':
                pass
            elif caractere == '\n':
                self.linha_atual += 1
                self.posicao_atual = 0
        self.posicao_atual += 1
                