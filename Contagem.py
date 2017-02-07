
import ply.yacc as yacc

# Get the token map from the   This is required.

from LexerContagem import tokens

dic_elementos = {}
dic_valorelementos = {}
class contar(dic_elementos, dic_valorelementos):
    def __init__(self):
        self.dic_elementos =  dic_elementos.copy()
        self.dic_valorelementos = dic_valorelementos.copy()
    def p_expression_igual (p):
        'term :  term IGUAL term'
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

    def p_expression_number (p):
        'term :  term NUMBER'
    def p_expression_number_junto (p):
        'term :  term NUMBER term'

    def p_expression_ceele (p):
        'term :  ce CEELE term'
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

    def p_expression_nada(p):
        'term : ELEMENTO'
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


    def p_term_hashtag (p):
        'term : term HASHTAG term'
        try:
            dic_elementos[p[3][0]] = dic_elementos[p[3][0]] + 1
        except IndexError:
            dic_elementos[p[3][0]] = 1

        except TypeError:
            print

        try:
            dic_elementos['H'] = dic_elementos['H'] - 4


        except IndexError:
            dic_elementos['H'] = dic_valorelementos[p[3][0]]
        except TypeError:
            print
    def p_term_sifrao(p):
        'term :  term SIFRAO term'
        try:
            dic_elementos[p[3][0]] = dic_elementos[p[3][0]] + 1
        except IndexError:
            dic_elementos[p[3][0]] = 1

        except TypeError:
            print

        try:
            dic_elementos['H'] = dic_elementos['H'] - 6


        except IndexError:
            dic_elementos['H'] = dic_valorelementos[p[3][0]]
        except TypeError:
            print
    #
    # def p_factor_num(p):
    #     'factor : ELEMENTO'

    def p_error(p):
        print "Syntax error in input!"

    # Build the parser
    yacc.yacc(debug=True)


    # Use this if you want to build the parser using LALR(1) instead of SLR
    yacc.yacc(method="LALR")

    def passarPalavras(self,palavra):
        yacc.parse(palavra)
        return dic_elementos