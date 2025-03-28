# 📌 Proyecto de Modulo 1: Calculadora de Índices Corporales
## Programación en Python - U. de los Andes

## 📖 Descripción
Este proyecto es una calculadora de índices corporales que permite calcular diferentes métricas relacionadas con la salud y el estado físico. Está compuesto por un módulo de funciones (`calculadora_indices.py`) y cinco programas de consola que permiten realizar cálculos específicos.

## 🛠️ Estructura del Proyecto
```
📂 CalculadoraIndices
│-- 📄 calculadora_indices.py  # Módulo con funciones para los cálculos
│-- 📄 consola_calculo_imc.py  # Calcula el Índice de Masa Corporal (IMC)
│-- 📄 consola_calculo_porcentaje_grasa.py  # Calcula el porcentaje de grasa corporal
│-- 📄 consola_calculo_calorias_reposo.py  # Calcula las calorías en reposo (TMB)
│-- 📄 consola_calculo_calorias_actividad.py  # Calcula el gasto calórico según la actividad física
│-- 📄 consola_calculo_calorias_adelgazar.py  # Recomienda un rango de calorías para adelgazar
│-- 📄 README.md  # Documentación del proyecto
```

## 📌 Requisitos
- Python 3.x
- Spyder (opcional, recomendado para ejecutar el código)

## 🚀 Instalación y Ejecución
1. Clona o descarga este repositorio en tu equipo.
2. Asegúrate de que tienes Python instalado.
3. Ejecuta cada script según el cálculo que desees realizar.

Por ejemplo, para calcular el IMC, ejecuta:
```sh
python consola_calculo_imc.py
```

## 🔍 Uso de los Scripts
Cada archivo de consola solicita los datos al usuario, realiza el cálculo utilizando `calculadora_indices.py` y muestra el resultado en la terminal.

### 1️⃣ Índice de Masa Corporal (IMC)
Ejecuta:
```sh
python consola_calculo_imc.py
```
Entrada:
```
Ingrese su peso en kg: 81
Ingrese su altura en metros: 1.75
```
Salida:
```
Su IMC es: 26.45
```

### 2️⃣ Porcentaje de Grasa Corporal
Ejecuta:
```sh
python consola_calculo_porcentaje_grasa.py
```
Entrada:
```
Ingrese su peso en kg: 81
Ingrese su altura en metros: 1.75
Ingrese su edad en años: 20
Ingrese su género (M/F): M
```
Salida:
```
Su porcentaje de grasa corporal es: 20.14%
```

### 3️⃣ Calorías en Reposo (Tasa Metabólica Basal)
Ejecuta:
```sh
python consola_calculo_calorias_reposo.py
```
Entrada:
```
Ingrese su peso en kg: 81
Ingrese su altura en cm: 175
Ingrese su edad en años: 20
Ingrese su género (M/F): M
```
Salida:
```
Su tasa metabólica basal es: 1808.75 calorías por día.
```

### 4️⃣ Calorías con Actividad Física
Ejecuta:
```sh
python consola_calculo_calorias_actividad.py
```
Entrada:
```
Ingrese su peso en kg: 81
Ingrese su altura en cm: 175
Ingrese su edad en años: 20
Ingrese su género (M/F): M
Seleccione su nivel de actividad física:
1: Poco o ningún ejercicio (1.2)
2: Ejercicio ligero (1.375)
3: Ejercicio moderado (1.55)
4: Deportista (1.725)
5: Atleta (1.9)
Ingrese el número correspondiente a su nivel de actividad:3
```
Salida:
```
Su gasto calórico diario es: 2803.56 calorías.
```

### 5️⃣ Calorías para Adelgazar
Ejecuta:
```sh
python consola_calculo_calorias_adelgazar.py
```
Entrada:
```
Ingrese su peso en kg: 81
Ingrese su altura en cm: 175
Ingrese su edad en años: 20
Ingrese su género (M/F): M
```
Salida:
```
Para adelgazar es recomendado que consumas entre: 1447.0 y 1627.88 calorías al día.
```

## 📜 Licencia
Este proyecto es de código abierto y puedes modificarlo y distribuirlo libremente.

## 👨‍💻 Autor
Desarrollado por [Tu Nombre] 😃.

