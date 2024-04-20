import matplotlib.pyplot as plt
import time as t
r= 100000
VB= 12
C=500 * (10**-6)
Vc0= 1.25
e= 2.718
def VC(t):
    var= VB - Vc0
    var2 = e ** ((-1*t)/(r*C))
    var3= var * var2
    return VB - var3
fig, ax = plt.subplots()

VCs = []
Tiempo= []
for k in range(500):
    VCs.append(VC(k))
    Tiempo.append(k)
ax.plot(Tiempo, VCs)
ax.set_title('Curva de Tension', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_xlabel("Tiempo(s)")
ax.set_ylabel("Voltaje del condensador (Vc)")
plt.savefig('diagrama-dispersion.png')
plt.show()