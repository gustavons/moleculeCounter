# -----------------------------------------------------------------------------
# calclex.py
# -----------------------------------------------------------------------------
import sys

if ".." not in sys.path: sys.path.insert(0, "..")
import ply.lex as lex

tokens = (
    'CE', 'O','ENE', 'ESE', 'EFE', 'AGAR', 'BE', 'UM', 'DOIS', 'TRES',
    'IGUAL', 'ARROBA', 'BARRA', 'CONTRABARRA','NAME', 'LPAREN',
    'RPAREN',
)

# Tokens

t_CE = r'\C'
t_O = r'\O'
t_ENE = r'\N'
t_ESE = r'\S'
t_EFE = r'\F'
t_AGAR = r'\H'
t_BE = r'\B'
t_UM = r'\\1'
t_DOIS = r'\\2'
t_TRES = r'\\3'
t_IGUAL = r'\='
t_ARROBA = r'\@'
t_BARRA = r'/'
t_CONTRABARRA = r'\\'
# t_ = r'\+'
# t_ = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'[a-z A-Z_][a-z A-Z 0-9_]*'


# def t_NUMBER(t):
#     r'\d+'
#     try:
#         t.value = int(t.value)
#     except ValueError:
#         print("Integer value too large %s" % t.value)
#         t.value = 0
#     return t


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex(debug=1)