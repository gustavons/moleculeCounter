# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'CE', 'O','ENE', 'ESE', 'EFE', 'AGAR', 'BE', 'UM', 'DOIS', 'TRES',
    'IGUAL', 'ARROBA', 'BARRA', 'CONTRABARRA','NAME', 'LPAREN',
    'RPAREN',
)

# Tokens

t_CE = r'\C'
t_O = r'\O'
t_ENE = r'\N'
t_ESE = r'S'
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

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    try:
         t.value = int(t.value)
    except ValueError:
         print "Line %d: Number %s is too large!" % (t.lineno,t.value)
	 t.value = 0
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.skip(1)

# Build the lexer
lex.lex(debug=1)

# Test it out
data = '''CC\C=C/C\C=C/C\C=C/CCCCCCCC(O)=O
'''

# Give the lexer some input
lex.input(data)

# Tokenize
while 1:
    tok = lex.token()
    if not tok: break      # No more input
    print tok