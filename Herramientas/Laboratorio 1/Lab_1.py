import math
import matplotlib.pyplot as plt

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

#Generador de diccionarios
def diccionarios(region_filtro,genero_filtro,diccionario):
    columna_filtrada_genero = []
    columna_filtrada_region= []
    columna_filtrada_promedio = []
    
    for i, valor in enumerate(diccionario['region']):
        if valor == region_filtro:
            columna_filtrada_genero.append(diccionario['genero'][i])
            columna_filtrada_region.append(diccionario['region'][i])
            columna_filtrada_promedio.append(diccionario['promedio'][i])
                
    diccionario_region = {'region':columna_filtrada_region, 'genero':columna_filtrada_genero, 'promedio':columna_filtrada_promedio}

    #Filtrando por genero masculino en la región 1
    columna_filtrada_genero = []
    columna_filtrada_region= []
    columna_filtrada_promedio = []

    for i, valor in enumerate(diccionario_region['genero']):
        if valor == genero_filtro:
            columna_filtrada_genero.append(diccionario_region['genero'][i])
            columna_filtrada_region.append(diccionario_region['region'][i])
            columna_filtrada_promedio.append(diccionario_region['promedio'][i])

        
    diccionario_region_genero = {'region':columna_filtrada_region, 'genero':columna_filtrada_genero, 'promedio':columna_filtrada_promedio}
    
    return diccionario_region_genero


#Filtrando por pormedios
def filtro_promedio(promedio,diccionario):
    columna_filtrada_genero = []
    columna_filtrada_region= []
    columna_filtrada_promedio = []
    
    for i, valor in enumerate(diccionario['promedio']):
        valor = float(valor)
        if valor >= promedio:
            columna_filtrada_genero.append(diccionario['genero'][i])
            columna_filtrada_region.append(diccionario['region'][i])
            columna_filtrada_promedio.append(diccionario['promedio'][i])

    diccionario_region_genero_promedio = {'region':columna_filtrada_region, 'genero':columna_filtrada_genero, 'promedio':columna_filtrada_promedio}
    
    return diccionario_region_genero_promedio

#Generador de proporciones
def calculo_proporciones(diccionario,base):
    proporcion = len(diccionario['genero'])/len(base['genero'])
    proporcion = round(proporcion, 2)
    return proporcion


#Asignando cantidad becas
def cantidad_becas(N,proporcion):
    cantidad_becas_proporcion = int(proporcion*N)
    return cantidad_becas_proporcion

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


#Asignando becas a estudiantes
def asignacion_becas(becas,region,genero,base):
    columna_filtrada_genero = []
    columna_filtrada_region= []
    columna_filtrada_promedio = []
    columna_filtrada_id = []
    #columna_filtrada_flag = []
    
    while becas >= 1:
        promedio = 5
        for i, filas in enumerate(base['genero']):
            if base['genero'][i]== genero and base['region'][i]==region and float(base['promedio'][i]) >= promedio:
                if base['flag'][i] == False:
                    columna_filtrada_genero.append(base['genero'][i])
                    columna_filtrada_region.append(base['region'][i])
                    columna_filtrada_promedio.append(base['promedio'][i])
                    columna_filtrada_id.append(base['id'][i])
                    base['flag'][i] = True
                becas -= 1
            if becas == 0:
                break
            promedio -= 0.1

            
    alumnos_becados = {'id':columna_filtrada_id, 'region':columna_filtrada_region, 'genero':columna_filtrada_genero, 'promedio':columna_filtrada_promedio}
    
    return alumnos_becados
    
    
###DEFINICIÒN DE VARIABLES

base_indexada = indexacion()

