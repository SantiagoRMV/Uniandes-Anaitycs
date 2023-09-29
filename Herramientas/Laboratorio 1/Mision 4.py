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


def asignacion_becas_subpoblacion(region,genero,becas,base):
    columna_filtrada_id = []
    columna_filtrada_region = []
    columna_filtrada_genero= []
    base_subpoblacion = {'id': columna_filtrada_id, 'region':columna_filtrada_region, 'genero':columna_filtrada_genero}
    
    #Generando los filtros para el diccionario base_filtrada
    for i, (region_estudiante, genero_estudiante) in enumerate(zip(base['region'], base['genero'])):
        if region_estudiante == region and genero_estudiante == genero:
            columna_filtrada_id.append(base['id'][i])
            columna_filtrada_region.append(region_estudiante)
            columna_filtrada_genero.append(genero_estudiante)
    
    #Calculando proporcion para la subpoblacion
    proporcion = len(base_subpoblacion['genero']) / len(base['genero'])
    proporcion = round(proporcion, 2)
    
    #Calculando la cantidad de becas para la subploblacion
    cantidad_becas_subpoblacion = int(proporcion * becas)
    
    #Asignando becas a la subpoblacion
    beca_filtrada_id = []
    beca_filtrada_region = []
    beca_filtrada_genero= []
    beca_filtrada_promedio = []
    mejor_promedio = 5.0
    for i, (region_estudiante, genero_estudiante, promedio_estudiante) in enumerate(zip(base['region'], base['genero'], base['promedio'])):
        #Control de becas disponibles
        if cantidad_becas_subpoblacion == 0:
            break
            
        if region_estudiante == region and genero_estudiante == genero and promedio_estudiante >= mejor_promedio:
            beca_filtrada_id.append(base['id'][i])
            beca_filtrada_region.append(region_estudiante)
            beca_filtrada_genero.append(genero_estudiante)
            beca_filtrada_promedio.append(promedio_estudiante)
            cantidad_becas_subpoblacion -= 1
        #Ajustando el promedio
        mejor_promedio -= 0.1
            
    alumnos_becados = {'id': beca_filtrada_id, 'region':beca_filtrada_region, 'genero':beca_filtrada_genero, 'promedio':beca_filtrada_promedio}
    return alumnos_becados
    
n_becas = 100
combos = [('Region_1','masculino'),('Region_1','femenino'),('Region_1','otro'),('Region_1','no binario'),
          ('Region_2','masculino'),('Region_2','femenino'),('Region_2','otro'),('Region_2','no binario'),
          ('Region_3','masculino'),('Region_3','femenino'),('Region_3','otro'),('Region_3','no binario'),
          ('Region_4','masculino'),('Region_4','femenino'),('Region_4','otro'),('Region_4','no binario'),
          ('Region_5','masculino'),('Region_5','femenino'),('Region_5','otro'),('Region_5','no binario')]

#Diccionario para alamacenar cada ejecución
resultados_becas = {}

for region, genero in combos:
    variable = f'{region}_{genero}'
    resultados_becas[variable] = asignacion_becas_subpoblacion(region, genero, n_becas, base_datos)
    
resultados_becas