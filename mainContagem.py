# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from LexerContagem import tokens
import LexerContagem as lexer




def p_expression_igual (p):
    'expression :  expression IGUAL term '
    if p[1] == 'C' and p[3] == 'C':
        print "entrou igual"
        lexer.dic_elementos[p[1]] = lexer.dic_elementos[p[1]] - 4




def p_expression_nada(p):
    'term :  term factor '

    print p[1]
    print  p[2]
    if p[1] == 'C' and p[2] == 'C':
        print "entrou"
        lexer.dic_elementos[p[1]] = lexer.dic_elementos[p[1]] - 2

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
#
def p_term_hashtag (p):
    'term : term HASHTAG factor'
    if p[1] == 'C' and p[3] == 'C':
        print "entrou hastag"
        lexer.dic_elementos[p[1]] = lexer.dic_elementos[p[1]] - 6
#     p[0] = p[1] * p[3]

def p_term_sifrao(p):
    'expression :  term SIFRAO factor'
    if p[1] == 'C' and p[3] == 'C':
        print "entrou sifrao"
        lexer.dic_elementos[p[1]] = lexer.dic_elementos[p[1]] - 8

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : ELEMENTO'
    p[0] = p[1]

# def p_factor_expr(p):
#     'factor : expression'
#     p[0] = p[2]
# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"

# Build the parser
yacc.yacc()

# Use this if you want to build the parser using LALR(1) instead of SLR
yacc.yacc(method="LALR")

yacc.parse('CC')
print lexer.dic_elementos