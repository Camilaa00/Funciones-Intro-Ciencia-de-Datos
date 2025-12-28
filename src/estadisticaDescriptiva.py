import math

# MEDIDAS DE TENDENCIA CENTRAL:
#-----------------------------
def promedio(lista):
  """
  La función 'promedio' calcula el promedio de una lista de números.
  Parámetros
  -------------
  lista: lista 

  Qué retorna?
  --------------
  Promedio: promedio de los números de la lista [float]
  """
  nueva_lista = []
  for i in lista:
    if math.isfinite(i):
      nueva_lista.append(i)
  return sum(nueva_lista)/len(nueva_lista)


def mediana(lista):
  """
  La función 'mediana' calcula la mediana de una lista de números.

  Parámetros:
  --------------
  lista: lista de entrada. [list]

  Qué retorna?
  --------------
  mediana: float (mediana de los números de la lista)
  """
  
  if len(lista) == 0:
    return 0

  lista_ordenada = sorted(lista)
  n = len(lista_ordenada)

  if n % 2 == 1:
    return lista_ordenada[n // 2]
  else:
    medio1 = lista_ordenada[n // 2 - 1]
    medio2 = lista_ordenada[n // 2]
    return (medio1 + medio2) / 2

def moda(lista):
  """
  La función 'moda' calcula la moda de una lista de entrada.

  Parámetros:
  --------------
  lista: lista de entrada (cualquier tipo de dato)

  Qué retorna?
  --------------
  moda: int, float, string, etc. (depende del tipo de dato que conforme la lista)
  """
  if len(lista) == 0:
    return []

  frecuencias = {}
  for num in lista:
    frecuencias[num] = frecuencias.get(num, 0) +1

  max_freq = max(frecuencias.values())
  modas = [num for num, freq in frecuencias.items() if freq == max_freq]

  return modas

# MEDIDAS DE DISPERSIÓN:
#-------------------------------
def rango(lista):
  """
  La función 'rango' calcula el rango de una lista de números.

  Parámetros:
  --------------
  lista: lista de números [list]

  Qué retorna?
  --------------
  rango: float
  """
  if len(lista) == 0:
    return 0
  return max(lista) - min(lista)


def varianza(lista, tipo="poblacional"):
  """
  La función 'varianza' calcula la varianza de una lista de números.

  Parámeteros:
  -----------------
  lista: lista de números [list]
  tipo: string (es opcional. Tipo de varianza: "poblacional" o "muestral")

  Qué retorna?
  --------------
  varianza: float
  """
  if len(lista) < 2:
    return 0

  prom = promedio(lista)
  suma_cuadrados = sum((x - prom) ** 2 for x in lista)
  n = len(lista)

  if tipo == "muestral" and n > 1:
    return suma_cuadrados / (n - 1)
  else:
    return suma_cuadrados / n


def desviacion_estandar(lista, tipo="poblacional"):
  """
  La función 'desviacion_estandar' calcula la desviación estándar de una lista de números.

  Parámetros:
  --------------
  lista: lista de números. [list]
  tipo: string (es opcional. Tipo de varianza: "poblacional" o "muestral")

  Qué retorna?
  --------------
  Desviación estándar: float
  """
  return math.sqrt(varianza(lista, tipo))

def frecuencia(lista):
  """
  La función 'frecuencias' calcula la frecuencia de los datos de la lista.

  Parámetros
  -------------
  lista: todo tipo de dato.

  Qué retorna?
  -------------
  frecuencia: todo tipo de dato (frecuencia de los datos de la lista)
  """
  frecuencias = {}
  for i in lista:
    frecuencias[i] = frecuencias.get(i, 0) + 1
  return frecuencias

def cuartiles(lista):
  """
  La función 'cuartiles' calcula los cuartiles Q1, Q2 (mediana) y Q3 de una lista de números. 
  También elimina valores NaN e infinitos.

  Parámetros:
  ------------
  lista: list
    Lista de valores numéricos.

  Qué retorna?
  ----------------
  tuple
      (Q1, Q2, Q3)
  """
  num_ordenados = sorted(lista)
  n = len(num_ordenados)

Q2 = mediana(num_ordenados)

# Cuartil 1:
if n % 2 == 0:
  mitad_inferior = num_ordenados[:n // 2]
else:
  mitad_inferior = num_ordenados[:n // 2]

Q1 = mediana(mitad_inferior)

# Cuartil 3:
if n % 2 == 0:
  mitad_superior = num_ordenados[n//2:]
else:
  mitad_superior = num_ordenados[n//2+1:]
  Q3 = mediana(mitad_superior)
    
    return Q1, Q2, Q3

def rango_intercuartilico(lista):
  """
  Esta función calcula el rango intercuartílico (IQR = Q3 - Q1).

  Parámetros:
  -------------
  lista: list
    Lista de valores numéricos.

  Qué retorna?
  -------------
  float
      IQR
  """
  Q1, _, Q3 = cuartiles(lista)
  return Q3 - Q1

def mediana_desv_abs(lista):
  """
  Esta función calcula la Mediana de las Desviaciones Absolutas.

  Parámetros:
  -------------
  lista: list
    Lista de valores numéricos.

  Qué retorna?
  -------------
  float
      MAD
  """
  med = mediana(lista)
  std_abs = [abs(x - med) for i in lista]
  return mediana(std_abs)


  



