# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:01:30 2025

@author: X1CARBON2
"""

import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    genero = input("Ingrese su género (M/F): ").strip().upper()
    valor_genero = 10.8 if genero == "M" else 0
    porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print(f"Su porcentaje de grasa corporal es: {porcentaje_grasa}%")

if __name__ == "__main__":
    main()
