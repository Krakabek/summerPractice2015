__author__ = 'Danil Radkovsky, Stas Chmilenko'
import pylab as p
import numpy as np

def f(x):
    return (x - 2) ** 2

def min(f, a, b, eps, points=[]):
    delta = (b - a) / 1000.0
    x1 = (a + b) / 2 - delta
    x2 = (a + b) / 2 + delta

    if f(x1) < f(x2):

        points.append(x2)
        if (x2 - a) < eps:

            x_min = (x2 + a) / 2

            return [f(x_min), x_min, points]

        else:
            return min(f, a, x2, eps, points)

    else:
        points.append(x1)
        if (b - x1) < eps:

            x_min = (b + x1) / 2

            return [f(x_min), x_min, points]

        else:
            return min(f, x1, b, eps, points)

if __name__ == '__main__':
    points = []
    res = min(f, -5, 5, 0.01)
    print("%.2f" % res[0], "%.2f" % res[1])
    x = p.arange(-5, 5, 0.01)
    p.figure()
    p.plot(x, f(x))
    p.plot(res[2], map(f, res[2]), 'ro')
    # p.plot(res[2], map(lambda y:0, res[2]), 'b*')
    p.ylim([-1, 30])
    p.xlim([-5, 5])
    p.xlabel('X')
    p.ylabel('F(X)')
    p.show()
