# ------------------------------------------------------------
# Analizador lexico
# ------------------------------------------------------------
import ply.lex as lex
tokens = ('NUMBER','ELEMENTO','ELEMENTOMINUS', 'IGUAL', 'SIFRAO', 'HASHTAG', 'SIMBOLOS', 'CEELE')

# Tokens
t_CEELE = r'(\b(Li)|(Na)|(Rb)|(Cs)|(Fr)|(Be)|(Mg)|(Ca)|(Sr)' \
          r'|(Ba)|(Ka)|(Al)|(Ga)|(In)|(Ti)|(Si)|(Ge)|(Sn)|(Pb)' \
          r'|(As)|(Sb)|(Bi)|(Se)|(Te)|(Po)|(Cl)|(Br)|(At)\b)'
t_NUMBER = r'\d'
t_SIMBOLOS = r'[/ \( \) \[ \] \\ @ \+ \-]+'
t_IGUAL = r'\='
t_SIFRAO =  r'\$'
t_HASHTAG = r'\#'

# A string containing ignored characters
t_ignore = '\t\n:'

def t_ELEMENTOMINUS(t):
    r'[abcdefghijklmnopqrstuvwxyz]+'
    try:
        t.value = t.value
    except ValueError:
        # print "nao foi %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t
# A regular expression rule with some action code
def t_ELEMENTO(t):
    r'[CONSFHBK]'
    try:
         t.value = t.value
    except ValueError:
         #print "nao foi %d: Number %s is too large!" % (t.lineno,t.value)
         t.value = 0
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)
# Error handling rule
def t_error(t):
    #print "Illegal character '%s'" % t.value[0]
    t.skip(1)
# Build the lexer
lex.lex(debug=1)

