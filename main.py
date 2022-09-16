from typing import Union
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# --------- Año con mas carreras ------------
@app.get("/anyo")

def anyo():
    df_races=pd.read_csv('Datasets/races.csv')
    df_races_anyos=df_races.groupby(['year']).count()
    anio = df_races_anyos['raceId'].idxmax()
    
    return str(anio)

# --------- Piloto mas ganador ------------
@app.get("/masGanador")

def mas_ganador():
    df_resultados=pd.read_json('Datasets/results_formateado.json')
    primeros = df_resultados['position'] == 1
    df_primeros = df_resultados[primeros].groupby(['driverId']).count()

    masGanador = df_primeros['position'].idxmax()

    df_pilotos=pd.read_json('Datasets/drivers_formateado.json')
    piloto=df_pilotos.loc[masGanador]
    nombre,apellido = piloto['name'].values()
    nya = nombre +" "+apellido

    return (nya)


# --------- Circuito mas corrido ------------
@app.get("/circuitoMasCorrido")

def circuito_mas_corrido():
    df_carreras=pd.read_csv('Datasets/races.csv')
    circuitos = df_carreras.groupby(['circuitId']).count()
    masCorrido = circuitos['raceId'].idxmax()

    df_circuitos=pd.read_csv('Datasets/circuits.csv')
    circuito=df_circuitos.loc[masCorrido]
    
    return circuito['name']


# ---- Pilotos con mas puntos de escuderia American/British ----

@app.get("/pilotoEscuderia")
def piloto_escuderia():
    df_constructores = pd.read_json('Datasets/constructors_formateado.json')
    nacionalidad = (df_constructores.nationality == 'American') | (df_constructores.nationality == 'British')
    df_escuderiasAM = df_constructores.loc[nacionalidad]

    escuderia = df_escuderiasAM.constructorId   #Id escuderias American y british

    df_pilotos2 = pd.read_json('Datasets/results_formateado.json')
    df_pilotos3 = df_pilotos2.loc[escuderia]

    piloto4 = df_pilotos3.groupby(['driverId']).sum()
    piloto4Id = piloto4['points'].idxmax()

    df_drivers = pd.read_json('Datasets/drivers_formateado.json')
    pilotoPuntos=df_drivers.loc[piloto4Id]
    nombre,apellido = pilotoPuntos['name'].values()
    NyA = nombre +" "+apellido

    return (NyA)
