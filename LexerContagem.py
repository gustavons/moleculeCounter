#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------
# Analizador lexico
# ------------------------------------------------------------
import ply.lex as lex

# class MyLexer(object):

tokens = ('NUMBER','VARIAVEL','ELEMENTO','ELEMENTOMINUS', 'IGUAL', 'SIFRAO', 'HASHTAG', 'LSIMBOLOS', 'RSIMBOLOS' )

# Tokens
# t_ELEMENTODUASLETRAS = r'(\b(Li)|(Na)|(Rb)|(Cs)|(Fr)|(Be)|(Mg)|(Ca)|(Sr)' \
#           r'|(Ba)|(Ka)|(Al)|(Ga)|(In)|(Ti)|(Si)|(Ge)|(Sn)|(Pb)' \
#           r'|(As)|(Sb)|(Bi)|(Se)|(Te)|(Po)|(Cl)|(Br)|(At)\b)'
t_NUMBER = r'\d'
t_LSIMBOLOS = r'[\(\[]{1}'
t_RSIMBOLOS = r'[\)\]]{1}'
t_IGUAL = r'\='
t_SIFRAO =  r'\$'
t_HASHTAG = r'\#'
t_VARIAVEL = r'P|S'

# A string containing ignored characters
t_ignore = '\n:+-.@\/hH'
t_ignore_COMMENT = r'\t.*'
# t_ignore_COMMENT = r'\t.*'

def t_ELEMENTOMINUS(t):
    r'[kbcnposfi]+'
    try:
        t.value = t.value
    except ValueError:
        # print "nao foi %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t


# A regular expression rule with some action code
def t_ELEMENTO(t):
    r'\bLi|Na|Rb|Cs|Fr|Be|Mg|Ca|Sr|Ba|Ka|Al|Ga|In|Ti|Si|Ge|Sn|Pb|As|Sb|Bi|Se|Te|Po|Cl|Br|At\b|[\bC|K|B|N|O|F|I\b]{1}'
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
    print "Illegal character '%s'" % t.value[0]
    t.skip(1)


# Build the lexer
lex.lex(debug=1)

        # Build the lexer
#     def build(self, **kwargs):
#         self.lexer = lex.lex(module=self, **kwargs)
#      # Test it output
#     def test(self,data):
#         self.lexer.input(data)
#         while True:
#              tok = self.lexer.token()
#              if not tok:
#                  break
#              print(tok)
#
# # Build the lexer and try it out
# m = MyLexer()
# m.build()           # Build the lexer
# m.test("Cl")     # Test it
#

