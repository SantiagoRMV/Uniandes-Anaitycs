#Generando la base de datos
def lectura_archivos():
    #Creando listas de archivos
    archivos = ['edad','escolaridad','estado_civil','estrato','genero','promedio','region']
    rutas = []
    #Generando las rutas 
    for archivo in archivos:
        ruta_archivo = f'./Archivos/{archivo}.txt'
        rutas.append(ruta_archivo) 
    #Creando el diccionario para almacenar la información
    diccionario = {}
    #Ciclo para almacenar la información de los archivos en el diccionario
    for ruta in rutas:
        with open(ruta, 'r') as file:
            datos = []
            for linea in file:
                linea = linea[:-1]
                datos.append(linea)
        ruta = ruta[11:-4]
        diccionario[ruta] = datos
        
    return diccionario

#Asignando Id estudiante
def indexacion():
    base_datos = lectura_archivos()
    ids = []
    flags = []
    #Asignando Id a cada estudiante
    for i in range(len(base_datos['genero'])):
        ids.append(i)
        flags.append(False)
    
    base_datos['id'] = ids
    base_datos['flag'] = flags
    return base_datos

base = indexacion()

#Filtro por estrato
def poblacion_estrato(base, estrato):
    columna_filtrada_estrato = []
    columna_filtrada_promedio = []
    
    for i, valor in enumerate(base['estrato']):
        if valor == estrato:
            columna_filtrada_estrato.append(base['estrato'][i])
            columna_filtrada_promedio.append(base['promedio'][i])

    diccionario_estrato_promedio = {'estrato':columna_filtrada_estrato,'promedio':columna_filtrada_promedio}
    
    return diccionario_estrato_promedio

#Calculando percentiles por estrato
def proporciones_promedios(diccionario, percentil):
    #Convirtiendo los datos a numeros
    for i, estrato in enumerate(diccionario['promedio']):
        float(diccionario['promedio'][i])
    #Ordenando los datos de mayor a menor
    valores_ordenados = sorted(diccionario['promedio'], reverse=False)
    #Calculando los perdencitles
    indice = int(percentil*len(diccionario['promedio']))
    valor_percentil = valores_ordenados[indice]
    return valor_percentil
    
#Asignando becas
def asignar_beca(diccionario, promedios, becas):
    columna_filtrada_id = []
    columna_filtrada_estrato = []
    columna_filtrada_promedio = []
    estratos = ['1','2','3','4','5']
    y = 0
    
    while becas >= 1:
        for estrato in estratos:
            promedio = promedios[y]
            print(f'empezando ciclo de estrato {estrato}')
            print(promedio)
            for i, estrato_alumno in enumerate(diccionario['estrato']):
                if int(diccionario['estrato'][i]) == int(estrato):
                    print(diccionario['estrato'][i])
                    if float(diccionario['promedio'][i]) >= float(promedio) and diccionario['flag'][i] == False:
                        columna_filtrada_id.append(diccionario['id'][i])
                        columna_filtrada_estrato.append(diccionario['estrato'][i])
                        columna_filtrada_promedio.append(diccionario['promedio'][i])
                        base['flag'][i] = True
                        print('Alumno becado')
                    becas -= 1
                    
                if becas == 0:
                    break
            y += 1
    
    alumnos_becados = {'id':columna_filtrada_id, 'estrato':columna_filtrada_estrato, 'promedio':columna_filtrada_promedio}
    return alumnos_becados
                    
                

#Generando diccionarios por estrato
promedios_estrato_1 = poblacion_estrato(base, '1')
promedios_estrato_2 = poblacion_estrato(base, '2')
promedios_estrato_3 = poblacion_estrato(base, '3')
promedios_estrato_4 = poblacion_estrato(base, '4')
promedios_estrato_5 = poblacion_estrato(base, '5')

#Generando calificacion minima 2% mejor
percentil = 0.98
mejores_estrato_1 = proporciones_promedios(promedios_estrato_1,percentil)
mejores_estrato_2 = proporciones_promedios(promedios_estrato_2,percentil)
mejores_estrato_3 = proporciones_promedios(promedios_estrato_3,percentil)
mejores_estrato_4 = proporciones_promedios(promedios_estrato_4,percentil)
mejores_estrato_5 = proporciones_promedios(promedios_estrato_5,percentil)
promedios_estrato = [mejores_estrato_1,mejores_estrato_2,mejores_estrato_3,mejores_estrato_4,mejores_estrato_5]

#Asignando becas
N = 100
becados = asignar_beca(base, promedios_estrato, N)

