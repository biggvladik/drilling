from typing import Dict

H_intervals=[3450,2000]
intervals=2
Q=39
well_type="Oil"
def construction(H_intervals, intervals,Q,well_type):

    Q_OD_Oil={40:114.3,70:127,100:139.7,125:146.1,150:168.3,300:177.8,500:193.7}
    Q_OD_Gas={75:114.3,150:127,225:139.7,250:146.1,375:168.3,500:177.8,750:193.7,1000:219.1,3000:244.5,5000:273.1}
    PDC=[88.9,95.3,98.4,108,114.3,117.5,120.7,123.8,127,130.2,139.7,142.9,149.2,152.4,155.6,158.8,165,171.5,200,215.9,
         222.3,250.8,279.4,311,320,349.2,365.1,368.3,371.5,393.7,444.5,469.9,473.1,490,508]
    OD_coupling_diameter={114.3:127,127:141.3,139.7:153.7,146.1:166,168.3:187.7,177.8:194.5,193.7:215.9,219.1:244.5,
                          244.5:269.9,273.1:298.5,298.5:323.9,323.9:351,339.7:365.1,351:376,377:402,406.4:431.8,426:451,473.1:508,508:533.4}
    OD_gap={114.3:5,127:15,139.7:10,146.1:15,168.3:15,177.8:10,193.7:15,219.1:20,244.5:25,273.1:15,298.5:30,323.9:20,
            339.7:30,351:40,377:25,406.4:30,426:35,473.1:45,508:50}
    ID_OD={97.1:114.3,99.5:114.3,101.5:114.3,102.9:114.3,103.9:114.3,108.6:127,112:127,114.2:127,115.8:127,118.7:139.7,
           121.3:139.7,124.3:139.7,125.7:139.7,127.3:139.7,144.1:168.3,147.1:168.3,150.5:168.3,152.3:168.3,152.4:177.8,
           153.7:168.3,154.8:177.8,157:177.8,159.4:177.8,161.6:177.8,164:177.8,166:177.8,168.3:193.7,171.9:193.7,
           174.7:193.7,177.1:193.7,178.5:193.7,190.7:219.1,193.7:219.1,196.3:219.1,198.7:219.1,201.3:219.1,203.7:219.1,
           205.7:219.1,216.9:244.5,220.5:244.5,222.3:244.5,224.5:244.5,226.7:244.5,228.7:244.5,240.1:273.1,242.9:273.1,
           245.5:273.1,247.9:273.1,250.3:273.1,252.7:273.1,255.3:273.1,258.9:273.1,268.9:298.5,273.7:298.5,276.3:298.5,
           279.5:298.5,281.5:298.5,295.9:323.9,299.1:323.9,301.9:323.9,304.9:323.9,306.9:323.9,308.9:339.7,311.7:339.7,
           313.5:339.7,315.3:339.7,317.9:339.7,320.3:339.7,322.9:339.7,327:351,329:351,331:351,333:351,353:377,355:377,
           357:377,359:377,373:406.4,381.2:406.4,384.2:406.4,387.4:406.4,402:426,404:426,406:426,450.9:473.1,475.8:508,482.6:508,485.8:508}
    well_construcion=[]
    intervals+=1
    H_intervals.append(40)
    if well_type=='Oil':
        for key in Q_OD_Oil:
            if Q<key:
                D=Q_OD_Oil[key]
                break
    elif well_type=='Gas':
        for key in Q_OD_Gas:
            if Q < key:
                D = Q_OD_Gas[key]
                break
    d=100
    for key in ID_OD:
        if key>d:
            d=key
            s=round(0.5*(D-d),1)
            break
    for i in range(intervals):
        well_construcion.append({'H_intervals':H_intervals[i],'Db':0,'Dm':0,'D':D,'d':d,'s':s,'size':int(D + (0.5 if D > 0 else -0.5))})
        for key in OD_coupling_diameter:
            if D==key:
                Dm=OD_coupling_diameter[key]
                gap=OD_gap[key]
                break
        well_construcion[i]['Dm']=Dm
        Db=Dm+2*gap
        for j in range(len(PDC)):
            if PDC[j]>Db:
                Db=PDC[j]
                break
        well_construcion[i]['Db']=Db
        d=Db+2*0.3
        for key in ID_OD:
            if d<key:
                d=key
                D=ID_OD[key]
                s=round(0.5*(D-d),1)
                break


    return well_construcion



a=construction(H_intervals,intervals, Q, well_type)
for k in range (len(a)-1,-1,-1):
    print(a[k])
