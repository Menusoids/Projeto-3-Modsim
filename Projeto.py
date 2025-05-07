# -vamos modelar um dardo de nerf sendo disparado com um certo angulo


# Importa bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint

# --------------------------PARAMETROS INICIAIS -------------------------------------

# dados do DARDO (objeto)

m = 0.0015               # massa (Kg)
A = ((0.013/2)**2) * pi  # área frontal (m²)
Cd = 0.75                # coeficiente de arrasto do Dardo (adimencional)

v0 = 15                  # velocidade inicial (m/s)
x0 = 0                   # posição inicial (m)
y0 = 0                   # posição inicial (m)

# dados FISICOS (ambiente)

g = 9.81                 # gravidade (m/s²)
d = 1.225                # densidade do ar (kg/m³)

# angulos (graus)
angulos = np.arange(0,90,10) # lista de variação do angulo

# ------------------------ MODELO ---------------------------------------------------

dt = 1e-3
tempo = np.arange(0,3,dt) #lista de tempo

def modelo (X, t):

    # Desgrupa a lista
    x, y, vx, vy = X

    # Calcula velocidade
    v = sqrt(vx**2 + vy**2)
    cos_ang = vx/v # coseno
    sin_ang = vy/v # seno
    
    # Calcula as forças
    D = (1/2) * d * A * Cd * v**2
    P = m*g

    # Calcula as taxas de variação
    dxdt = vx
    dydt = vy
    dvxdt = (-D * cos_ang) / m 
    dvydt = (-D * sin_ang - P) / m

    # Verifica se a esfera já atingiu o chão (caso y<0, zera as derivadas)
    if y < 0:
        return [0, 0, 0, 0]
    
    # Agrupa a lista com as taxas de variação
    return [dxdt, dydt, dvxdt, dvydt]


# --------------- APLICAÇÃO PARA VALIDAÇÃO ------------------

# Determina angulo fixo
ang = 45

# Calcula velocidades em cada eixo
vx0 = v0 * cos (radians(ang))
vy0 = v0 * sin (radians(ang))

# Agrupa em uma lista
X = [x0, y0, vx0, vy0]

# Aplica odeint
aplicação = odeint(modelo, X, tempo)

# Faz gráfico
plt.plot(aplicação[:,0], aplicação[:,1], label=f'{ang}°')
plt.title('Trajetória do lançamento oblíquo')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid()
plt.show()

# --------------- GRÁFICO PRÉ CONCLUSIVO ---------------------------------

for ang in angulos:
    if ang == 10:
        continue

    vx0 = v0 * cos (radians(ang))
    vy0 = v0 * sin (radians(ang))

    X = [x0, y0, vx0, vy0]
    aplicação = odeint(modelo, X, tempo)
    plt.plot(aplicação[:,0], aplicação[:,1], label=f'{ang}°')

plt.title('Trajetória do lançamento para diferentes angulos')
plt.axis('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid()
plt.show()



		




