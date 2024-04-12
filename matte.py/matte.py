import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2
def integral(a,b,n):
    i=0
    bredd=abs(a)+abs(b)
    totalarea=0
    while i<n:
        breddrektangel=bredd/n
        höjd=breddrektangel+a
        höjden=höjd**2
        area=höjden*breddrektangel
        totalarea=area+totalarea
        i+=1
    return totalarea



x=np.linspace(-10,10,100)

y=f(x)
resultat=integral(-1,1,5)
print(resultat)
plt.plot(x,y)
plt.show()

