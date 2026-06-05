# Calculadora para cantidades de materiales para dosificaciones de concreto
# Author: Ingeniero Jose Luis Puente Rodriguez

def calculadora_concreto():
    print("Calculadora de materiales para dosificaciones de concreto\n")

    # Dosificaciones de concreto para un saco de cemento (50 kg)
    # Diccionario con las dosificaciones para diferentes tipos de concreto
    # Cemento (1 saco de 50 kg), Arena, Grava y Agua (en baldes de 19 litros)
    
    resistencias = {
        "1": {"nombre":"f'c 100 kg/cm2","cemento": 1, "arena": 8, "grava": 8.5, "agua": 3, "rendimiento_1m3": 0.20},
        "2": {"nombre":"f'c 150 kg/cm2","cemento": 1, "arena": 5.5, "grava": 6.5, "agua": 2.5, "rendimiento_1m3": 0.167},
        "3": {"nombre":"f'c 200 kg/cm2","cemento": 1, "arena": 4, "grava": 6, "agua": 2, "rendimiento_1m3": 0.143},
        "4": {"nombre":"f'c 250 kg/cm2","cemento": 1, "arena": 3.5, "grava": 5, "agua": 1.5, "rendimiento_1m3": 0.125},
        "5": {"nombre":"f'c 300 kg/cm2","cemento": 1, "arena": 2.5, "grava": 4.5, "agua": 1.5, "rendimiento_1m3": 0.112}
    }

    #Imprimir opciones de dosificación
    print("Seleccione la resistencia que desea:")
    for key, data in resistencias.items():
        print(f"{key}. {data['nombre']}")
    print("\n")

    # Solicitar al usuario que seleccione una opción
    opcion = input("\nIngresa el número (1-5): ").strip()
    if opcion not in resistencias:
        print("Opción no válida. Usando f'c 200 kg/cm² por seguridad.")
        mezcla = resistencias["3"]
    else:
        mezcla = resistencias[opcion]
    #Imprimir opcion elegida
    print(f"\nDosificación seleccionada: {mezcla['nombre']}")
    # Solicitar al usuario la cantidad de concreto que desea preparar en metros cúbicos
    try:
        cantidad_m3 = float(input("Ingrese la cantidad de concreto que desea preparar (en m³): "))
        if cantidad_m3 <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")
    except ValueError:
        print(f"Error, ingrese un número válido por favor.")
        return
    # Calcular la cantidad de materiales necesarios
    sacos_cemento = cantidad_m3 / mezcla["rendimiento_1m3"]
    arena = sacos_cemento * mezcla["arena"]
    grava = sacos_cemento * mezcla["grava"]
    agua = sacos_cemento * mezcla["agua"]

    # Imprimir los resultados
    print(f"\nMateriales necesarios para {cantidad_m3} m³ de concreto:")
    print(f"Sacos de cemento: {sacos_cemento:.2f}")
    print(f"Arena (en baldes de 19 litros): {arena:.2f}")
    print(f"Grava (en baldes de 19 litros): {grava:.2f}")
    print(f"Agua (en baldes de 19 litros): {agua:.2f}")

    # TODO: redondear los botes al número entero más alto 

# Ejecutar programa
if __name__ == "__main__":
    calculadora_concreto()