#Generando diccionarios por cada region y genero
#REGION 1 
df_region_1_masculino = diccionarios("Region_1","masculino",lectura_archivos())
df_region_1_femenino = diccionarios('Region_1', "femenino", lectura_archivos())
df_region_1_binario = diccionarios('Region_1', "no binario", lectura_archivos())
df_region_1_otro = diccionarios('Region_1', "otro", lectura_archivos())
#REGION 2
df_region_2_masculino = diccionarios("Region_2","masculino",lectura_archivos())
df_region_2_femenino = diccionarios('Region_2', "femenino", lectura_archivos())
df_region_2_binario = diccionarios('Region_2', "no binario", lectura_archivos())
df_region_2_otro = diccionarios('Region_2', "otro", lectura_archivos())
#REGION 3
df_region_3_masculino = diccionarios("Region_3","masculino",lectura_archivos())
df_region_3_femenino = diccionarios('Region_3', "femenino", lectura_archivos())
df_region_3_binario = diccionarios('Region_3', "no binario", lectura_archivos())
df_region_3_otro = diccionarios('Region_3', "otro", lectura_archivos())
#REGION 4
df_region_4_masculino = diccionarios("Region_4","masculino",lectura_archivos())
df_region_4_femenino = diccionarios('Region_4', "femenino", lectura_archivos())
df_region_4_binario = diccionarios('Region_4', "no binario", lectura_archivos())
df_region_4_otro = diccionarios('Region_4', "otro", lectura_archivos())
#REGION 5
df_region_5_masculino = diccionarios("Region_5","masculino",lectura_archivos())
df_region_5_femenino = diccionarios('Region_5', "femenino", lectura_archivos())
df_region_5_binario = diccionarios('Region_5', "no binario", lectura_archivos())
df_region_5_otro = diccionarios('Region_5', "otro", lectura_archivos())


#Calculando proporciones
#REGION 1 
prop_r1_masculino = calculo_proporciones(df_region_1_masculino, lectura_archivos())
prop_r1_femenino = calculo_proporciones(df_region_1_femenino, lectura_archivos())
prop_r1_binario = calculo_proporciones(df_region_1_binario, lectura_archivos())
prop_r1_otro = calculo_proporciones(df_region_1_otro, lectura_archivos())
#REGION 2 
prop_r2_masculino = calculo_proporciones(df_region_2_masculino, lectura_archivos())
prop_r2_femenino = calculo_proporciones(df_region_2_femenino, lectura_archivos())
prop_r2_binario = calculo_proporciones(df_region_2_binario, lectura_archivos())
prop_r2_otro = calculo_proporciones(df_region_2_otro, lectura_archivos())
#REGION 3
prop_r3_masculino = calculo_proporciones(df_region_3_masculino, lectura_archivos())
prop_r3_femenino = calculo_proporciones(df_region_3_femenino, lectura_archivos())
prop_r3_binario = calculo_proporciones(df_region_3_binario, lectura_archivos())
prop_r3_otro = calculo_proporciones(df_region_3_otro, lectura_archivos())
#REGION 4
prop_r4_masculino = calculo_proporciones(df_region_4_masculino, lectura_archivos())
prop_r4_femenino = calculo_proporciones(df_region_4_femenino, lectura_archivos())
prop_r4_binario = calculo_proporciones(df_region_4_binario, lectura_archivos())
prop_r4_otro = calculo_proporciones(df_region_4_otro, lectura_archivos())
#REGION 5
prop_r5_masculino = calculo_proporciones(df_region_5_masculino, lectura_archivos())
prop_r5_femenino = calculo_proporciones(df_region_5_femenino, lectura_archivos())
prop_r5_binario = calculo_proporciones(df_region_5_binario, lectura_archivos())
prop_r5_otro = calculo_proporciones(df_region_5_otro, lectura_archivos())

N = 100

#Asignando becas
becas_r1_masculino = cantidad_becas(N, prop_r1_masculino)
becas_r1_femenino = cantidad_becas(N, prop_r1_femenino)
becas_r1_binario = cantidad_becas(N, prop_r1_binario)
becas_r1_otro = cantidad_becas(N, prop_r1_otro)

becas_r2_masculino = cantidad_becas(N, prop_r2_masculino)
becas_r2_femenino = cantidad_becas(N, prop_r2_femenino)
becas_r2_binario = cantidad_becas(N, prop_r2_binario)
becas_r2_otro = cantidad_becas(N, prop_r2_otro)

becas_r3_masculino = cantidad_becas(N, prop_r3_masculino)
becas_r3_femenino = cantidad_becas(N, prop_r3_femenino)
becas_r3_binario = cantidad_becas(N, prop_r3_binario)
becas_r3_otro = cantidad_becas(N, prop_r3_otro)

