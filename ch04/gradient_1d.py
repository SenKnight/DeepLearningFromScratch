# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)


def function_1(x):
    return 0.01*x**2 + 0.1*x 


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(f'{x}的斜率：{d}')
    y = f(x) - d*x
    return lambda t: d*t + y # 这里返回倒数在x时的切线，参数等于t，斜率等于d，偏移值由t=x时确定（此时y=f(x)）
     
x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf1 = tangent_line(function_1, 5)
tf2 = tangent_line(function_1, 10)

plt.plot(x, y)
plt.plot(x, tf1(x))
plt.plot(x, tf2(x))
plt.show()
