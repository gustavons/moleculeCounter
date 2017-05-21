from Contagem import contar

if __name__ == "__main__":


    moleculas = 0
    file = 'drug_revised_1_numbersatoms_33_(1).smiles'
    # verificar dados do arquivo
    conta = contar()
    for linha in open(file, 'r'):


        processamento = conta.passarPalavras(linha)
        moleculas = moleculas+1
        print 'Processamento: '
        print processamento
    print 'Moleculas:'
    print moleculas