becas_r4_masculino = cantidad_becas(N, prop_r4_masculino)
becas_r4_femenino = cantidad_becas(N, prop_r4_femenino)
becas_r4_binario = cantidad_becas(N, prop_r4_binario)
becas_r4_otro = cantidad_becas(N, prop_r4_otro)

becas_r5_masculino = cantidad_becas(N, prop_r5_masculino)
becas_r5_femenino = cantidad_becas(N, prop_r5_femenino)
becas_r5_binario = cantidad_becas(N, prop_r5_binario)
becas_r5_otro = cantidad_becas(N, prop_r5_otro)


#Calculo de las becas distribuidas correctamente
lista_becas_asignadas = [becas_r1_masculino,
                         becas_r1_femenino,
                         becas_r1_binario,
                         becas_r1_otro,
                         becas_r2_masculino,
                         becas_r2_femenino,
                         becas_r2_binario,
                         becas_r2_otro,
                         becas_r3_masculino,
                         becas_r3_femenino,
                         becas_r3_binario,
                         becas_r3_otro,
                         becas_r4_masculino,
                         becas_r4_femenino,
                         becas_r4_binario,
                         becas_r4_otro,
                         becas_r5_masculino,
                         becas_r5_femenino,
                         becas_r5_binario,
                         becas_r5_otro]

total_becas = sum(lista_becas_asignadas)


#Asignación de becas
asignacion_becas_r1_masculino = asignacion_becas(becas_r1_masculino, 'Region_1', 'masculino', base_indexada)
asignacion_becas_r1_femenino = asignacion_becas(becas_r1_femenino, 'Region_1', 'femenino', base_indexada)
asignacion_becas_r1_binario = asignacion_becas(becas_r1_binario, 'Region_1', 'no binario', base_indexada)
asignacion_becas_r1_otro = asignacion_becas(becas_r1_otro, 'Region_1', 'otro', base_indexada)

asignacion_becas_r2_masculino = asignacion_becas(becas_r2_masculino, 'Region_2', 'masculino', base_indexada)
asignacion_becas_r2_femenino = asignacion_becas(becas_r2_femenino, 'Region_2', 'femenino', base_indexada)
asignacion_becas_r2_binario = asignacion_becas(becas_r2_binario, 'Region_2', 'no binario', base_indexada)
asignacion_becas_r2_otro = asignacion_becas(becas_r2_otro, 'Region_2', 'otro', base_indexada)

asignacion_becas_r3_masculino = asignacion_becas(becas_r3_masculino, 'Region_3', 'masculino', base_indexada)
asignacion_becas_r3_femenino = asignacion_becas(becas_r3_femenino, 'Region_3', 'femenino', base_indexada)
asignacion_becas_r3_binario = asignacion_becas(becas_r3_binario, 'Region_3', 'no binario', base_indexada)
asignacion_becas_r3_otro = asignacion_becas(becas_r3_otro, 'Region_3', 'otro', base_indexada)

asignacion_becas_r4_masculino = asignacion_becas(becas_r4_masculino, 'Region_4', 'masculino', base_indexada)
asignacion_becas_r4_femenino = asignacion_becas(becas_r4_femenino, 'Region_4', 'femenino', base_indexada)
asignacion_becas_r4_binario = asignacion_becas(becas_r4_binario, 'Region_4', 'no binario', base_indexada)
asignacion_becas_r4_otro = asignacion_becas(becas_r4_otro, 'Region_4', 'otro', base_indexada)

asignacion_becas_r5_masculino = asignacion_becas(becas_r5_masculino, 'Region_5', 'masculino', base_indexada)
asignacion_becas_r5_femenino = asignacion_becas(becas_r5_femenino, 'Region_5', 'femenino', base_indexada)
asignacion_becas_r5_binario = asignacion_becas(becas_r5_binario, 'Region_5', 'no binario', base_indexada)
asignacion_becas_r5_otro = asignacion_becas(becas_r5_otro, 'Region_5', 'otro', base_indexada)


becas_entregadas = base_indexada['flag'].count(True)























