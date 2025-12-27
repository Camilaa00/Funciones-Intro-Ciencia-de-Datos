import math

# MEDIDAS DE TENDENCIA CENTRAL:
#-----------------------------
def promedio(lista):
  """
  La función 'promedio' calcula el promedio de una lista de números.
  Parámetros
  -------------
  lista: lista (argumento de entrada de la función)

  Qué retorna?
  --------------
  Promedio: float (promedio de los números de la lista)
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
  lista: lista de entrada. (números)

  Qué retorna?
  --------------
  mediana: float (mediana de los números de la lista)
  """
  
  if len(lista) == 0:
    return 0

  lista_orenada = sorted(lista)
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
  lista: lista de números (int o float)

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
  lista: lista de números
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
  lista: lista de números.
  tipo: string (es opcional. Tipo de varianza: "poblacional" o "muestral")

  Qué retorna?
  --------------
  Desviación estándar: float
  """
  return math.sqrt(varianza(lista, tipo))

def frecuencias(lista):
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
  



