import math

# MEDIDAS DE TENDENCIA CENTRAL:
#-----------------------------
def promedio(lista):
  """
  La función 'promedio' calcula el promedio de una lista de números.
  Parámetros
  -------------
  lista: [list] 

  Qué retorna?
  --------------
  Promedio: [float]
    (Promedio de los números de la lista) 
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
  lista: [list]
    (lista de entrada)

  Qué retorna?
  --------------
  mediana: [float] 
    (mediana de los números de la lista)
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
  lista: [cualquier tipo de dato]
    (Lista de entrada)

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
  lista: [list]
    (lista de números)
  Qué retorna?
  --------------
  rango: [float]
  """
  if len(lista) == 0:
    return 0
  return max(lista) - min(lista)


def varianza(lista, tipo="poblacional"):
  """
  La función 'varianza' calcula la varianza de una lista de números.

  Parámeteros:
  -----------------
  lista: [list]
    (lista de números)
  tipo: string (es opcional. Tipo de varianza: "poblacional" o "muestral")

  Qué retorna?
  --------------
  varianza: [float]
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
  lista: [list]
    (lista de números)
  tipo: string (es opcional. Tipo de varianza: "poblacional" o "muestral")

  Qué retorna?
  --------------
  Desviación estándar: [float]
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
  lista: [list]
    (Lista de valores numéricos)

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
  lista: [list]
    (Lista de valores numéricos)

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
  lista: [list]
    (Lista de valores numéricos)

  Qué retorna?
  -------------
  float
      MAD
  """
  med = mediana(lista)
  std_abs = [abs(i - med) for i in lista]
  return mediana(std_abs)

    
def percentil(p, lista):
  """
  Calcula el percentil p (0-100) de una lista de valores.
    
  Parámetros:
  -----------
  p : [float]
      (Percentil deseado (0 a 100))
  lista : [list]
      (Lista de valores numéricos)
        
  Retorna:
  --------
  float
      Valor del percentil.
  """
  lista_ordenada = sorted(lista)
  n = len(lista_ordenada)
    
  # Casos especiales
  if p <= 0:
      return lista_ordenada[0]
  if p >= 100:
      return lista_ordenada[-1]
  
  k = (p / 100) * (n - 1)
  f = int(k)          
  c = k - f           
    
  if (f + 1) < n:
      return lista_ordenada[f] + c * (lista_ordenada[f + 1] - lista_ordenada[f])
  else:
      return lista_ordenada[f]

def correlacion(x, y):
  """
  Calcula el coeficiente de correlación entre dos variables.

  Parámetros:
  ------------
  x : list[float]
      Primera variable (lista de valores numéricos).
  y : list[float]
      Segunda variable (lista de valores numéricos).
      Debe tener la misma longitud que x.

  Qué retorna?
  -------------
  float or None
      - Coeficiente de correlación de Pearson (entre -1 y 1).
      - 0 si alguna variable tiene varianza cero (todos los valores iguales).
      - None si las listas tienen longitudes diferentes.
  """
  if len(x) != len(y):
    return None

  n = len(x)

  promedio_x = sum(x) / n
  promedio_y = sum(y) / n

  numerador = 0.0
  for i in range(n):
    numerador += (x[i] - promedio_x) * (y[i] - promedio_y)

  varianza_x = sum((xi - promedio_x) ** 2 for xi in x) / n
  varianza_y = sum((yi - promedio_y) ** 2 for yi in y) / n

  if varianza_x == 0 or varianza_y == 0:
    return 0

  desviacion_x = varianza_x ** 0.5
  desviacion_y = varianza_y ** 0.5

  denominador = desviacion_x * desviacion_y

  if denominador == 0:
    return 0

  return numerador / (n * denominador)

def covarianza(x, y):
  """
  Calcula la covarianza entre dos variables.

  Parámetros:
  ------------
  x : list[float]
      Primera variable (lista de valores numéricos).
  y : list[float]
      Segunda variable (lista de valores numéricos).
      Debe tener la misma longitud que x.
        
  Retorna:
  --------
  float
      Covarianza entre x e y.  
  """
   
  if len(x) != len(y):
    raise ValueError("Las listas x e y deben tener la misma longitud")
    
  n = len(x)
  
  promedio_x = sum(x) / n
  promedio_y = sum(y) / n
    

  suma_productos = 0
  for i in range(n):
      suma_productos += (x[i] - promedio_x) * (y[i] - promedio_y)
    
  return suma_productos / n


