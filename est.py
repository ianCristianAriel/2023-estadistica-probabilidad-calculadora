#ESTADISTICA
#importacion de librerias
import numpy as np
import pandas as pd
from scipy.stats import t
from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import f
from scipy.stats import pearsonr

# estadística_descriptiva:
def media(datos):
    media = np.mean(datos)
    return media
    
def mediana(datos):
    mediana = np.median(datos)
    return mediana

#medidas_dispersión
def desviacion_estandar(datos):
    desviacion_estandar = np.std(datos)
    return desviacion_estandar

def varianza(datos):
    media = np.mean(datos)
    varianza = np.mean((datos - media)**2)
    return varianza

def rango(datos):
    rango = max(datos) - min(datos)
    return rango

#Distribuciones estadísticas:
def distribucion_normal(media, desviacion_estandar, x):
    distribucion = norm.pdf(x, loc=media, scale=desviacion_estandar)
    return distribucion

def distribucion_t_student(grados_libertad, x):
    distribucion = t.pdf(x, df=grados_libertad)
    return distribucion

def distribucion_chi_cuadrado(grados_libertad, x):
    distribucion = chi2.pdf(x, df=grados_libertad)
    return distribucion

def distribucion_fisher(grados_libertad1, grados_libertad2, x):
    distribucion = f.pdf(x, dfn=grados_libertad1, dfd=grados_libertad2)
    return distribucion
    
#regresión:
def regresión_lineal():
    # Crear el modelo de regresión lineal
    modelo = LinearRegression()
    # Entrenar el modelo
    modelo.fit(x, y)
    # Obtener los coeficientes del modelo
    coeficiente_intercepto = modelo.intercept_
    coeficientes_pendiente = modelo.coef_
    return coeficiente_intercepto, coeficientes_pendiente

def coeficiente_correlación(x,y):
    # Cálculo del coeficiente de correlación utilizando scipy
    coef_correlacion, p_valor = pearsonr(x, y)
    
#Muestreo:
def muestreo_aleatorio_simple(poblacion, tamaño_muestra):
    muestra = np.random.choice(poblacion, size=tamano_muestra, replace=False)
