def media(lista):
  if len(lista) == 0:
    return 0
  return sum(lista) / len(lista)


def mediana(lista):
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
  if len(lista) == 0:
    return []

  frecuencias = {}
  for num in lista:
    frecuencias[num] = frecuencias.get(unm, 0) +1

  max_freq = max(frecuencias.values())
  modas = [num for num, freq in frecuencias.items() if freq == max_freq]

  return modas

def varianza(lista, poblacional=True):
  if len(lista) < 2:
    return 0

  prom = media(lista)
  suma_cuadrados = sum((x - prom) ** 2 for x in lista)
  n = len(lista)
  divisor =n if poblacional else n - 1

  return suma_cuadrados / divisor

def desviacion_estandar(lista, poblacional=True):
  return varianza(lista, poblacional) ** 0.5

def rango(lista):
  if len(lista) == 0:
    return 0
  return max(lista) - min(lista)


