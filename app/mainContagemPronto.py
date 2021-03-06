#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.yacc as yacc
import copy as copia

from LexerContagem import tokens
import LexerContagem as lexer
from datetime import datetime


def analise(file, quantidade_moleculas):

    # Nome dos arquivos criados
    nome_arquivo_sucesso = '../result/'+datetime.now().ctime()+'__saida_'+ str(quantidade_moleculas) + 'moleculas_ARQUIVO' + '.txt'
    sem_sucesso_nome_arquivo = '../result/'+datetime.now().ctime()+'__saida_diferente_de_' + str(quantidade_moleculas) + 'moleculas_ARQUIVO_'  + '.txt'
    sem_contar_nome_arquivo = '../result/'+datetime.now().ctime()+'__nao_contado_moleculas_ARQUIVO' + '.txt'

    sentinela = []
    if (quantidade_moleculas != -1):

        # Abrir para escriver no arquivo
        sucesso = open(nome_arquivo_sucesso, 'w')
        insucesso = open(sem_sucesso_nome_arquivo, 'w')
        nao_contado = open(sem_contar_nome_arquivo, 'w')

    # Definir o valor de elementos com a valencia variavel
    def p_variavel(p):
        'term : VARIAVEL'
        lower = p[1].islower()
        position =  p.lexer.lexpos
        letter = p[1].upper()
        l_simbol = 0
        r_simbol = 0
        try:
            ultimo = ''
            tolkien = p.lexer.clone()

            while(r_simbol < max(dic_valorelementos_variaveis[letter])-1):
                token_ver = tolkien.next().value
                if (token_ver.isdigit()):
                    break
                if (ultimo == '' and token_ver == '('):
                    break
                elif (token_ver == (')'or']') and ultimo ==''):
                    break
                if (token_ver == (')'or']')):
                    r_simbol += 1
                elif (token_ver == ('('or'[')):
                    l_simbol += 0
                elif (token_ver == ('=')):
                    if (ultimo == '('):
                        r_simbol += 1
                    else:
                        r_simbol += 2
                elif (token_ver == ('#')):
                    r_simbol += 3
                elif (token_ver == ('$')):
                    r_simbol += 4


                ultimo = token_ver
            # if (position > 2):
            #     r_simbol += ')'
        except:
            pass
        if (not lower and p.lexer.lexpos > 2):
            r_simbol += 1
        elif(lower and p.lexer.lexpos <= 1):
            r_simbol += 1

        if (lower and r_simbol==0):
            r_simbol += 3
        if(lower):
            valor = r_simbol
            letter = p[1].upper()
            try:
                dic_elementos[letter] = dic_elementos[letter] + 1
            except:
                dic_elementos[letter] = 1

            try:
                dic_elementos['H'] = dic_elementos['H'] + int(valor-3)

            except:

                dic_elementos['H'] = valor - 3

        # Verificando se o elemento tem ou não valencia variavel
        elif (r_simbol > dic_valorelementos[letter]):
            valor = r_simbol

            try:
                if (letter != 'H'):
                    dic_elementos['H'] = dic_elementos['H'] + valor - 2

            except:
                dic_elementos['H'] = valor

            try:
                dic_elementos[letter] = dic_elementos[letter] + 1
            except:
                dic_elementos[letter] = 1

        else:
            try:
                if (letter != 'H'):
                    dic_elementos['H'] = dic_elementos['H'] + dic_valorelementos[letter] - 2

            except:
                dic_elementos['H'] = dic_valorelementos[letter]

            try:
                dic_elementos[letter] = dic_elementos[letter] + 1
            except:
                dic_elementos[letter] = 1


    # definir o valor de cada elemento
    def p_expression_nada(p):
        'term : ELEMENTO'

        if (p[1] not in lista_elementosDuas):
            for i in range(0, len(p[1])):

                letter = p[1][i].upper()
                try:
                    if (letter != 'H'):
                        dic_elementos['H'] = dic_elementos['H'] + dic_valorelementos[letter] - 2

                except:
                    dic_elementos['H'] = dic_valorelementos[letter]

                try:
                    dic_elementos[letter] = dic_elementos[letter] + 1
                except:
                    dic_elementos[letter] = 1
        else:

            try:
                dic_elementos[p[1]] = dic_elementos[p[1]] + 1
            except:
                dic_elementos[p[1]] = 1

            try:
                dic_elementos['H'] = dic_elementos['H'] + dic_valorelementos[p[1]] - 2

            except:
                dic_elementos['H'] = dic_valorelementos[p[1]]
    # Definir o valor de cada elemento de uma cadeia ciclica
    def p_expression_menos(p):
        'term : ELEMENTOMINUS'

        for i in range(0, len(p[1])):

            letter = p[1][i].upper()
            try:
                dic_elementos[letter] = dic_elementos[letter] + 1
            except:
                dic_elementos[letter] = 1

            try:
                dic_elementos['H'] = dic_elementos['H'] + dic_valorelementos[letter]-3

            except:

                dic_elementos['H'] = int(dic_valorelementos[letter] -1)

    # As simbolos
    # def p_expression_simbolos(p):
    #     'term :  LSIMBOLOS term RSIMBOLOS'
        # print 'aqui'
    def p_expression_rsimbolos(p):
        'term : RSIMBOLOS'
    def p_expression_ssimbolos(p):
        'term : LSIMBOLOS'

    def p_expression_ponto(p):
        'term : PONTO'
        dic_elementos['H'] = dic_elementos['H'] + 2

    def p_expression_maior(p):
        'term : MAIOR'
        dic_elementos['H'] = dic_elementos['H'] + 2

    def p_expression_so_igual(p):
        'term : IGUAL'
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

    def p_expression_so_hashtag(p):
        'term : HASHTAG'
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
    def p_expression_so_sifrao(p):
        'term : SIFRAO'
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

    def p_error(p):
        print "Syntax error in input!"

    def p_ciclo(p):
        'term : term term'

    def p_aromatica(p):
        'term : term NUMBER'
        if (p[2] in sentinela):
            dic_elementos['H'] = dic_elementos['H'] - 2
            sentinela.remove(p[2])
        else:
            sentinela.append(p[2])


    # Build the parser
    yacc.yacc()
    # Use this if you want to build the parser using LALR(1) instead of SLR
    yacc.yacc(method="SLR")
    moleculas = 0
    codigo_linha = 0

    lista_resultados = []
    # função para realizar o processamento
    for linha in open(file,'r'):
    # for linha in ['N[C@@H](CO)C(O)=O']:
        dic_elementos = {}
        dic_valorelementos = {'H' : 1, 'Li' : 1, 'Na' : 1, 'K' : 1, 'Rb' : 1, 'Cs' : 1, 'Fr' : 1,
                              'Be' : 2, 'Mg' : 2, 'Ca' : 2, 'Sr' : 2, 'Ba' : 2, 'Ka' : 2, 'B' : 3, 'Al' : 3, 'Ga' : 3, 'In' : 3, 'Ti' : 3,
                              'C' : 4, 'Si' : 4, 'Ge' : 4, 'Sn' : 4, 'Pb' : 4,
                              'N' : 3, 'P' : 3, 'As' : 3, 'Sb' : 3, 'Bi' : 3,
                              'O' : 2, 'S' : 2, 'Se' : 2, 'Te' : 2, 'Po' : 2,
                              'F' : 1, 'Cl' : 1, 'Br' : 1, 'I' : 1, 'At' : 1
                              }
        dic_valorelementos_variaveis = {'P' : [4,5], 'S' : [3,4,5]}
        lista_elementosDuas = ['Mg', 'Br', 'In', 'Ka', 'Li', 'Pb', 'Si', 'As', 'Sn', 'Rb', 'Ti', 'Sb',
                             'Po', 'Sr', 'Be', 'Fr', 'Te', 'Ba', 'Cl',
                             'Ca', 'Al', 'Ge', 'Se', 'Ga', 'Na', 'Cs', 'Bi', 'At']
        moleculas += 1
        codigo_linha +=1
        try:
            yacc.parse(linha)
            print 'Processamento: '+ linha, dic_elementos
            if (dic_elementos['H'] < 0):
                dic_elementos['H'] = 0
            if (quantidade_moleculas != -1):

                if (quantidade_moleculas == somar_lista(dic_elementos.values())):
                    ## Abre arquivo de saida e insere o valor no arquivo de saida de sucesso
                    sucesso = open(nome_arquivo_sucesso, 'a+')
                    sucesso.writelines(str(codigo_linha) + ' ' + str(dic_elementos)+' Soma moleculas: '+str(somar_lista(dic_elementos.values()))
                                       +' Massa Molar: '+str(set_massa_molar(dic_elementos))+'\n')
                    sucesso.close()
                    lista_resultados.append(dic_elementos)
                else:
                    ## Abre arquivo de saida e insere o valor no arquivo de saida de insucesso
                    insucesso = open(sem_sucesso_nome_arquivo, 'a+')
                    insucesso.writelines(str(codigo_linha) + ' ' + str(dic_elementos)+' Soma moleculas: '+str(somar_lista(dic_elementos.values()))
                                         +' Massa Molar: '+str(set_massa_molar(dic_elementos))+'\n')
                    insucesso.close()
                    lista_resultados.append(dic_elementos)
            else:
                lista_resultados.append(dic_elementos)
        except:
            ## Abre arquivo de saida e insere o valor no arquivo de saida de insucesso
            nao_contado = open(sem_contar_nome_arquivo, 'a+')
            nao_contado.writelines(str(codigo_linha) + '   ' + linha)
            nao_contado.close()
            lista_resultados.append(dic_elementos)
            continue




    # Inprimir na tela numero de moleculas
    print 'Moleculas: '+ str(moleculas)
    if (quantidade_moleculas != -1):

        sucesso.close()
        insucesso.close()
    return lista_resultados
