def check_word(palavra_necessaria,letras,letra_necessaria):
    #Este código faz parte dos exercicios do livro Pense Em Python (Allen B. Downey)
    """
    Valida se uma palavra pode ser formada a partir de um conjunto de letras,
    garantindo a presença de uma letra obrigatória e respeitando critérios de tamanho.

    Args:
        Palavra_necessaria (str): A palavra a ser testada.
        Letras (str): O conjunto de letras disponível.
        Letra_necessaria (str): A letra que obrigatoriamente deve estar na palavra.
    """
    #Normalização das Variáveis. (todas em letra minuscula, e sem espaço entre elas)
    palavra_minuscula = palavra_necessaria.lower().replace(" ", "")
    letras_minuscula = letras.lower().replace(" ", "")
    letra_necessaria_minuscula = letra_necessaria.lower().replace(" ", "")

    #Usando um filtro pela quantidade de letras.
    verificação_letra = len(letras)
    verificacao_palavra = len(palavra_minuscula)

    #Filtro para saber se a palavra possui 7 letras.
    if  verificação_letra != 7 :
        print("O numero de letras deve ser igual a 7!")
        return

    if verificacao_palavra <= 3 :
        print("A palavra deve conter no minimo 4 letras!")
        return

    #Filtro para saber se a letra necessaria está dentro do conjunto de letras.
    for i in letra_necessaria_minuscula :
        if i not in letras_minuscula :
            print("O conjunto de letras fornecidas, não possui a letra necessaria, por favor reescreva os parametros.")
            return


    #Filtro para saber se a palavra usa a letra necessaria.
    for i in letra_necessaria_minuscula :
        if i not in palavra_minuscula :
            print("Não possui a letra necessária")
            return
    print("Parábens! A Palavra é aceitavel!!")



check_word('color', 'ACDLORT', 'R')
check_word('ratatat', 'ACDLORT', 'R')
check_word('rat', 'ACDLORT', 'R')
