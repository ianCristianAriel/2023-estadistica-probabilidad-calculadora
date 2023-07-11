import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import poisson


#1 Probabilidad elemental:
def espacio_muestral(espacio):
    return espacio

def evento(espacio, seleccion):
    if seleccion in espacio:
        evento = seleccion
    return evento

def probabilidad(evento, espacio):
    probabilidad = evento / espacio
    return probabilidad

#2 probabilidad_condicional:
def probabilidad_condicional(probabilidad, probabilidad2):
    probabilidad_condicional = probabilidad / probabilidad2
    return probabilidad_condicional
    
#teoria_probabilidad:
def reglas(union, interseccion):
    if union == True:
        return union
    if interseccion == True:
        return interseccion

#distribuciones
def dist_discreta(eventos=[], probabilidades=[]):
    cum_probabilidades = np.cumsum(probabilidades)
    return eventos, cum_probabilidades
    
def dist_continua(media, desviacion_estandar, limite_inferior, limite_superior):
    x = np.linspace(limite_inferior, limite_superior, 100)
    y = norm.cdf(x, media, desviacion_estandar)
    return x, y

def dist_multinomial(valores, probabilidades):
    cum_probabilidades = np.cumsum(probabilidades)
    return valores, cum_probabilidades
    
def dist_hipergeométrica(poblacion_total, exitos_en_poblacion, tam_muestra):
    x = np.arange(0, tam_muestra+1)
    pmf = hypergeom.pmf(x, poblacion_total, exitos_en_poblacion, tam_muestra)
    cdf = np.cumsum(pmf)
    return x, cdf
    
def dist_poisson(lambda_param, limite_superior):
    x = np.arange(0, limite_superior+1)
    pmf = poisson.pmf(x, lambda_param)
    cdf = np.cumsum(pmf)
    return x, cdf

    
def dist_prob_conjunta(datos):
    valores = np.unique(datos)
    distribucion = []
    for valor in valores:
        probabilidad = np.mean(datos == valor)
        distribucion.append(probabilidad)
    return valores, distribucion

#Teorema de Bayes:
def teorema_bayes(probabilidad_a, probabilidad_b_dado_a, probabilidad_b):
    # Calculamos la probabilidad de A dado B utilizando el teorema de Bayes
    probabilidad_a_dado_b = (probabilidad_b_dado_a * probabilidad_a) / probabilidad_b
    return probabilidad_a_dado_b

def probabilidad_condicional_inversa(probabilidad_a_dado_b, probabilidad_b, probabilidad_a):
    # Calculamos la probabilidad de B dado A utilizando el teorema de Bayes
    probabilidad_b_dado_a = (probabilidad_a_dado_b * probabilidad_b) / probabilidad_a
    return probabilidad_b_dado_a

