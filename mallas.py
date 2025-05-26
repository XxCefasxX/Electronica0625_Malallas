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
    # Creamos lista de términos (coeficiente, índice de I)
    terminos = [(resistencias_propias[i], i)]  # término propio: coeficiente y su índice
    
    # Agregamos términos compartidos (coeficiente, índice)
    for j in range(num_mallas):
        if i != j and resistencias_compartidas[i][j] != 0:
            terminos.append((resistencias_compartidas[i][j], j))
    
    # Ordenamos por índice de la intensidad (segunda posición de la tupla)
    terminos.sort(key=lambda x: x[1])
    
    # Formamos la ecuación uniendo los términos ordenados
    ecuacion = " + ".join(f"{coef}·I{idx+1}" for coef, idx in terminos)
    
    # Añadimos el lado derecho
    ecuacion += f" = {voltajes[i]}"
    
    print(f"Ecuación de Malla {i+1}: {ecuacion}")
