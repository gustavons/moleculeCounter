
import ply.yacc as yacc

# Get the token map from the   This is required.

from LexerContagem import tokens

class contar(object): #dic_elementos, dic_valorelementos):

    def __init__(self):
        self.dic_elementos = {}
        self.dic_valorelementos = {'C': 4, 'O': 2, 'N': 3, 'S': 2, 'F': 1, 'H': 1, 'B': 4, 'Cl': 1}

    def p_expression_igual (self,p):
        'term :  term IGUAL term'
        try:
            self.dic_elementos[p[3][0]] = self.dic_elementos[p[3][0]] + 1
        except IndexError:
            self.dic_elementos[p[3][0]] = 1

        except TypeError:
            print

        try:
            self.dic_elementos['H'] = self.dic_elementos['H'] - 2


        except IndexError:
            self.dic_elementos['H'] = self.dic_valorelementos[p[3][0]]
        except TypeError:
            print

    def p_expression_number (self, p):
        'term :  term NUMBER'
    def p_expression_number_junto (self, p):
        'term :  term NUMBER term'

    def p_expression_ceele (self, p):
        'term :  ce CEELE term'
        try:
            self.dic_elementos['Cl'] = self.dic_elementos['Cl'] + 1
        except:
            self.dic_elementos['Cl'] = 1


        try:
            self.dic_elementos['H'] = self.dic_elementos['H'] - 1


        except :
            self.dic_elementos['H'] = self.dic_valorelementos['Cl']


    def p_expression_ce(self, p):
        'ce : ELEMENTO'
    def p_expression_simbolos(self, p):
        'term :  term SIMBOLOS'

    def p_expression_simbolos_junto(self, p):
        'term :  term SIMBOLOS term'

    def p_expression_nada(self, p):
        'term : ELEMENTO'
        if p[1] == 'Cl':
            try:
                self.dic_elementos[p[1]] = self.dic_elementos[p[1]] + 1
            except:
                self.dic_elementos[p[1]] = 1

            try:
                self.dic_elementos['H'] = self.dic_elementos['H'] + self.dic_valorelementos[p[1]] - 2


            except:
                self.dic_elementos['H'] = self.dic_valorelementos[p[1]]
        else:
            for i in p[1]:

                try:
                    self.dic_elementos[i] = self.dic_elementos[i] + 1
                except:
                    self.dic_elementos[i] = 1

                try:
                    self.dic_elementos['H'] = self.dic_elementos['H'] + self.dic_valorelementos[i] - 2


                except:
                    self.dic_elementos['H'] = self.dic_valorelementos[i]
                        # CONSFHB


    def p_term_hashtag (self, p):
        'term : term HASHTAG term'
        try:
            self.dic_elementos[p[3][0]] = self.dic_elementos[p[3][0]] + 1
        except IndexError:
            self.dic_elementos[p[3][0]] = 1

        except TypeError:
            print

        try:
            self.dic_elementos['H'] = self.dic_elementos['H'] - 4


        except IndexError:
            self.dic_elementos['H'] = self.dic_valorelementos[p[3][0]]
        except TypeError:
            print
    def p_term_sifrao(self, p):
        'term :  term SIFRAO term'
        try:
            self.dic_elementos[p[3][0]] = self.dic_elementos[p[3][0]] + 1
        except IndexError:
            self.dic_elementos[p[3][0]] = 1

        except TypeError:
            print

        try:
            self.dic_elementos['H'] = self.dic_elementos['H'] - 6


        except IndexError:
            self.dic_elementos['H'] = self.dic_valorelementos[p[3][0]]
        except TypeError:
            print
    #
    # def p_factor_num(p):
    #     'factor : ELEMENTO'

    def p_error(self, p):
        print "Syntax error in input!"

    yacc.yacc(debug=True)

    # Use this if you want to build the parser using LALR(1) instead of SLR
    yacc.yacc(method="LALR")

    def passarPalavras(self,palavra):
        # Build the parser

        yacc.parse(palavra)
        return self.dic_elementos