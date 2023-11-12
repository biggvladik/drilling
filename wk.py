import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

class Well:

    def __init__(self,H,Ppl,well_type,Q):
        self.H=H                    #Глубина
        self.Ppl=Ppl                #Пластовое давление на глубине Н
        self.well_type=well_type    #Тип скважины "Нефтяная" или "Газовая"
        self.Q=Q                    #Дебит скважины в т/сутки если скважина нефтяная и м^3/сутки если газовая
        self.coef = None
        self.condi = None

    def coefficients(self):
        Ka=[]           #Коэффициент аномальности
        p_min=[]        #Минимальная плотность БР
        p_max=[]        #Максимальная плотность БР
        Kp=[]           #Коэффициент поглащения
        Kgr=[]          #Коэффициент гидроразрыва пласта
        Pgs=[]          #Гидрастатическиое давление
        Ppogl=[]        #Давление поглащения


        for i in range(len(self.H)):
            Pgs.append(9.81*1000*self.H[i]/1000000)
            Ppogl.append(0.0083 * self.H[i] + 0.66 * self.Ppl[i])
            Ka.append(round(self.Ppl[i]/Pgs[i],3))
            Kp.append(round(Ppogl[i]/Pgs[i],3))
            Kgr.append(round(1.2*Ppogl[i]/Pgs[i],3))
            if self.H[i]<2500:
                p_min.append(round(Ka[i]*1.1,3))
                p_max.append(round(Kp[i]/1.1, 3))
            else:
                p_min.append(round(Ka[i] * 1.05, 3))
                p_max.append(round(Kp[i] / 1.05, 3))




        self.coef=[self.H,Ka,Kp,Kgr,p_min,p_max]
        return self.coef

    # def compatible_conditions(self):
    #
    #     H_line=[50]       #Грлубины спуска ОК
    #     min_line=[]     #Минимумы плотностей
    #     max_line=[]     #Максимумы плотностей
    #
    #     # Добавление начальной точки
    #     self.coef[0].insert(0, 0)
    #     self.coef[1].insert(0, self.coef[1][0])
    #     self.coef[2].insert(0, self.coef[2][0])
    #     self.coef[3].insert(0, self.coef[3][0])
    #     self.coef[4].insert(0, self.coef[4][0])
    #     self.coef[5].insert(0, self.coef[5][0])
    #
    #     #Определение совместимых условий бурения
    #     d=0        #Подошва предидущего интервала
    #     for k in range(2,len(self.H)):
    #         if self.coef[4][k]>min(self.coef[5][self.H.index(d)+1:k+1]):
    #             H_line.append(self.H[k])
    #             min_line.append(max(self.coef[4][self.H.index(d):k]))
    #             max_line.append(min(self.coef[5][self.H.index(d):k]))
    #             d=self.H[k]
    #
    #         elif max(self.coef[4][self.H.index(d)+1:k+1])>self.coef[5][k]:
    #             H_line.append(self.H[k])
    #             min_line.append(max(self.coef[4][self.H.index(d):k]))
    #             max_line.append(min(self.coef[5][self.H.index(d):k]))
    #             d=self.H[k]
    #
    #         elif k==len(self.H)-1:
    #             H_line.append(self.H[k])
    #             min_line.append(max(self.coef[4][self.H.index(d)+1:k+1]))
    #             max_line.append(min(self.coef[5][self.H.index(d)+1:k+1]))
    #             d=self.H[k]
    #
    #
    #     self.condi=[H_line,min_line,max_line]
    #     print('CONDI',self.condi)
    #     return self.condi

    def graphic(self):

        #Создание ступенчатых графиков
        plt.step(x=self.coef[1],y=self.coef[0],data=None,where='post',marker='.',label="Коэффициент аномальности" )
        plt.step(x=self.coef[2],y=self.coef[0],data=None,where='post',marker='.',label="Коэффициент поглащения")
        plt.step(x=self.coef[3],y=self.coef[0],data=None,where='post',marker='.',label="Коэффициент гидроразрыва")
        plt.step(x=self.coef[4],y=self.coef[0],data=None,where='post',marker='.',label="Минимальная плотность БР")
        plt.step(x=self.coef[5], y=self.coef[0], data=None, where='post', marker='.',label="Максимальная плотность БР")

        #Обозначение совместимых условий
      #  plt.fill_between(x=[self.coef[4][0], self.coef[5][0]], y1=0, y2=50, color='g', alpha=0.4)
        for l in range(len(self.condi[0])-1):
            plt.fill_between(x=[self.condi[1][l],self.condi[2][l]],y1=self.condi[0][l],y2=self.condi[0][l+1], color='g', alpha=0.4)

        #Оформление графиков
        plt.title('График совмещенных давлений', fontsize=17)
        plt.xlabel('К', fontsize=12, color='blue')
        plt.ylabel('Н,м', fontsize=12, color='blue')
        plt.legend(loc='upper right')
        plt.grid(True)
        plt.gca().invert_yaxis()

        plt.savefig('well_graphic.png')
        plt.show()
    def construction(self):

        #Диаметр эксплотационки от дебита нетфи (тонн/сутки)
        Q_OD_Oil = {40: 114.3, 70: 127, 100: 139.7, 125: 146.1, 150: 168.3, 300: 177.8, 500: 193.7}
        # Диаметр эксплотационки от дебита газа (м^3/сутки)
        Q_OD_Gas = {75: 114.3, 150: 127, 225: 139.7, 250: 146.1, 375: 168.3, 500: 177.8, 750: 193.7, 1000: 219.1,
                    3000: 244.5, 5000: 273.1}
        #Диаметры долот
        PDC = [88.9, 95.3, 98.4, 108, 114.3, 117.5, 120.7, 123.8, 127, 130.2, 139.7, 142.9, 149.2, 152.4, 155.6, 158.8,
               165, 171.5, 200, 215.9,222.3, 250.8, 279.4, 311, 320, 349.2, 365.1, 368.3, 371.5, 393.7, 444.5, 469.9,
               473.1, 490, 508]
        OD_coupling_diameter = {114.3: 127, 127: 141.3, 139.7: 153.7, 146.1: 166, 168.3: 187.7, 177.8: 194.5,
                                193.7: 215.9, 219.1: 244.5,244.5: 269.9, 273.1: 298.5, 298.5: 323.9, 323.9: 351,
                                339.7: 365.1, 351: 376, 377: 402,406.4: 431.8, 426: 451, 473.1: 508, 508: 533.4}
        OD_gap = {114.3: 5, 127: 15, 139.7: 10, 146.1: 15, 168.3: 15, 177.8: 10, 193.7: 15, 219.1: 20, 244.5: 25,
                  273.1: 15, 298.5: 30, 323.9: 20,339.7: 30, 351: 40, 377: 25, 406.4: 30, 426: 35, 473.1: 45, 508: 50}
        ID_OD = {97.1: 114.3, 99.5: 114.3, 101.5: 114.3, 102.9: 114.3, 103.9: 114.3, 108.6: 127, 112: 127, 114.2: 127,
                 115.8: 127, 118.7: 139.7,121.3: 139.7, 124.3: 139.7, 125.7: 139.7, 127.3: 139.7, 144.1: 168.3,
                 147.1: 168.3, 150.5: 168.3,152.3: 168.3, 152.4: 177.8,153.7: 168.3, 154.8: 177.8, 157: 177.8,
                 159.4: 177.8, 161.6: 177.8, 164: 177.8, 166: 177.8,168.3: 193.7, 171.9: 193.7,174.7: 193.7,
                 177.1: 193.7, 178.5: 193.7, 190.7: 219.1, 193.7: 219.1, 196.3: 219.1, 198.7: 219.1,201.3: 219.1,
                 203.7: 219.1,205.7: 219.1, 216.9: 244.5, 220.5: 244.5, 222.3: 244.5, 224.5: 244.5, 226.7: 244.5,
                 228.7: 244.5,240.1: 273.1, 242.9: 273.1,245.5: 273.1, 247.9: 273.1, 250.3: 273.1, 252.7: 273.1,
                 255.3: 273.1, 258.9: 273.1, 268.9: 298.5,273.7: 298.5, 276.3: 298.5,279.5: 298.5, 281.5: 298.5,
                 295.9: 323.9, 299.1: 323.9, 301.9: 323.9, 304.9: 323.9, 306.9: 323.9,308.9: 339.7, 311.7: 339.7,
                 313.5: 339.7, 315.3: 339.7, 317.9: 339.7, 320.3: 339.7, 322.9: 339.7, 327: 351, 329: 351, 331: 351,
                 333: 351, 353: 377, 355: 377,357: 377, 359: 377, 373: 406.4, 381.2: 406.4, 384.2: 406.4, 387.4: 406.4,
                 402: 426, 404: 426, 406: 426,450.9: 473.1, 475.8: 508, 482.6: 508, 485.8: 508}

        count_intervals=len(self.condi[0])
        H_intervals = self.condi[0][::-1]
        global well_construcion
        well_construcion = []
        if self.well_type == 'Нефтяная':
            for key in Q_OD_Oil:
                if self.Q < key:
                    D = Q_OD_Oil[key]
                    break
        elif self.well_type == 'Газовая':
            for key in Q_OD_Gas:
                if self.Q < key:
                    D = Q_OD_Gas[key]
                    break
        d = 0.875 * D
        for key in ID_OD:
            if key > d:
                d = key
                s = round(0.5 * (D - d), 1)
                break
        for i in range(count_intervals-1):
            well_construcion.append(
                {'Db': 0, 'Dm': 0, 'D': D, 'd': d, 's': s, 'size': int(D + (0.5 if D > 0 else -0.5)),
                 'H_intervals': H_intervals[i]})
            for key in OD_coupling_diameter:
                if D == key:
                    Dm = OD_coupling_diameter[key]
                    gap = OD_gap[key]
                    break
            well_construcion[i]['Dm'] = Dm
            Db = Dm + 2 * gap
            for j in range(len(PDC)):
                if PDC[j] > Db:
                    Db = PDC[j]
                    break
            well_construcion[i]['Db'] = Db
            d = Db + 2 * 0.3
            for key in ID_OD:
                if d < key:
                    d = key
                    D = ID_OD[key]
                    s = round(0.5 * (D - d), 1)
                    break

        return well_construcion[::-1]

    # def cementing(self):
    #
    #     V_cement=0
    #
    #     for g in range(len(well_construcion)):
    #         V_cement+=(well_construcion[g]['d']**2*math.pi*10**-5)/4    #Расчет цементного стакана
    #         if g==1:                                                #Расчет V1 для направления
    #             V_cement +=(math.pi * (well_construcion[g]['Db'] ** 2 - well_construcion[g]['D'] ** 2) * (
    #                         well_construcion[g]['H_intervals']) * 10 ** -6)/ 4
    #         else:                                                   #Расчет V1 и V2 для остальных интервалов
    #             V_cement+=(math.pi*(well_construcion[g]['Db']**2-well_construcion[g]['D']**2)*(
    #                 well_construcion[g-1]['H_intervals']-well_construcion[g]['H_intervals'])*10**-6)/4
    #             if self.well_type=='Нефтяная':
    #                 V_cement+=(math.pi*(well_construcion[g-1]['d']**2-well_construcion[g]['D']**2)*150*10**-6)/4
    #             elif self.well_type=='Газовая':
    #                 V_cement+=(math.pi*(well_construcion[g-1]['d']**2-well_construcion[g]['D']**2)*500*10**-6)/4
    #     return round(V_cement,3)

    def cementing(self):
        V_cement = 0
        for g in range(len(well_construcion)):
            V_cement += ((well_construcion[g][
                              'd'] / 1000) ** 2 * math.pi * 10) / 4
            if g == 0:
                V_cement += (math.pi * (
                ((well_construcion[g]['Db'] / 1000) ** 2 - (well_construcion[g]['D'] / 1000) ** 2)) *
                             well_construcion[g]['H_intervals']) / 4
            else:
                V_cement += (math.pi * (
                            (well_construcion[g - 1]['d'] / 1000) ** 2 - (well_construcion[g]['D'] / 1000) ** 2) *
                             well_construcion[g - 1]['H_intervals']) / 4
                if self.well_type == 'РќРµС„С‚СЏРЅР°СЏ':
                    V_cement += (math.pi * ((well_construcion[g]['Db'] / 1000) ** 2 - (
                                well_construcion[g]['D'] / 1000) ** 2) * 150 * 10 ** -6) / 4
                elif self.well_type == 'Р“Р°Р·РѕРІР°СЏ':
                    V_cement += (math.pi * ((well_construcion[g]['Db'] / 1000) ** 2 - (
                                well_construcion[g]['D'] / 1000) ** 2) * 500 * 10 ** -6) / 4
        return round(V_cement, 3)





    def compatible_conditions(self):

        H_line = [0]
        min_line = []
        max_line = []


        self.coef[0].insert(0, 0)
        self.coef[1].insert(0, self.coef[1][0])
        self.coef[2].insert(0, self.coef[2][0])
        self.coef[3].insert(0, self.coef[3][0])
        self.coef[4].insert(0, self.coef[4][0])
        self.coef[5].insert(0, self.coef[5][0])


        d = 0
        for k in range(1, len(self.H)):
            if self.coef[4][k] > min(self.coef[5][self.H.index(d) + 1:k + 1]):
                H_line.append(self.H[k - 1])
                min_line.append(max(self.coef[4][self.H.index(d) + 1:k]))
                max_line.append(min(self.coef[5][self.H.index(d) + 1:k]))
                d = self.H[k - 1]

            elif max(self.coef[4][self.H.index(d) + 1:k + 1]) > self.coef[5][k]:
                H_line.append(self.H[k - 1])
                min_line.append(max(self.coef[4][self.H.index(d) + 1:k]))
                max_line.append(min(self.coef[5][self.H.index(d) + 1:k]))
                d = self.H[k - 1]

            elif k == len(self.H) - 1:
                H_line.append(self.H[k])
                min_line.append(max(self.coef[4][self.H.index(d) + 1:k + 1]))
                max_line.append(min(self.coef[5][self.H.index(d) + 1:k + 1]))
                d = self.H[k]

        self.condi = [H_line, min_line, max_line]
        return self.condi


# well1=Well([50,200,700,1100,1500,2000,2100],[0.6,2.2,7.4,12.3,15.3,20,18.8],'Нефтяная',80)
# print(well1.coef)
# well1.coefficients()
# well1.compatible_conditions()
# print(f'{well1.construction()}')
# print(well1.cementing())
# well1.graphic()





