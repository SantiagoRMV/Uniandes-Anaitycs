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
        
    diccionario['edad'] = [int(edad) for edad in diccionario['edad']]
    diccionario['estrato'] = [int(estrato) for estrato in diccionario['estrato']]
    diccionario['promedio'] = [float(promedio) for promedio in diccionario['promedio']]

    ids = []
    flags = []
    #Asignando Id a cada estudiante
    for i in range(len(diccionario['genero'])):
        ids.append(i)
        flags.append(False)
            
    diccionario['id'] = ids
    diccionario['flag'] = flags

    llaves_ordenadas = ['id','edad','escolaridad','estado_civil','estrato','genero','promedio', 'region','flag']
    diccionario = {llave: diccionario[llave] for llave in llaves_ordenadas}
    
    return diccionario

base_datos = lectura_archivos()

def becas_estrato(base, becas):
    resultados_estrato = {}
    estratos = [1,2,3,4,5]
    
    #Generando tuplas con los datos de cada estrato, promedio
    for estrato in estratos:
        columna_filtrada_estrato = []
        columna_filtrada_promedio = []
        variable = f'estrato_{estrato}'
        for i, valor in enumerate(base['estrato']):
            if valor == estrato:
                columna_filtrada_estrato.append(base['estrato'][i])
                columna_filtrada_promedio.append(base['promedio'][i])
                resultados_estrato[variable] = (columna_filtrada_estrato, columna_filtrada_promedio)
    
    
    #Ordenando los datos de forma ascendente
    resultados_ordenado = {}
    
    for key, value in resultados_estrato.items():
        estratos, promedios = value
        estratos, promedios = zip(*sorted(zip(estratos, promedios), key=lambda x: x[1]))
        resultados_ordenado[key] = (list(estratos), list(promedios))
    
    
    #Calculando el percentil 98
    percentiles = {}
    
    for key, (estratos, promedios) in resultados_ordenado.items():
        # Calcula el índice correspondiente al percentil 98
        indice = int(len(promedios) * 0.98)
        # Obtiene el valor del percentil 98
        valor_percentil = promedios[indice]
        percentiles[key] = valor_percentil
     
        
    #Asignando becas a cada estrato
    becas_asignadas = {}
    estratos = [1,2,3,4,5]   
    i=1
    while becas > 0:        
        for estrato in estratos:
            columna_id_alumno = []
            columna_estrato_alumno = []
            columna_promedio_alumno = []
            promedio = percentiles[f'estrato_{estrato}']

            for (id_alumno,estrato_alumno,promedio_alumno,flag_alumno) in zip(base['id'],base['estrato'],base['promedio'],base['flag']):
                if estrato_alumno == estrato and promedio_alumno >= promedio and flag_alumno == False:
                    columna_id_alumno.append(id_alumno)
                    columna_estrato_alumno.append(estrato_alumno)
                    columna_promedio_alumno.append(promedio_alumno)
                    flag_alumno = True
                    becas -= 1
                    becas_asignadas[f'estrato_{estrato}_ciclo_{i}'] = {'id': columna_id_alumno, 'estrato':columna_estrato_alumno, 'promedio':columna_promedio_alumno}

                if becas == 0:
                    break

        if becas > 0:
            for clave, valor in percentiles.items():
                percentiles[clave] = valor - 0.1
        i += 1

    # Diccionario resultante
    diccionario_agrupado = {}

    # Recorre el diccionario original
    for clave, valor in becas_asignadas.items():
        # Extrae el estrato de la clave
        estrato = clave.split('_')[1]

        # Combina los datos en el diccionario agrupado
        if estrato in diccionario_agrupado:
            for dato in valor:
                diccionario_agrupado[estrato][dato].extend(valor[dato])
        else:
            diccionario_agrupado[estrato] = valor
    
    return diccionario_agrupado

asignacion_becas = becas_estrato(base_datos, 60)