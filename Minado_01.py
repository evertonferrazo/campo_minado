#Kauã Alves Lima
#Everton Ferraz de Oliveira

import random
caveira = '''
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
'''
def criar_quadro(tamanho, minas):
    quadro = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
    contar = 0
    while contar < minas:
        linha = random.randint(0, tamanho -1)
        coluna = random.randint(0, tamanho -1)
        if quadro[linha][coluna] != "*":
            quadro[linha][coluna] = "*"
            contar += 1
    return quadro

def contar_minas(quadro, linha, coluna):
    contar = 0
    tamanho = len(quadro)
    for i in range(max(0, linha-1), min(linha+2, tamanho)):
        for j in range(max(0, coluna-1), min(coluna+2, tamanho)):
            if quadro[i][j] == "*":
                contar += 1
    return contar

def imp_quadro(quadro):
    tamanho = len(quadro)
    print("    " + " ".join([chr(65 + i) for i in range(tamanho)]))
    print("   +" + "-" * (2 * tamanho - 1) + "+")
    for i in range(tamanho):
        print(f"{i+1} | " + " ".join(quadro[i]) + " |")
    print("   +" + "-"*(2*tamanho-1) + "+")

def jogar():
    print("----x----x---- CAMPO MINADO ----x----x----")

    tamanho = int(input("Informe o tamanho do campo (2 à 26): "))
    while tamanho < 2 or tamanho > 26:
        print("Valor Inválido!")
        tamanho = int(input("Informe o tamanho do campo: "))

    tamanho1 = tamanho * tamanho

    minas = int(input("Informe a quantidade de minas: "))
    if tamanho < 8:
        while minas >= tamanho1:
            print(f"Quantidade Inválida! O máximo de minas possíveis é {tamanho1 / 2}")
            minas = int(input("Informe a quantidade de minas: "))
    else:
        while minas > 50:
            print("Valor Inválido, o máximo permitido é 50.")
            minas = int(input("Informe a quantidade de minas: "))

    quadro = criar_quadro(tamanho, minas)
    quadro_visivel = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
    fim_jogo = False

    while not fim_jogo:
        imp_quadro(quadro_visivel)
        acao = input("Informe a letra M para marcar/desmarcar ou qualquer outra letra para abrir: ")

        posicao_linha = None
        while posicao_linha is None:
            posicao_linha = input("Informe a Linha: ")
            if not posicao_linha.isdigit():
                print("Valor inválido! Digite um número para a Linha.")
                posicao_linha = None
            else:
                linha = int(posicao_linha) - 1

        posicao_coluna = None
        while posicao_coluna is None:
            posicao_coluna = input("Informe a Coluna: ")
            if len(posicao_coluna) != 1 or not posicao_coluna.isalpha():
                print("Valor inválido! Digite uma única letra para a Coluna.")
                posicao_coluna = None
            else:
                coluna = ord(posicao_coluna.upper()) - 65

        if acao.lower() == "m" and "M":
            if quadro_visivel[linha][coluna] == " ":
                quadro_visivel[linha][coluna] = "X"
            else:
                quadro_visivel[linha][coluna] = " "
        else:
            if quadro[linha][coluna] == "*":
                print("BOOM! Você perdeu!")
                print(caveira)
                fim_jogo = True
            else:
                quadro_visivel[linha][coluna] = str(contar_minas(quadro, linha, coluna))

jogar()