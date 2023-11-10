import os
import random
import sys

TAM = 25
p1 = random.randint(0, 24)
p2 = random.randint(0, 24)

def sorteio_palavra():
    random.seed()
    quantidade = 0
    pala = []
    i = random.randint(0, 112)
    with open("ProjetoDB1-1.0- Caça-palavras/palavras.txt", "r") as palavras:
        for linha in palavras:
            palavra = linha.strip()
            pala.append(palavra)
            quantidade += 1
        
    return pala[i]


def sorteio_vogal():
    vogais = "AEIOU"
    return random.choice(vogais)

def sorteio_consoante():
    consoantes = "BCDFGHJKLMNPQRSTVWXYZ"
    return random.choice(consoantes)

def gerar_matriz():
    matriz = [[None for _ in range(25)] for _ in range(25)]

    for i in range(25):
        for j in range(25):
            if (i * 25 + j) % 3 == 0:
                matriz[i][j] = sorteio_vogal()
            else:
                matriz[i][j] = sorteio_consoante()
    
    return matriz


def inserir_palavra(palavra, matriz):
    random.seed()
    valida = 1
    
    print (f"{palavra}.")
    while valida != 0:
        resultado = 1 + random.randint(0, 3)
        i = 0

        if resultado == 1:
            if p1 + 1 < len(palavra):
                valida = 1
            else:
                for i in range(len(palavra)):
                    matriz[p1 - i][p2] = palavra[i]
                valida = 0

        elif resultado == 2:
            if (TAM - p1) + 1 < len(palavra):
                valida = 1
            else:
                for i in range(len(palavra)):
                    matriz[p1 + i][p2] = palavra[i]
                valida = 0

        elif resultado == 3:
            if (TAM - p2) + 1 < len(palavra):
                valida = 1
            else:
                for i in range(len(palavra)):
                    matriz[p1][p2 + i] = palavra[i]
                valida = 0

        elif resultado == 4:
            if p2 + 1 < len(palavra):
                valida = 1
            else:
                for i in range(len(palavra)):
                    matriz[p1][p2 - i] = palavra[i]
                valida = 0

        else:
            break

def exibir_matriz(matriz):
    for row in matriz:
        print(" ".join(row))
    print("\n")
    print("PROCURE".center(20))
    linha = int(input("Insira a linha: "))
    coluna = int(input("Insira a coluna: "))
    
    os.system("cls")
    if linha == p1+1 and coluna == p2+1:
        print("PARABÉNS".center(20))
        print("VOCÊ ACERTOU!!!".center(20))
    else:
        print("VOCÊ ERROU.")
    jogar_novamente()

def jogar_novamente():
    print("\n")
    print("Deseja jogar novamente?\n")
    resposta = int(input("1. Sim\n2. Não\n"))

    match resposta:

        case 1:
            os.system("cls")
            matriz = gerar_matriz()
            palavra = sorteio_palavra()
            inserir_palavra(palavra, matriz)
            exibir_matriz(matriz)
        case 2:
            sys.exit()

matriz = gerar_matriz()
palavra = sorteio_palavra()
inserir_palavra(palavra, matriz)
exibir_matriz(matriz)