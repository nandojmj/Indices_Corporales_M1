# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:02:35 2025

@author: X1CARBON2
"""

import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en cm: "))
    edad = int(input("Ingrese su edad en años: "))
    genero = input("Ingrese su género (M/F): ").strip().upper()
    valor_genero = 5 if genero == "M" else -161
    
  # Mostrar opciones de actividad física
    print("\nSeleccione su nivel de actividad física:")
    print("1. Poco o ningún ejercicio")
    print("2. Ejercicio ligero (1 a 3 días a la semana)")
    print("3. Ejercicio moderado (3 a 5 días a la semana)")
    print("4. Deportista (6 a 7 días a la semana)")
    print("5. Atleta (entrenamientos mañana y tarde)")

    # Diccionario de opciones
    opciones_actividad = {
        "1": 1.2,
        "2": 1.375,
        "3": 1.55,
        "4": 1.725,
        "5": 1.9
    }

    # Solicitar selección y validar entrada
    opcion = input("\nIngrese el número correspondiente a su nivel de actividad: ").strip()
    while opcion not in opciones_actividad:
        print("Opción no válida. Inténtelo de nuevo.")
        opcion = input("Ingrese el número correspondiente a su nivel de actividad: ").strip()
    
    valor_actividad = opciones_actividad[opcion]
    
    calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print(f"Su gasto calórico diario es: {calorias_actividad} calorías.")

if __name__ == "__main__":
    main()
