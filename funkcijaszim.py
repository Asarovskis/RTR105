# Artūrs Asars-Asarovskis Rebco 1 Laboratorijas darbs No2. - Zīmēšana
#Improtē kāda faili nepieciešami, lai izveidotu grafiku
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import exp, linspace 
#Piedefinē robežas, kā arī ievada, kāda funkcija tiek uzzī mēta
x = linspace(0, 7, 70)
y= (1-x)*exp(-x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('expx')
#Piedefinē kā sauc doto grafiku
plt.title('Eksponenciala funkcija')
plt.plot(x, y)
#Piedefinē funkcijas līknes krāsu
plt.plot(x, y, color = "#001100")
plt.show()
