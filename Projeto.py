# -vamos modelar um dardo de nerf sendo disparado com um certo angulo

# --------------------------PARAMETROS INICIAIS -------------------------------------

# Importa bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint

# dados do DARDO (objeto)

m = 0.0015               # massa (Kg)
A = ((0.013/2)**2) * pi  # área frontal (m²)
v0 =                     # velocidade inicial (m/s)

Cd = 0.75                # coeficiente de arrasto do Dardo (adimencional)

# dados FISICOS (ambiente)

g = 9.81        # gravidade (m/s²)
d = 1.225       # densidade do ar (kg/m³)

# angulos (graus)
angulos = np.arange(0,90,10)

# ------------------------ MODELO ---------------------------------------------------

tempo = np.arange() #se


