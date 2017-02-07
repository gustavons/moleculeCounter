# Yacc example

import ply.yacc as yacc

# Get the token map from the   This is required.
from LexerContagem import tokens
import LexerContagem as lexer


dic_elementos = {}

dic_valorelementos = {'C':4,'O':2,'N':3,'S':2,'F':1,'H':1,'B':4, 'Cl':1}

def p_expression_igual (p):
    'term :  term IGUAL term'
    print 'entrou igual'
    try:
        dic_elementos[p[3][0]] = dic_elementos[p[3][0]] + 1
    except IndexError:
        dic_elementos[p[3][0]] = 1

    except TypeError:
        print

    try:
        dic_elementos['H'] = dic_elementos['H'] - 2


    except IndexError:
        dic_elementos['H'] = dic_valorelementos[p[3][0]]
    except TypeError:
        print
        # print p[1]
    # if p[1] == 'C' and p[3] == 'C':
    #     print "entrou igual"
    #     dic_elementos[p[1]] = dic_elementos[p[1]] - 4

def p_expression_number (p):
    'term :  term NUMBER'
def p_expression_number_junto (p):
    'term :  term NUMBER term'

def p_expression_ceele (p):
    'term :  ce CEELE term'
    print 'entrou CEELE'
    try:
        dic_elementos['Cl'] = dic_elementos['Cl'] + 1
    except:
        dic_elementos['Cl'] = 1


    try:
        dic_elementos['H'] = dic_elementos['H'] - 1


    except :
        dic_elementos['H'] = dic_valorelementos['Cl']


def p_expression_ce(p):
    'ce : ELEMENTO'
def p_expression_simbolos(p):
    'term :  term SIMBOLOS'

def p_expression_simbolos_junto(p):
    'term :  term SIMBOLOS term'
# def p_expression_simbolos(p):
#     'expression :  term SIMBOLOS term'
#
# def p_termos(p):
#     'term : IGUAL'
def p_expression_nada(p):
    'term : ELEMENTO'
    print 'entrou nada'
    if p[1] == 'Cl':
        try:
            dic_elementos[p[1]] = dic_elementos[p[1]] + 1
        except:
            dic_elementos[p[1]] = 1

        try:
            dic_elementos['H'] = dic_elementos['H'] + dic_valorelementos[p[1]] - 2


        except:
            dic_elementos['H'] = dic_valorelementos[p[1]]
    else:
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


# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]
#
def p_term_hashtag (p):
    'term : term HASHTAG factor'
    if p[1] == 'C' and p[3] == 'C':
        print "entrou hastag"
        dic_elementos[p[1]] = dic_elementos[p[1]] - 6

def p_term_sifrao(p):
    'expression :  term SIFRAO factor'
    if p[1] == 'C' and p[3] == 'C':
        print "entrou sifrao"
        dic_elementos[p[1]] = dic_elementos[p[1]] - 8

# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]

def p_factor_num(p):
    'factor : ELEMENTO'

# def p_factor_expr(p):
#     'factor : expression'
#     p[0] = p[2]
# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"

# Build the parser
yacc.yacc(debug=True)


# Use this if you want to build the parser using LALR(1) instead of SLR
yacc.yacc(method="LALR")

yacc.parse('ClC')
print dic_elementos