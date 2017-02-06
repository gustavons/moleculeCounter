# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
# 'CE', 'O','ENE', 'ESE', 'EFE', 'AGAR', 'BE', 'UM', 'DOIS', 'TRES',
#     , 'ARROBA', 'BARRA', 'CONTRABARRA','NAME', 'LPAREN',
#     'RPAREN',


# dic_elementos = {}
tokens = (
      'ELEMENTO', 'IGUAL', 'SIFRAO', 'HASHTAG',
)

# Tokens

# t_CE = r'\C'
# t_O = r'\O'
# t_ENE = r'\N'
# t_ESE = r'S'
# t_EFE = r'\F'
# t_AGAR = r'\H'
# t_BE = r'\B'
# t_UM = r'\\1'
# t_DOIS = r'\\2'
# t_TRES = r'\\3'
t_IGUAL = r'\='
t_SIFRAO =  r'\$'
t_HASHTAG = r'\#'
# t_VAZIO = r''
# t_ARROBA = r'\@'
# t_BARRA = r'/'
# t_CONTRABARRA = r'\\'
# t_ = r'\+'
# t_ = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_EQUALS = r'='
# t_LPAREN = r'\('
# t_RPAREN = r'\)'


# A regular expression rule with some action code
# def t_NUMBER(t):
#     r'\d+'
#     try:
#          t.value =
#     except ValueError:
#          print "Line %d: Number %s is too large!" % (t.lineno,t.value)
# 	 t.value = 0
#     return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = '/\()[]1234567890\t'
# A regular expression rule with some action code
def t_ELEMENTO(t):
    r'[CONSFHB]+'
    try:
         t.value = t.value
         print t.value

         # if (t.value == 'C'):
         #    try:
         #        dic_elementos[t.value] = dic_elementos[t.value]+ 4
         #    except:
         #        dic_elementos[t.value] =  4
         # if (t.value == 'O'):
         #       dic_elementos[t.value] = 2
         # if (t.value == 'N'):
         #       dic_elementos[t.value] = 3
         # if (t.value == 'S'):
         #       dic_elementos[t.value] = 2
         # if (t.value == 'F'):
         #       dic_elementos[t.value] = 1
         # if (t.value == 'H'):
         #       dic_elementos[t.value] = 1
         # if (t.value == 'B'):
         #       dic_elementos[t.value] = 4

    except ValueError:
         print "nao foi %d: Number %s is too large!" % (t.lineno,t.value)
	 t.value = 0
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.skip(1)

# Build the lexer
lex.lex(debug=1)

# Test it out
# data = '''C1CCC1
# '''
#
# # Give the lexer some input
# lex.input(data)

#
# # Tokenize
# while 1:
#     tok = lex.token()
#     if not tok: break      # No more input
#     print tok
#
# print dic_elementos