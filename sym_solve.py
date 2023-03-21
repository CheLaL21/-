import numpy
import math
import matplotlib.pyplot as plt

Z_line0 = 0.1 + 0.4j # погонное сопротивление ЛЭП
If = 10 # источник напряжения для активации схемы

L12 = 12 # км
L23 = 8 # км
L34 = 5.7 # км
L45 = 12.9 # км

Z12 = Z_line0 * L12 # комплексное сопротивление участка 12
Z23 = Z_line0 * L23 # комплексное сопротивление участка 23
Z34 = Z_line0 * L34 # комплексное сопротивление участка 34
Z45 =  Z_line0 * L45 # комплексное сопротивление участка 45

# в зависимости от координаты места повреждения пересчитываем участок 23 на до и после
Z23_1 = [0] * 100
Z23_2 = [0] * 100
I23_1 = [0] * 100
I23_2 = [0] * 100
K = [0] * 100
Z_mut = [0] * 100
Uf = [0+0j] * 100

xf = range(1,100) # координата места повреждения, %
# в зависимости от координаты места повреждения строится замер
for i in range(len(xf)):
    Z23_1[i] = Z23 *(xf[i])/100
    Z23_2[i] = Z23 *(100 - xf[i])/100
    Z_mut[i] = (Z23_1[i] * Z23_2[i])/(Z23_1[i] + Z23_2[i])
    Uf[i] = If * Z_mut[i]
    I23_2[i] = Uf[i] / Z23_2[i]
    I23_1[i] = Uf[i] / Z23_1[i]
    K[i] = (I23_1[i] - I23_2[i]) / (I23_1[i] + I23_2[i])
    K[i] = K[i].real

K.pop()

plt.plot(xf,K, linewidth = 2.0)
plt.title("Замер для поврежденного участка цепи")
plt.xlabel("Координата места повреждения, %")
plt.ylabel("Замер, о.е")
plt.show()
