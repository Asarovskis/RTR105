import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import sin, linspace
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$sin(x)$')
plt.plot(x, y2)
plt.show()

x = linspace(0, 4, 70)
y1= x
plt.plot(x, y1, color = "#FF0000")

x = linspace(0, 4, 70)
y2= y1**3(1,2,3)

plt.plot(x, y2, color = "#0000FF")

x = linspace(0, 4, 70)
y3= y2**5(1,2,3)

plt.plot(x, y3, color = "#FFFF00")

x = linspace(0, 4, 70)
y4= y3**7(1,2,3)

plt.plot(x, y4, color = "#00FFFF")


plt.show()
