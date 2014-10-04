# -*- coding: utf-8 -*-

from objetos import Calculadora


def executar():
    calc = Calculadora("Legal")
    calc.mostrar_display()
    calc.mostrar_botoes()



if __name__ == "__main__":
    executar()