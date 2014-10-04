# -*- coding: utf-8 -*-


class Botao(object):
    def __init__(self, label):
        self.label = label
        self.valor = None
        self.registrado = None

    @classmethod
    def criar_botoes(cls, label_valores):
        return [cls(label, valor) for label, valor in label_valores]

    def pressionar(self):
        self.registrado = self.valor

    def exibir(self):
        print("-----")
        print "| {} |".format(self.label)
        print "-----"


class BotaoNumerico(Botao):
    def __init__(self, label, valor):
        super(BotaoNumerico, self).__init__(label)
        self.valor = valor


class BotaoOperacao(Botao):
    def __init__(self, label, operacao):
        super(BotaoOperacao, self).__init__(label)
        self.valor = operacao


class Memoria(object):
    pass


class Display(object):
    def exibir(self):
        print " ----------------"
        print "|              0 |"
        print " ----------------"


class Calculadora(object):
    def __init__(self, nome):
        self.nome = "Calculadora {}".format(nome)
        self.display = Display()
        self._memoria = Memoria()
        self._botoes = []

    @property
    def botoes(self):
        if not self._botoes:
            botoes_numericos = BotaoNumerico.criar_botoes([(str(num), num) for num in range(0, 10)])
            botoes_operacoes = BotaoOperacao.criar_botoes([("+", "Soma"), ("-", u"Subtração"), ("*", u"Multiplicação"), ("/", u"Divisão")])
            self._botoes.extend(botoes_numericos)
            self._botoes.extend(botoes_operacoes)
        return self._botoes

    def calcular(self):
        return self.botoes[0].registrado + self.botoes[1].registrado

    def mostrar_display(self):
        self.display.exibir()

    def mostrar_botoes(self):
        for botao in self.botoes:
            botao.exibir()
