from Token import Token

class AutomatoLexico:
    def __init__(self):
        self.estado = 0
        self.lexema = []
        self.linha_atual = 1
        self.reserveWords = Token.classificacao_token()

    def processar_caractere(self, caractere:str):
        if self.estado == 0:
            if caractere.isalpha():
                self.estado = 1
                self.lexema.append(caractere)
            elif caractere.isdigit():
                self.estado = 2
                self.lexema.append(caractere)
            elif caractere in self.reserveWords:
                ...