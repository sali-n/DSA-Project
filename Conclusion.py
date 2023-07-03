import numpy as np
import matplotlib.pyplot as plt

sizes = [1000,10000,100000]

# times = [5.78E-03, 0.5509955, 75.1365939]   #for array find
#times = [0.0158749, 2.7956147, 421.6265063]   #for linked list find
times = [0.0005436, 0.0534972, 38.538236]    #for array deletion

plt.scatter(sizes[1:3],times[1:3])
f = np.polyfit(sizes,times,2)

newsamples = [10**x for x in range(3,7)]
newx = np.linspace(min(newsamples),max(newsamples),150)

a = [(lambda x: f[0]*x**2 + f[1]*x + f[2])(x) for x in newx]

print(np.interp(1000000,newx,a)/60)

plt.plot(newx,a,color='red')