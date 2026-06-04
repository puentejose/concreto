# Calculadora para cantidades de materiales para dosificaciones de concreto
# Author: Ingeniero Jose Luis Puente Rodriguez

def calculadora_concreto():
    print("Calculadora de materiales para dosificaciones de concreto\n")

    # Dosificaciones de concreto para un saco de cemento (50 kg)
    # Diccionario con las dosificaciones para diferentes tipos de concreto
    # Cemento (1 saco de 50 kg), Arena, Grava y Agua (en baldes de 19 litros)
    
    resistencias = {
        "f'c 100 kg/cm²": {"cemento": 1, "arena": 8, "grava": 8.5, "agua": 3},
        "f'c 150 kg/cm²": {"cemento": 1, "arena": 5.5, "grava": 6.5, "agua": 2.5},
        "f'c 200 kg/cm²": {"cemento": 1, "arena": 4, "grava": 6, "agua": 2},
        "f'c 250 kg/cm²": {"cemento": 1, "arena": 3.5, "grava": 5, "agua": 1.5},
        "f'c 300 kg/cm²": {"cemento": 1, "arena": 2.5, "grava": 4.5, "agua": 1.5}
    }

    print("Seleccione la resistencia que desea:")
    for i, (resistencia, materiales) in enumerate(resistencias.items(), start=1):
        print(f"{i}. {resistencia}")
    print("\n")
          
# Ejecutar programa
if __name__ == "__main__":
    calculadora_concreto()