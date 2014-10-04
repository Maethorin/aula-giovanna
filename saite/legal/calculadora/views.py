# -*- coding: utf-8 -*-

from django.template.response import TemplateResponse


def calculadora(request):
    contexto = {
        "resultado": 0,
        "mensagem": "",
        "operando_1": 0,
        "operando_2": 0,
        "operacoes": ["soma", "subtracao", "multiplicacao", "divisao"],
        "grupo": [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, "C", "="]],
    }
    if request.method == "POST":
        try:
            contexto["operando_1"] = int(request.POST["numero_1"])
            contexto["operando_2"] = int(request.POST["numero_2"])
        except ValueError:
            contexto["mensagem"] = "Digite o número!"
        try:
            contexto["operador"] = request.POST["operacao"]
            if contexto["operador"] == "soma":
                contexto["resultado"] = contexto["operando_1"] + contexto["operando_2"]
            if contexto["operador"] == "subtracao":
                contexto["resultado"] = contexto["operando_1"] - contexto["operando_2"]
            if contexto["operador"] == "multiplicacao":
                contexto["resultado"] = contexto["operando_1"] * contexto["operando_2"]
            if contexto["operador"] == "divisao":
                contexto["resultado"] = float(contexto["operando_1"]) / float(contexto["operando_2"])
        except KeyError:
            contexto["mensagem"] = "Escolha a operação, seu animal!"
    contexto["resultado"] = deixa_bonito(contexto["resultado"])
    return TemplateResponse(request, "calculadora.html", contexto)


def deixa_bonito(resultado):
    resultado = str(resultado)
    if len(resultado) <= 3:
        return resultado
    outra = []
    for i in range(len(resultado), 3, -3):
        indice = i - 1
        depois = ((indice - 3) * -1)
        antes = ""
        if i == len(resultado):
            parte = resultado[:depois]
        else:
            antes = (indice * -1)
            if abs(depois) > 0:
                parte = resultado[antes:depois]
            else:
                parte = resultado[antes:]
        outra.append(parte)
        print "indice: {} | resultado[{}:{}] = {}".format(indice, antes, depois, parte)

    return ".".join(outra)
    # return "{}.{}.{}.{}.{}".format(resultado[:-12],resultado[-12:-9],resultado[-9:-6], resultado[-6:-3], resultado[-3:])





