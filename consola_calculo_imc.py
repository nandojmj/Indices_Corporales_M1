# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 11:58:06 2025

@author: X1CARBON2
"""

import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calc.calcular_IMC(peso, altura)
    print(f"Su IMC es: {imc}")

if __name__ == "__main__":
    main()
