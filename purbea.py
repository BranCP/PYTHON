import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(3, 3*np.pi,5000)
fig=plt.figure(figsize=(8,6),dpi=600)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp');
print("hola")
