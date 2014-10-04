 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import sys

z = 0



def somar():
    a, b, c, d = sys.argv[1:]
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    print((a + b - c) * d)


def subtrair(numero_a, numero_b):
   return numero_a - numero_b

