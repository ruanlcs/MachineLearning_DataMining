import numpy as np
import matplotlib.pyplot as plt

# Define os valores eixo x
x = np.linspace(-10, 10, 400)  

# coeficientes da função quadrática
a = 0.1875
b = -1.125
c = 3.6875

# Definindo a função
y = a * x**2 + b * x + c

# Exibe o gráfico
plt.plot(x, y, label=r'$y = 2x^2 + 3x - 5$')

plt.title('Gráfico da Equação')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)  
plt.axhline(0, color='black',linewidth=0.5) 
plt.axvline(0, color='black',linewidth=0.5)  
plt.show()
