# Yacc example

import ply.yacc as yacc

# Get the token map from the   This is required.
from LexerContagem import tokens
import LexerContagem as lexer


dic_elementos = {}

dic_valorelementos = {'C':4,'O':2,'N':3,'S':2,'F':1,'H':1,'B':4}
# dic_elementos['H'] = 0

def p_expression_igual (p):
    'expression :  term IGUAL term] '
    try:
        dic_elementos[p[3][0]] = dic_elementos[p[3][0]] + 1
    except :
        dic_elementos[p[3][0]] = 1

    try:
        dic_elementos['H'] = dic_elementos['H'] + dic_valorelementos[p[3][0]] - 2


    except:
        dic_elementos['H'] = dic_valorelementos[p[3][0]]
    # print p[1]
    # if p[1] == 'C' and p[3] == 'C':
    #     print "entrou igual"
    #     dic_elementos[p[1]] = dic_elementos[p[1]] - 4




def p_expression_nada(p):
    'term :  ELEMENTO'
    for i in p[1]:

        try:
            dic_elementos[i] = dic_elementos[i] + 1
        except:
            dic_elementos[i] = 1

        try:
            dic_elementos['H'] = dic_elementos['H'] + dic_valorelementos[i] - 2


        except:
            dic_elementos['H'] = dic_valorelementos[i]
                # CONSFHB
        # if p[1][i] == 'O' :
        #     try:
        #         # dic_elementos['H'] = dic_elementos['H'] + 1
        #         dic_elementos[p[1][i]] = dic_elementos[p[1][i]] + 1
        #
        #     except:
        #         dic_elementos['H'] = 2
        #         dic_elementos[p[1][i]] =  1
        # if p[1][i] == 'N' :
        #     try:
        #         dic_elementos['H'] = dic_elementos['H'] + 2
        #         dic_elementos[p[1][i]] = dic_elementos[p[1][i]] + 1
        #
        #     except:
        #         dic_elementos['H'] = 3
        #         dic_elementos[p[1][i]] =  1
        #
        # if p[1][i] == 'S' :
        #     try:
        #         dic_elementos['H'] = dic_elementos['H'] + 2
        #         dic_elementos[p[1][i]] = dic_elementos[p[1][i]] + 1
        #
        #     except:
        #         dic_elementos['H'] = 4
        #         dic_elementos[p[1][i]] =  1
        #
        # if p[1][i] == 'F' :
        #     try:
        #         dic_elementos['H'] = dic_elementos['H'] + 2
        #         dic_elementos[p[1][i]] = dic_elementos[p[1][i]] + 1
        #
        #     except:
        #         dic_elementos['H'] = 4
        #         dic_elementos[p[1][i]] =  1
        # if p[1][i] == 'H' :
        #     try:
        #         dic_elementos['H'] = dic_elementos['H'] + 2
        #         dic_elementos[p[1][i]] = dic_elementos[p[1][i]] + 1
        #
        #     except:
        #         dic_elementos['H'] = 4
        #         dic_elementos[p[1][i]] =  1
        #
        # if p[1][i] == 'B' :
        #     try:
        #         dic_elementos['H'] = dic_elementos['H'] + 2
        #         dic_elementos[p[1][i]] = dic_elementos[p[1][i]] + 1
        #
        #     except:
        #         dic_elementos['H'] = 4
        #         dic_elementos[p[1][i]] =  1
        #

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
#
def p_term_hashtag (p):
    'term : term HASHTAG factor'
    if p[1] == 'C' and p[3] == 'C':
        print "entrou hastag"
        dic_elementos[p[1]] = dic_elementos[p[1]] - 6
#     p[0] = p[1] * p[3]

def p_term_sifrao(p):
    'expression :  term SIFRAO factor'
    if p[1] == 'C' and p[3] == 'C':
        print "entrou sifrao"
        dic_elementos[p[1]] = dic_elementos[p[1]] - 8

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

yacc.parse('C=C')
print dic_elementos