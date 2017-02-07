from Contagem import contar

if __name__ == "__main__":
    dic_elementos = {}

    dic_valorelementos = {'C': 4, 'O': 2, 'N': 3, 'S': 2, 'F': 1, 'H': 1, 'B': 4, 'Cl': 1}
    moleculas = 0
    file = 'drug_revised_1_numbersatoms_33_(1).smiles'
    # verificar dados do arquivo
    for linha in open(file, 'r'):

        conta = contar(dic_elementos,dic_valorelementos)
        processamento = conta.passarPalavras(linha)
        moleculas = moleculas+1
        print 'Processamento: '
        print processamento
    print 'Moleculas:'
    print moleculas