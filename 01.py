import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Даны значения величины заработной платы заемщиков банка (zp)
# и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии,
# приняв за X заработную плату (то есть, zp - признак),
# а за y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b0 = (np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
b1 = np.mean(y)-b0*np.mean(x)

print("Коэффициенты для x,y по формуле:")
print(b0)
print(b1)

y_pred = 2.62*x+444.18


x_matrix = x.reshape((10, 1))
y_matrix = y.reshape((10, 1))

z = np.hstack([np.ones((10, 1)), x_matrix])

b2 = np.dot(np.linalg.inv(np.dot(z.T, z)), z.T @ y_matrix)
print("Коэффициенты по матричному методу с интерсептом:\n", b2)


b3 = np.dot(np.linalg.inv(np.dot(x_matrix.T, x_matrix)), x_matrix.T @ y_matrix)
print("Коэффициент по матричному методу без интерсепта:\n", b3)


# Посчитать коэффициент линейной регрессии при заработной плате (zp),
# используя градиентный спуск (без intercept).

print("Градиентный спуск без интерсепта:")
B = 0.1
B0 = 0.1
n = 10


def mse(B, y=y, x=x, n=10):
    return np.sum((B*x-y)**2)/n


alpha = 5e-5

for i in range(2000):
    B -= alpha*(2/n)*np.sum((B*x-y)*x)
    if i % 50 == 0:
        print('Итерация = {i}, B = {B}, mse = {mse}'.format(i=i, B=B, mse=mse(B)))

# Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге
# одновременно (то есть изменение одного коэффициента не должно влиять
# на изменение другого во время одной итерации).

print("Градиентный спуск с интерсептом:")


def mse(B,B1, y=y, x=x, n=10):
    return np.sum((B0+B*x-y)**2)/n


for i in range(2000000):    
    B0 -= alpha*(2/n)*np.sum((B0+B*x-y))
    B -= alpha*(2/n)*np.sum((B0+B*x-y)*x)
    if i % 100000 == 0:
        print('Итерация = {i}, B = {B}, B0 = {B0}, mse = {mse}'.format(i=i, B=B, B0=B0, mse=mse(B, B0)))
