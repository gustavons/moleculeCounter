# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calclex import tokens

def p_expression_ce(p):
    'expression : CE expression'
    ##p[0] = p[1] + p[3]
    
    
def p_expression_ce (p):
    'expression : CE expression'
    #p[0] = p[1] + p[3]
def p_expression_o (p):
    'expression : O expression'
    #p[0] = p[1] + p[3]
def p_expression_ene (p):
    'expression : ENE expression'
    #p[0] = p[1] + p[3]
def p_expression_ese (p):
    'expression : ESE expression'
    #p[0] = p[1] + p[3]
def p_expression_efe (p):
    'expression : EFE expression'
    #p[0] = p[1] + p[3]
def p_expression_agar (p):
    'expression : AGAR expression'
    #p[0] = p[1] + p[3]
def p_expression_be (p):
    'expression : BE expression'
    #p[0] = p[1] + p[3]
def p_expression_um (p):
    'expression : UM expression'
    #p[0] = p[1] + p[3]
def p_expression_dois (p):
    'expression : DOIS expression'
    #p[0] = p[1] + p[3]
def p_expression_tres (p):
    'expression : TRES expression'
    #p[0] = p[1] + p[3]
def p_expression_igual (p):
    'expression : IGUAL expression'
    #p[0] = p[1] + p[3]
def p_expression_arroba (p):
    'expression : ARROBA expression'
    #p[0] = p[1] + p[3]
def p_expression_barra (p):
    'expression : BARRA expression'
    #p[0] = p[1] + p[3]
def p_expression_contrabarra (p):
    'expression : CONTRABARRA expression'
    #p[0] = p[1] + p[3]
#
# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]
#
# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]
#
# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]
#
# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]
#
# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]
#
# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]
#
def p_factor_expr(p):
     'expression : LPAREN expression RPAREN'
     p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"

# Build the parser
paser = yacc.yacc()

# Use this if you want to build the parser using LALR(1) instead of SLR
# yacc.yacc(method="LALR")

while 1:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = yacc.parse(s)
   print result
