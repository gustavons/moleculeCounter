import ply.yacc as yacc

from LexerContagem import tokens
import LexerContagem as lexer
def analise(file, quantidade_moleculas):

    # Nome dos arquivos criados
    nome_arquivo_sucesso = 'saida_' + str(quantidade_moleculas) + '_moleculas_ARQUIVO_' + str(file) + '.txt'
    sem_sucesso_nome_arquivo = 'saida_diferente_de_' + str(quantidade_moleculas) + '_moleculas_ARQUIVO_' + file + '.txt'
    sem_contar_nome_arquivo = 'nao_contado_moleculas_ARQUIVO_' + file + '.txt'


    sucesso = open(nome_arquivo_sucesso, 'w')
    insucesso = open(sem_sucesso_nome_arquivo, 'w')
    nao_contado = open(sem_contar_nome_arquivo, 'w')


    def p_expression_nada(p):
        'term : ELEMENTO'
        for i in range(0, len(p[1])):

            letter = p[1][i].upper()
            try:
                # if (letter != 'H'):
                dic_elementos['H'] = dic_elementos['H'] + dic_valorelementos[letter] - 2

            except:
                dic_elementos['H'] = dic_valorelementos[letter]

            try:
                dic_elementos[letter] = dic_elementos[letter] + 1
            except:
                dic_elementos[letter] = 1

    # def p_expression_termo(p):
    #     'term : menos'

    def p_expression_menos(p):
        'term : ELEMENTOMINUS'

        for i in range(0, len(p[1])):

            letter = p[1][i].upper()
            try:
                # if (letter != 'H'):
                dic_elementos['H'] = dic_elementos['H'] + int(dic_valorelementos[letter]*0.25)

            except:
                dic_elementos['H'] = int(dic_valorelementos[letter] * 0.25)

            try:
                dic_elementos[letter] = dic_elementos[letter] + 1
            except:
                dic_elementos[letter] = 1






    def p_expression_ceele (p):
            'term : term CEELE term'
            try:
                dic_elementos['Cl'] = dic_elementos['Cl'] + 1
            except:
                dic_elementos['Cl'] = 1


            try:
                dic_elementos['H'] = dic_elementos['H'] - 1


            except :
                dic_elementos['H'] = dic_valorelementos['Cl']

    def p_so_ceele(p):
        'term : ce CEELE'

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


    def p_expression_igual (p):
        'term :  term IGUAL term'
        try:
            dic_elementos[p[3][0].upper()] = dic_elementos[p[3][0].upper()] + 1
        except IndexError:
            dic_elementos[p[3][0].upper()] = 1

        except TypeError:
            pass

        try:
            dic_elementos['H'] = dic_elementos['H'] - 2


        except IndexError:
            dic_elementos['H'] = dic_valorelementos[p[3][0].upper()]
        except TypeError:
            pass


    def p_term_hashtag (p):
            'term : term HASHTAG term'
            try:
                dic_elementos[p[3][0].upper()] = dic_elementos[p[3][0].upper()] + 1
            except IndexError:
                dic_elementos[p[3][0].upper()] = 1

            except TypeError:
                pass

            try:
                dic_elementos['H'] = dic_elementos['H'] - 4


            except IndexError:
                dic_elementos['H'] = dic_valorelementos[p[3][0].upper()]
            except TypeError:
                pass
    def p_term_sifrao(p):
        'term :  term SIFRAO term'
        try:
            dic_elementos[p[3][0].upper()] = dic_elementos[p[3][0].upper()] + 1
        except IndexError:
            dic_elementos[p[3][0].upper()] = 1

        except TypeError:
            pass

        try:
            dic_elementos['H'] = dic_elementos['H'] - 6
        except IndexError:
            dic_elementos['H'] = dic_valorelementos[p[3][0].upper()]
        except TypeError:
            pass


    def p_simbolos_juntos(p):
        'term : SIMBOLOS term'


    def p_error(p):
        print "Syntax error in input!"

    def p_aromatica(p):
        'term : NUMBER term NUMBER'
        print 'entrouuuuuuu;........'
        dic_elementos['H'] = dic_elementos['H'] - 2
        

    # Build the parser
    yacc.yacc(debug=True)
    # Use this if you want to build the parser using LALR(1) instead of SLR
    yacc.yacc(method="LALR")
    moleculas = 0
    codigo_linha = 0


    # for linha in open(file,'r'):
    for linha in ['C12C3C4C1C5C4C3C25']:
        dic_elementos = {}
        dic_valorelementos = {'H': 1,'Li': 1, 'Na':1, 'K': 1, 'Rb': 1, 'Cs': 1, 'Fr': 1, 'Cl':1,

                              'C':4,

                              }
        moleculas += 1
        codigo_linha +=1
        try:
            yacc.parse(linha)
            print 'Processamento: '+ linha, dic_elementos

            if (quantidade_moleculas == somar_lista(dic_elementos.values())):

                ## Abre arquivo de saida e insere o valor no arquivo de saida de sucesso
                sucesso = open(nome_arquivo_sucesso, 'a+')
                sucesso.writelines(str(codigo_linha) + ' ' + str(dic_elementos)+' Soma moleculas: '+str(somar_lista(dic_elementos.values()))+ '\n')
                sucesso.close()

            else:
                ## Abre arquivo de saida e insere o valor no arquivo de saida de insucesso
                insucesso = open(sem_sucesso_nome_arquivo, 'a+')
                insucesso.writelines(str(codigo_linha) + ' ' + str(dic_elementos)+' Soma moleculas: '+str(somar_lista(dic_elementos.values()))+ '\n')
                insucesso.close()
        except:
            ## Abre arquivo de saida e insere o valor no arquivo de saida de insucesso
            nao_contado = open(sem_contar_nome_arquivo, 'a+')
            nao_contado.writelines(str(codigo_linha) + '   ' + linha +'\n')
            nao_contado.close()
            continue

    # Inprimir na tela numero de moleculas
    print 'Moleculas: '+ str(moleculas)
    sucesso.close()
    insucesso.close()
# Funcao para somar moleculas
def somar_lista(lista):
    soma = 0
    for i in lista:
        soma += int(i)

    return soma
if __name__ == "__main__":
    # Nome do arquivo
    file = 'drugb_approved2.smiles'
    # Captura o numero de atomos
    # numero_atomos = int(input("Digite o numero de atomos: "))

    analise(file, 1)
