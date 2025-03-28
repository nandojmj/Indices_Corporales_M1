# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:03:15 2025

@author: X1CARBON2
"""

import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en cm: "))
    edad = int(input("Ingrese su edad en años: "))
    genero = input("Ingrese su género (M/F): ").strip().upper()
    valor_genero = 5 if genero == "M" else -161
    
    mensaje = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(mensaje)

if __name__ == "__main__":
    main()
