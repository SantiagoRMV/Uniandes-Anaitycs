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

from itertools import product
#Listas de características
genero = ['masculino', 'femenino', 'no binario', 'otro']
estrato = [1, 2, 3, 4, 5]
region = ['Region_1', 'Region_2', 'Region_3', 'Region_4', 'Region_5']

# Crear un diccionario con las listas disponibles
listas_disponibles = {'genero': genero, 'estrato': estrato, 'region': region}

# Ingresar el número de becas disponibles
N = int(input("Ingrese el número de becas disponibles: "))

# Ingresar el rango de edad
min_edad = int(input("Edad mínima factible: "))
max_edad = int(input("Edad máxima factible: "))

#Filtrando usuarios por rango de edad
usuarios_seleccionados = []

for i, usuario in enumerate(base_datos['edad']):
    if min_edad <= base_datos['edad'][i] <= max_edad:
        usuarios_seleccionados.append(base_datos['id'][i])

#TODO: Control de estudiantes que cumplen los rangos de edad
#if len(usuarios_seleccionados) == 0:
 #   print('No hay alumnos que cumplan con este rango de edad')
  #  break

#Diccionario de estudiantes que cumplen el rango de edad
alumno_id = []
alumno_edad = []
alumno_region = []
alumno_genero = []
alumno_estrato = []
alumno_promedio = []
estudiantes_preseleccionados = {'id': alumno_id, 'edad': alumno_edad ,'region': alumno_region, 'genero':alumno_genero, 'estrato':alumno_estrato, 'promedio': alumno_promedio}

for i, alumno in enumerate(base_datos['id']):
    if base_datos['id'][i] in usuarios_seleccionados:
        alumno_id.append(base_datos['id'][i])
        alumno_edad.append(base_datos['edad'][i])
        alumno_region.append(base_datos['region'][i])
        alumno_genero.append(base_datos['genero'][i])
        alumno_estrato.append(base_datos['estrato'][i])
        alumno_promedio.append(base_datos['promedio'][i])
        
# Obtener la longitud de los datos de una de las claves (todas deben tener la misma longitud)
num_registros = len(estudiantes_preseleccionados['id'])

# Crear una lista de diccionarios
lista_registros_estudiantes = []

# Iterar a través de los registros
for i in range(num_registros):
    registro = {}
    for clave, valores in estudiantes_preseleccionados.items():
        registro[clave] = valores[i]
    lista_registros_estudiantes.append(registro)


# Pedir al usuario que ingrese los nombres de las listas
caracteristicas = input("Ingrese los nombres de las listas separados por comas (por ejemplo, 'genero, estrato, region'): ").split(',')

# Filtrar las listas seleccionadas por el usuario
listas_seleccionadas = [listas_disponibles[caracteristica.strip()] for caracteristica in caracteristicas]

# Generar todas las combinaciones de elementos de las listas seleccionadas
combinaciones = list(product(*listas_seleccionadas))

#Diccionario de control de procentajes
porcentajes = {}
suma_porcentajes = 0

#Barrido de cada combinación
for combinacion in combinaciones:
    porcentaje = float(input(f'Ingrese el procentaje (valor entre 0 y 1) para {combinacion}: '))
    
    while porcentaje < 0  or porcentaje > 1:
        print("El porcentaje debe estar entre 0 y 1.")
        porcentaje = float(input(f'Ingrese el porcentaje (entre 0 y 1) para {combinacion}: '))
    
    porcentajes[combinacion] = porcentaje
    suma_porcentajes += porcentaje
    
    if suma_porcentajes >= 1:
        print('Ya no puedes incluir mas porcentajes ya que cumpliste con el tope maximo a asignar')
        break

#Guardando las tuplas de cada combinación en una lista
lista_tuplas = []
for key in porcentajes.keys():
    lista_tuplas.append(key)

variables_tuplas = len(lista_tuplas[0])
cantidad_tuplas = len(porcentajes)

variables_filtro = {}
for i in range(cantidad_tuplas):
    variables = []
    for y in range(variables_tuplas):
        tupla = f'tupla_{i}'
        variable = list(porcentajes.keys())[i][y]
        variables.append(variable)
    variables_filtro[tupla] = variables

# Filtrar estudiantes basado en las variables de filtro
estudiantes_filtrados = {}

for tupla in combinaciones:
    estudiantes_filtrados[tupla] = []  # Inicializa una lista vacía para cada tupla         

lista_porcentajes = []
for porcentaje in porcentajes.values():
    lista_porcentajes.append(porcentaje)


for tupla in combinaciones:
    tupla_id = []
    tupla_genero = []
    tupla_region = []
    tupla_estrato = []
    tupla_promedio = []    
    
    for i, estudiante in enumerate(estudiantes_preseleccionados):         
            if all(estudiantes_preseleccionados[caracteristica][i] == variable_tupla for caracteristica , variable_tupla in zip(caracteristicas, tupla)):
                tupla_id.append(estudiantes_preseleccionados['id'][i])
                tupla_genero.append(estudiantes_preseleccionados['genero'][i])
                tupla_region.append(estudiantes_preseleccionados['region'][i])
                tupla_estrato.append(estudiantes_preseleccionados['estrato'][i])
                tupla_promedio.append(estudiantes_preseleccionados['promedio'][i])
            
    estudiantes_tupla = {'id':tupla_id ,'genero':tupla_genero ,'region':tupla_region ,'estrato':tupla_estrato ,'promedio':tupla_promedio}
    estudiantes_filtrados[tupla].append(estudiantes_tupla)

#Reemplazando nombres tuplas
estudiantes_en_tupla = {}
for tupla in estudiantes_filtrados.keys():
    if tupla in lista_tuplas:
        estudiantes_en_tupla[tupla] = estudiantes_filtrados[tupla]
        
#Calculando cantidad de becas a entregar
lista_becas = []
for tupla, porcentaje_asignado in zip(lista_tuplas, lista_porcentajes):
    becas_asignadas = N * porcentaje_asignado
    lista_becas.append(becas_asignadas)
    
#Asignando becas
becas_asignadas_tupla = {}
for tupla, becas in zip(estudiantes_en_tupla.keys(), lista_becas):
    if len(estudiantes_en_tupla[tupla][0]['id']) > 0:
        becas_tupla = becas
    elif len(estudiantes_en_tupla[tupla][0]['id']) ==  0:
        becas_tupla = 0
    becas_asignadas_tupla[tupla] = becas_tupla
print('Becas asignadas:')
print(becas_asignadas_tupla)                