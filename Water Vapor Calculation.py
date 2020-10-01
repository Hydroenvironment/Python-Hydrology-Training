import numpy as np
t = np.linspace(-100,100,50)
es = 611*np.exp(17.27*t/(237.3+t))
plt.plot(t,es)
plt.xlabel('t (degree Celcius)')
plt.ylabel('es (Pa)')
plt.show()
