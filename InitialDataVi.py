#Created by: Lars Daniel Johansson Nino, economics undergrad at Instituto Tecnologico Autonomo de Mexico ITAM
#Date: March 2022
#Purpose: Initial data vizualization for suicide data from Mexico from 2005 to 2019
import pandas as pd
import csv
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
import time
import numpy as np

def main():
    engine = create_engine('sqlite://', echo=False)
    datapath = rf"\Users\Dani Johansson\Desktop\DATA N RESEARCH\SyD\DATA20052019SUIC.csv"
    data = (pd.read_csv(datapath, index_col= 0)).to_sql('data', con=engine)

    barCount(data,engine,-1, 'ENT_OCURR')
    datTrends(data,engine,-1,'ENT_OCURR')
    speComposition(data,engine,-1,'ENT_OCURR',False)

#Methods Beggin
def barCount(data, engine, periods, param):
    #Case u=-1 -> total number
    if periods == -1:
        tu = "SELECT * FROM data"
    else:
        if periods < 10:
            val = '0'+str(u)
        else:
            val = str(u)
        tu = f"SELECT * FROM data WHERE ANIO_REGIS = 'd20{val}'"
    tem = engine.execute(tu)
    tem = pd.DataFrame(tem)
    with sns.axes_style('darkgrid'):
        g = sns.catplot(x = param, data=tem, aspect=3, kind="count", color='steelblue').set(title=f'Distribution of suicides 2005-2019')
        g.set_xticklabels(step=1)
        g.set_ylabels('Number of deaths')
        plt.show()

def datTrends(data, engine, location, param):
    print("Trends")
    valYears = []
    dates = pd.date_range("2005", periods = 15, freq = "12M")

    for i in range(5,20):
        if i < 10:
            val = '0'+str(i)
        else:
            val = str(i)
        tem = pd.DataFrame(engine.execute(f"SELECT COUNT(*) FROM data WHERE ANIO_REGIS = '20{val}'"))
        valYears.append(tem['COUNT(*)'][0])


    datas = pd.DataFrame(valYears, dates, columns=['Number of Suicides'])
    with sns.axes_style('whitegrid'):
        sns.lineplot(data=datas, palette="tab10", linewidth=1.4).set(title=f'Evolution of suicides 2005-2019')
        plt.show()

def speComposition(data, engine, u, param, byState):
    # param -> specific composition variable to examine in relation to the whole
    print("Special composition")
    for i in range(1,32):
        entid = i
        tem = f"SELECT * FROM data WHERE ANIO_REGIS = '2005' AND ENT_OCURR = {entid}"
        tem = pd.DataFrame(engine.execute(tem))
        print(tem.head())
        sns.kdeplot(tem['ESCOLARIDA']).set(title=f'Escolaridad para: {entid}')
        plt.show()
        sns.kdeplot(tem['MUN_OCURR']).set(title=f'MUN_OCURR para: {entid}')
        plt.show()
        sns.countplot(x=tem['MUN_OCURR']).set(title=f'MUN_OCURR para: {entid}')
        plt.show()
        sns.boxplot(x = tem['MUN_OCURR'], y =tem['ESCOLARIDA'], data = tem, hue = tem['SEXO'])
        plt.show()
        temMunEsc = tem.pivot_table(index = 'MUN_OCURR', columns = 'ESCOLARIDA', values = 'DERECHOHAB')
        sns.heatmap(temMunEsc, cmap = 'Blues')
        plt.show()
        sns.pairplot(temMunEsc, hue = 'ESCOLARIDA', palette = 'Blues')
        plt.show()
main()
