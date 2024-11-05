class Token:
    def __init__(self, lexema, numLinha):
        self.lexema = lexema
        self.tipoToken = None
        self.numLinha = numLinha
    
    def classificacao_token(self):
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
            "return": "RETURN",
            "(": "LBRACKET",
            ")": "RBRACKET",
            "{": "LBRACE",
            "}": "RBRACE",
        }

        return ReserveWords

        # if self.lexema in ReserveWords:
        #     self.tipoToken = ReserveWords[self.lexema]
