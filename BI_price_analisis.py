
from Conn_CC_HLTC import CryptoConector
import numpy as np
import pandas as pd
import pdb
import matplotlib.pyplot as plt
from markov_matrix import Markov_X

# ANALISIS DE TIEMPOS https://www.youtube.com/watch?v=A9c7hGXQ5A8


def rendDia(intervalo_tiempo, token, fiat):
    df = CryptoConector(intervalo_tiempo, token, fiat)
    hltc = df.precioDia()
    # CAMBIA EL INDICE DEL PANDA AL CAMPO TIME
    hltc.set_index('time', inplace=True)
    #
    # # BOTA LAS COLUMNAS DE VOLUMENES
    # hltc.drop(['volumeto', 'volumefrom'], axis=1, inplace=True)
    #
    # # OBTENGO LAS MEDIAS PARA CADA DIA PROMEDIANDO LA MAXIMA, LA MINIMA,  APE
    # # RTURA Y PRECIO DE CIERRE PARA CADA RANGO DE TIEMPO ESTO EN EL EJE HORIZ
    # hltc = hltc.mean(axis=1, skipna=True)
    #
    # # TRANSFORMA EL PANDA --> NUMPY CON LA FUNCION values
    # # MATRIZ UNIDIMENCIONAL DE 1 X N
    # hltc = hltc.values
    #
    # # SE CALCULA EL RENDIMIENTO CORTANDO LOS NUMPY COMO SI FUERAN STRINGS SE
    # # SU DIMENCION EN UNO
    # rend = (hltc[1:]-hltc[:-1])/hltc[1:]
    # np.set_printoptions(precision=5, suppress=True,)
    return hltc

# %% print
print(rendDia(100, 'BTC', 'USD'))

nano = Markov_X('hora', 100, 'ETH', 'USD')
print('Matriz S')
print(nano.matriz_S())
print('Matriz P')
print(nano.matriz_P())

# x = rendDia(100, 'ETH', 'USD')
# x.index
# x['2019-03-27':'2019-04-02']
# # type(x.time[0]) AL MES
# # RESAMPLE
#
# x.close.resample('W').mean().plot(kind="bar")
