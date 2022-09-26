# -*- coding: utf-8 -*-
"""Copy of Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pLKYHuW6zB1U8Voqv7m7gPIQ2Kl0xfjp
"""



import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
time = ctrl.Antecedent(np.arange(10,123,7),'time')
rice = ctrl.Antecedent(np.arange(100,1000,5),'rice')
power = ctrl.Consequent(np.arange(0,1.5,0.3),'power') 
time['rat ngan']= fuzz.trimf(time.universe,[10,10,20])
time['ngan']= fuzz.trimf(time.universe,[10,20,30])
time['vua du']= fuzz.trimf(time.universe,[20,30,80])
time['dai']= fuzz.trimf(time.universe,[30,80,110])
time['rat dai']= fuzz.trimf(time.universe,[80,110,120])
rice['bi song']= fuzz.trimf(rice.universe,[100,100,300])
rice['bi nhao']= fuzz.trimf(rice.universe,[100,300,500])
rice['vua chin']= fuzz.trimf(rice.universe,[300,500,900])
rice['bi chay']= fuzz.trimf(rice.universe,[500,900,1000])
power['Yeu']= fuzz.trimf(power.universe,[0,0,0.2])
power['Binh thuong']= fuzz.trimf(power.universe,[0,0.2,0.6])
power['Kha manh']= fuzz.trimf(power.universe,[0.2,0.6,0.7])
power['Manh']= fuzz.trimf(power.universe,[0.7,1,1])
time.view()
rice.view()
power.view()
power['Binh thuong'].view()
rule1=ctrl.Rule(time['rat dai'] & rice['bi song'], power['Yeu'])
rule2=ctrl.Rule(time['rat dai'] & rice['bi nhao'],power['Yeu'])
rule3=ctrl.Rule(time['rat dai'] & rice['bi chay'],power['Manh'])
rule4=ctrl.Rule(time['rat dai'] & rice['bi song'],power['Yeu'])
rule5=ctrl.Rule(time['rat dai'] & rice['bi nhao'],power['Binh thuong'])
rule6=ctrl.Rule(time['vua du'] & rice['bi chay'],power['Manh'])
rule7=ctrl.Rule(time['vua du'] & rice['bi song'],power['Binh thuong'])
rule8=ctrl.Rule(time['dai'] & rice['bi nhao'],power['Binh thuong'])
rule9=ctrl.Rule(time['dai'] & rice['bi chay'],power['Manh'])
rule10=ctrl.Rule(time['rat dai'] & rice['vua chin'],power['Kha manh'])
rule11=ctrl.Rule(time['rat dai'] & rice['bi nhao'],power['Binh thuong'])
rule12=ctrl.Rule(time['rat dai'] & rice['bi song'],power['Binh thuong'])
rule13=ctrl.Rule(time['rat dai'] & rice['bi chay'],power['Manh'])

powerinput_ctrl=ctrl.ControlSystem([rule1,rule2,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13])
powerinput=ctrl.ControlSystemSimulation(powerinput_ctrl)
powerinput.input['time']= 60
powerinput.input['rice'] = 700
powerinput.compute()
print(powerinput.output['power'])
power.view(sim=powerinput)