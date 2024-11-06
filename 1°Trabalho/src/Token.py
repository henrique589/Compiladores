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