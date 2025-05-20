#Preguntar número de mallas
num_mallas = int(input("¿Cuántas mallas tiene el circuito?: "))

#listas para guardar datos
resistencias_propias = []
voltajes = []

# Preguntar datos de cada malla
for i in range(num_mallas):
    r = float(input(f"Suma de resistencias propias en malla {i+1} (ohms): "))
    v = float(input(f"Suma de fuentes en malla {i+1} (V, positivo si ayuda al sentido): "))
    resistencias_propias.append(r)
    voltajes.append(v)

#Preguntar resistencias compartidas entre mallas
resistencias_compartidas = [[0]*num_mallas for _ in range(num_mallas)]

for i in range(num_mallas):
    for j in range(i+1, num_mallas):
        r = float(input(f"Resistencia compartida entre malla {i+1} y malla {j+1} (0 si no hay): "))
        resistencias_compartidas[i][j] = r
        resistencias_compartidas[j][i] = r

for i in range(num_mallas):
    # Empieza la ecuación con la resistencia propia e intensidad propia
    ecuacion = f"{resistencias_propias[i]}·I{i+1}"
    
    # Recorremos otras mallas para ver si hay resistencias compartidas
    for j in range(num_mallas):
        if i != j and resistencias_compartidas[i][j] != 0:
            # Agregamos término con la intensidad de la otra malla
            ecuacion += f" + {resistencias_compartidas[i][j]}·I{j+1}"
    
    # Finalmente imprimimos el lado derecho (fuente)
    ecuacion += f" = {voltajes[i]}"
    
    print(f"Ecuación de Malla {i+1}: {ecuacion}")
