import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import exp, linspace 
x = linspace(0, 7, 70)
y= (1-x)*exp(-x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('expx')
plt.title('Eksponenciala funkcija')
plt.plot(x, y)
plt.plot(x, y, color = "#001100")
plt.show()
