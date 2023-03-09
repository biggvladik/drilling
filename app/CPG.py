import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
H=[200,500,900,1400,1800,2000,2340,2700,2950,3300]
Pre=[2.1,6.05,7.96,12.56,18,29.67,27.31,30.93,31.42,37.09]



def CPG(H,Pre):
    Pfr=[]
    Ka=[]
    Kfr=[]
    Phs=[]
    n = len(H)
    for i in range(n):                              # Получение расчётных данных
        Pfr.append(0.0083*H[i]+0.66*Pre[i])
        Phs.append(1000*9.81*H[i]*10**-6)
        Ka.append(Pre[i]/Phs[i])
        Kfr.append(Pfr[i]/Phs[i])
    fig =go.Figure()
    fig.update_yaxes(range=[H[-1]+700,-100 ])            #Коэффициенты для масштаба?
    fig.update_xaxes(range=[0.8, 2],side='top')
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
    Ka_fig.append(Ka_fig[-1])
    H_fig.append(H_fig[-1]+500)
    fig.add_trace(go.Scatter(x=Ka_fig, y=H_fig,name='P пластовое<sup></sup>'))
    k=0
    while k<2*n-2:                                     # Выравнивание графика давлений гидроразрыва
        if Kfr_fig[k]!=Kfr_fig[k+1]:
            Kfr_fig.insert(k+1,Kfr_fig[k])
            k+=2
    Kfr_fig.insert(0, Kfr_fig[0])
    Kfr_fig.append(Kfr_fig[-1])
    fig.add_trace(go.Scatter(x=Kfr_fig, y=H_fig,name='P гидроразрыва<sup></sup>'))
    fig.update_layout(legend_orientation="h",
                title="График совмещенных давлений",
                xaxis_title="Градиент давлений, МПа/100м",
                yaxis_title="Глубина спуска колонн, м",
                margin=dict(l=30, r=30, t=30, b=30))
    intervals=0
    len_intervals=0
    H_intervals=[]
    while len_intervals<H_fig[-1]:
        Ka_max=[]               #Интервалы бурения
        H_max=[]
        Ka_max.append(max(Ka_fig))
        Ka_max.append(max(Ka_fig))
        index_max=Ka_fig.index(max(Ka_fig))
        H_max.append(H_fig[index_max])
        H_max.append(H_fig[index_max+1])
        H_plot=H_fig[-1:index_max+1:-1]
        Kfr_plot=Kfr_fig[len(Kfr_fig)-1:index_max+1:-1]
        Ka_max.append(min(Kfr_plot))
        Ka_max.append(min(Kfr_plot))
        index_min = Kfr_plot.index(min(Kfr_plot))
        H_max.append(H_plot[index_min])
        H_max.append(H_plot[index_min + 1])
        if max(Ka_fig)>min(Kfr_plot):
            H_max.remove(H_max[-2])
            Ka_max.remove(Ka_max[-2])
            H_max.insert(2,H_max[-1])
            Ka_max.insert(2,max(Ka_fig))
        else:
            H_max.insert(2,max(H_fig))
            Ka_max.insert(2,max(Ka_fig))
            H_max.insert(3,max(H_fig))
            Ka_max.insert(3,min(Kfr_plot))
        for i in range(Kfr_fig.index(min(Kfr_plot)),0,-1):
            if Kfr_fig[i]<min(Kfr_plot):
                H_max.append(H_fig[i])
                Ka_max.append(min(Kfr_plot))
                break
            elif min(Kfr_plot)==min(Kfr_fig):
                H_max.append(0)
                H_max.append(0)
                Ka_max.append(min(Kfr_plot))
                Ka_max.append(max(Ka_fig))
        H_max.append(H_max[0])
        Ka_max.append(Ka_max[0])
        fig.add_trace(go.Scatter(x=Ka_max, y=H_max, name='Интервал бурения<sup></sup>'))
        ind_del_min = H_fig.index(min(H_max))+1
        ind_del_max = H_fig.index(max(H_max))+1
        for g in range(ind_del_max-ind_del_min):
                H_fig.pop(ind_del_min)
                Ka_fig.pop(ind_del_min)
                Kfr_fig.pop(ind_del_min)
        len_intervals=len_intervals+max(H_max)-min(H_max)
        intervals+=1
        H_intervals.append(max(H_max))
    return H_intervals,intervals,fig.show()
#a,b,c=CPG(H,Pre)
#a.show()
#print("Количество интервалов бурения:",c)
#print("Глубины интервалов бурения:" ,b)