# Funcao para somar moleculas
def somar_lista(lista):
    soma = 0
    for i in lista:
        soma += int(i)

    return soma

# função para calculo da massa molar
def set_massa_molar(dic_com_dados):
    mol = {'H' : 1.00794, 'Li' : 6.941, 'Be' : 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.00674, 'O': 15.9994,
           'F': 18.9984, 'Na' : 22.989770, 'Mg' : 24.3050, 'Al' : 26.981538, 'Si' : 28.0855, 'P': 30.973761,
           'S': 32.066, 'Cl' : 35.453, 'K': 39.0983, 'Ca' : 40.078, 'Ga' : 69.723, 'Ge' : 72.64, 'As' : 74.92160,
           'Se' : 78.96, 'Br' : 79.904, 'Rb' : 85.4678, 'Sr' : 87.62, 'In' : 114.818, 'Sn' : 118.710, 'Sb' : 121.760,
           'Te' : 127.60, 'I': 126.90447, 'Cs' : 132.90545, 'Ba' : 137.327, 'Ti' : 204.3833, 'Pb' : 207.3,
           'Bi' : 208.98038, 'Po' : 209, 'At' : 210, 'Fr' : 223, 'Ra' : 226}
    massa_molar = 0

    for elemento in dic_com_dados.keys():
        massa_molar += dic_com_dados[elemento] * mol[elemento]

    return massa_molar



if __name__ == "__main__":
    # Nome do arquivo
    file = 'drugb_approved2.smiles'
    # file = 'teste.txt'
    # Captura o numero de atomos
    numero_atomos = int(input("Digite o numero de atomos: "))

    analise(file, numero_atomos)
