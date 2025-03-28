# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:02:03 2025

@author: X1CARBON2
"""

import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en cm: "))
    edad = int(input("Ingrese su edad en años: "))
    genero = input("Ingrese su género (M/F): ").strip().upper()
    valor_genero = 5 if genero == "M" else -161
    calorias_reposo = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print(f"Su tasa metabólica basal es: {calorias_reposo} calorías por día.")

if __name__ == "__main__":
    main()
