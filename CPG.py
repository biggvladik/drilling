import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

H=[200,500,900,1400,1800,2000,2340,2700,2950,3300]
Pre=[2.1,6.05,7.96,12.56,18,29.67,27.31,30.93,31.42,37.09]

def CPG(H,Pre):
    n=len(H)
    Pfr=[]
    Ka=[]
    Kfr=[]
    Phs=[]

    for i in range(n):                              # Получение расчётных данных
        Pfr.append(0.0083*H[i]+0.66*Pre[i])
        Phs.append(1000*9.81*H[i]*10**-6)
        Ka.append(Pre[i]/Phs[i])
        Kfr.append(Pfr[i]/Phs[i])

    fig =go.Figure()
    fig.update_yaxes(range=[-200, 3500])            #Коэффициенты для масштаба?
    fig.update_xaxes(range=[0.8, 2])
    H_fig=H.copy()
    Ka_fig=Ka.copy()
    Kfr_fig=Kfr.copy()

    j=0
    while j<2*n-2:                                  # Выравнивание графика пластовых давлений
        if Ka_fig[j]!=Ka_fig[j+1]:
            Ka_fig.insert(j+1,Ka_fig[j])
            H_fig.insert(j+1,H_fig[j+1])
            j+=2
    Ka_fig.insert(0, Ka_fig[0])
    H_fig.insert(0, 0)
    fig.add_trace(go.Scatter(x=Ka_fig, y=H_fig,name='P пластовое<sup></sup>'))


    k=0
    while k<2*n-2:                                     # Выравнивание графика давлений гидроразрыва
        if Kfr_fig[k]!=Kfr_fig[k+1]:
            Kfr_fig.insert(k+1,Kfr_fig[k])
            k+=2
    Kfr_fig.insert(0, Kfr_fig[0])
    fig.add_trace(go.Scatter(x=Kfr_fig, y=H_fig,name='P гидроразрыва<sup></sup>'))
    fig.update_layout(legend_orientation="h",
                title="График совмещенных давлений",
                xaxis_title="Градиент давлений, МПа/100м",
                yaxis_title="Глубина спуска колонн, м",
                xaxis_title_font="h",
                margin=dict(l=30, r=30, t=30, b=30))

    return fig
a=CPG(H,Pre)
a.show()
#print(a)