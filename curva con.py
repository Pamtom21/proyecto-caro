import matplotlib.pyplot as plt

r= 100000 # r = resistencia den ohmios
VB= 12 # VB = voltaje de la bateria en voltios
C=500 * (10**-6) # C = es la capacidad en faradios
Vc0= 1.25 # voltaje inicial del condesador en voltios
e= 2.718 # constante de euler

#calcular corriente de condensador en funcon del tiempo
def VC(t):
    var= VB - Vc0
    var2 = e ** ((-1*t)/(r*C))
    var3= var * var2
    return VB - var3


#graficar
fig, ax = plt.subplots()

#funcion que calcula la corriente en el condensador en funcion del tiempo 
def IC(t):
    return (VB-VC(t)) / r

Tiempo = range(500)
ICs = [IC(t) for t in Tiempo ]
VCs = [VC(t) for t in Tiempo]    



ax.plot(Tiempo, VCs)
ax.set_title('Curva de Tension', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_xlabel("Tiempo(s)")
ax.set_ylabel("Voltaje del condensador (Vc)")

ax1 = ax.twinx()
color = 'tab:red'
ax1.plot(Tiempo,ICs, color = color)
ax1.set_ylabel("corriente de el condensador (A)", color=color)
ax1.tick_params(axis='y', labelcolor = color)


fig.tight_layout()
plt.savefig('Curva_De_Carga_C.png')
plt.show()