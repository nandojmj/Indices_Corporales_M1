# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 11:54:18 2025

@author: X1CARBON2
"""

# calculadora_indices.py

def calcular_IMC(peso: float, altura: float) -> float:
    """Calcula el Índice de Masa Corporal (IMC)."""
    return round(peso / (altura ** 2), 2)

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    """Calcula el porcentaje de grasa corporal basado en el IMC."""
    imc = peso / (altura ** 2)
    return round((1.2 * imc) + (0.23 * edad) - valor_genero - 5.4, 2)

def calcular_calorias_en_reposo(peso: float, altura_cm: float, edad: int, valor_genero: int) -> float:
    """Calcula la tasa metabólica basal (calorías en reposo)."""
    return round((10 * peso) + (6.25 * altura_cm) - (5 * edad) + valor_genero, 2)

def calcular_calorias_en_actividad(peso: float, altura_cm: float, edad: int, valor_genero: int, valor_actividad: float) -> float:
    """Calcula la cantidad de calorías quemadas según el nivel de actividad física."""
    calorias_reposo = calcular_calorias_en_reposo(peso, altura_cm, edad, valor_genero)
    return round(calorias_reposo * valor_actividad, 2)

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura_cm: float, edad: int, valor_genero: int) -> str:
    """Calcula el rango de calorías recomendado para adelgazar."""
    calorias_mantenimiento = calcular_calorias_en_reposo(peso, altura_cm, edad, valor_genero)
    min_calorias = round(calorias_mantenimiento * 0.8, 2)
    max_calorias = round(calorias_mantenimiento * 0.9, 2)
    return f"Para adelgazar es recomendado que consumas entre: {min_calorias} y {max_calorias} calorías al día."
