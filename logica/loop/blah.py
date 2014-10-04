# -*- coding: utf-8 -*-

def bleh(caixa_alta):
    if caixa_alta:
        return "BLEH!!!"
    else:
        return "bleh!!!"


def aluno_esta_aprovado(nome, nota):
    if nota < 3:
        return "Aluno {} REPROVADO!".format(nome)
    elif 3 <= nota < 5:
        return "Aluno {} ESTA DE RECUPERAÇÃO!".format(nome)
    else:
        return "Aluno {} APROVADO!".format(nome)

alunos = [
    ("Ze", 4),
    ("Andre", 3),
    ("Mariana", 6),
    ("Joao", 2)
]

for aluno in alunos:
    print(aluno_esta_aprovado(aluno[0], aluno[1]))

def faca_ou_morra(teste):
    while teste < 100:
        print(teste ** 2 + 5)
        teste = teste + 1

def tabuada(inicio=1, final=9):
    atual = inicio
    while atual <= final:
        tab = ["{} x {} = {}".format(numero, atual, numero * atual) for numero in range(0, 11)]
        print("\n################# Tabuada do {} ########################".format(atual))
        for linha in tab:
            print(linha)
        print("#########################################################\n".format(atual))
        atual = atual + 1