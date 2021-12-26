from dataclasses import dataclass
from enum import Enum


class TokenTypes(Enum):
    # single-character tokens
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    LEFT_BRACE = "LEFT_BRACE"
    RIGHT_BRACE = "RIGHT_BRACE"
    COMMA = "COMMA"
    DOT = "DOT"
    MINUS = "MINUS"
    PLUS = "PLUS"
    SEMICOLON = "SEMICOLON"
    SLASH = "SLASH"
    STAR = "STAR"

    # One or two character tokens
    BANG = "BANG"
    BANG_EQUAL = "BANG_EQUAL"
    EQUAL = "EQUAL"
    EQUAL_EQUAL = "EQUAL_EQUAL"
    GREATER = "GREATER"
    GREATER_EQUAL = "GREATER_EQUAL"
    LESS = "LESS"
    LESS_EQUAL = "LESS_EQUAL"

    # literals
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"

    # keywords
    AND = "AND"
    CLASS = "CLASS"
    ELSE = "ELSE"
    FALSE = "FALSE"
    FUN = "FUN"
    FOR = "FOR"
    IF = "IF"
    NIL = "NIL"
    OR = "OR"
    PRINT = "PRINT"
    RETURN = "RETURN"
    SUPER = "SUPER"
    THIS = "THIS"
    TRUE = "TRUE"
    VAR = "VAR"
    WHILE = "WHILE"

    EOF = "EOF"


SINGLE_TOKENS = {
    "{": TokenTypes.LEFT_PAREN,
    "}": TokenTypes.RIGHT_PAREN,
    "(": TokenTypes.LEFT_BRACE,
    ")": TokenTypes.RIGHT_BRACE,
    ",": TokenTypes.COMMA,
    ".": TokenTypes.DOT,
    "-": TokenTypes.MINUS,
    "+": TokenTypes.PLUS,
    ";": TokenTypes.SEMICOLON,
    "*": TokenTypes.STAR,
}

ONE_TWO_TOKENS = {

    "!": TokenTypes.BANG,
    "!=": TokenTypes.BANG_EQUAL,
    "=": TokenTypes.EQUAL,
    "==": TokenTypes.EQUAL_EQUAL,
    ">": TokenTypes.GREATER,
    ">=": TokenTypes.GREATER_EQUAL,
    "<": TokenTypes.LESS,
    "<=": TokenTypes.LESS_EQUAL,
    "/": TokenTypes.SLASH,
}

KEYWORDS = {
    "and": TokenTypes.AND,
    "class": TokenTypes.CLASS,
    "else": TokenTypes.ELSE,
    "false": TokenTypes.FALSE,
    "fun": TokenTypes.FUN,
    "for": TokenTypes.FOR,
    "if": TokenTypes.IF,
    "nil": TokenTypes.NIL,
    "or": TokenTypes.OR,
    "print": TokenTypes.PRINT,
    "return": TokenTypes.RETURN,
    "super": TokenTypes.SUPER,
    "this": TokenTypes.THIS,
    "true": TokenTypes.TRUE,
    "var": TokenTypes.VAR,
    "while": TokenTypes.WHILE,
    "eof": TokenTypes.EOF
}


@dataclass
class Token:
    type: TokenTypes
    lexeme: str
    literal: object
    line: int

    def __str__(self):
        return f"{self.type} {self.lexeme} {self.literal}"
