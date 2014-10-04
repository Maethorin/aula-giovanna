# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse


def home(request):
    nome = ""
    idade = ""
    if request.method == "POST":
        nome = request.POST["nome"]
        idade = request.POST["idade"]

    extra = request.GET.get("extra", "")
    contexto = {
        "nome": nome,
        "idade": idade,
        "extra": extra,
        "eh_post": request.method == "POST"
    }
    return TemplateResponse(request, "aula.html", contexto)

