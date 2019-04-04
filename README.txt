Execução:
    Para que esse programa seja executado é preciso que a biblioteca ply esteja instalada, caso não esteja execute os seguintes comandos:
        pip install ply

    Todos os arquivos .smiles devem está dentro da pasta \app

    Antes de executar o programa, deve-se inserir o nome do arquivo .smiles a ser processado na linha 305 do arquivo mainContagemPronto.py que esta na pasta \app

    Através do terminal aberta dentro da pasta \app, executar o arquivo mainContagemPronto.py através do comando:
        python  mainContagemPronto.py

     No terminal será então pedido o número de átomos a serem buscados.

Saída:
    Como resultado serão gerados três arquivos:
        um de sucesso que é a contagem do número de átomos é igual ao número de átomos inserido,
        outro arquivo é o de insucesso que é a contagem do número de átomos diferente da inserida,
        por último é gerado um arquivo com os elementos que não puderam ser contada

    Todos os arquivos gerados estarão dentro da pasta \result