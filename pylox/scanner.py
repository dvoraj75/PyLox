from typing import List

from token_ import Token, TokenTypes, SINGLE_TOKENS, ONE_TWO_TOKENS, KEYWORDS


class Scanner:
    def __init__(self, source: str):
        self.__source: str = source
        self.line: int = 1
        self.current: int = 0

    def scan_tokens(self) -> List[Token]:
        tokens = []

        while not self.is_at_end():
            c = self.__source[self.current]
            if token_type := SINGLE_TOKENS.get(c):
                # {,},(,),,,.,-,+,;,*
                tokens.append(Token(token_type, c, None, self.line))
            elif token_type := ONE_TWO_TOKENS.get(c):
                # >,>=,<,<=, !, !=, ==, /, //
                self.current += 1
                if c == "/":
                    if self.match("/"):
                        while not self.match('\n') and not self.is_at_end():
                            self.current += 1
                    else:
                        tokens.append(Token(token_type, c, None, self.line))
                    continue
                elif self.match("="):
                    c += "="
                    token_type = ONE_TWO_TOKENS.get(c)
                tokens.append(Token(token_type, c, None, self.line))  # TODO: opakujici se lajna, bude tu jeste vickrat
            elif c.isspace():
                # ignore whitespaces
                if c == '\n':
                    self.line += 1
            elif self.match("\""):
                # string
                token_type = TokenTypes.STRING
                start = self.current
                self.current += 1
                while not self.match("\""):
                    if self.is_at_end():
                        raise SyntaxError("Unterminated string!!!")  # TODO: vlastni chyby -> LoxSyntaxError?
                    if self.match("\n"):
                        self.line += 1
                    self.current += 1
                c = self.__source[start:self.current+1]
                literal = self.__source[start+1:self.current]
                tokens.append(Token(token_type, c, literal, self.line))
            else:
                if c.isdigit():
                    # number
                    start = self.current
                    self.current += 1
                    c = self.__source[self.current]
                    while c.isdigit():
                        self.current += 1
                        c = self.__source[self.current]
                    if self.match("."):
                        self.current += 1
                        c = self.__source[self.current]
                    while c.isdigit():
                        self.current += 1
                        c = self.__source[self.current]
                    token_type = TokenTypes.NUMBER
                    c = self.__source[start:self.current]
                    tokens.append(Token(token_type, c, float(c), self.line))
                elif c.isalpha() or self.match("_"):
                    # identifier or keyword
                    start = self.current
                    self.current += 1
                    c = self.__source[self.current]
                    while c.isalnum() or self.match("_"):
                        self.current += 1
                        c = self.__source[self.current]
                    c = self.__source[start:self.current]
                    token_type = KEYWORDS.get(c, TokenTypes.IDENTIFIER)
                    tokens.append(Token(token_type, c, c, self.line))
                else:
                    raise SyntaxError(f"Unexpected character: {c}")
                continue
            self.current += 1
        return tokens

    def is_at_end(self) -> bool:
        return self.current >= len(self.__source)

    def match(self, c: str) -> bool:
        if self.is_at_end():
            return False
        return self.__source[self.current] == c
