__author__ = 'Danil Radkovsky, Stas Chmilenko'
import pylab as p

import minimization as m


def f(x):
    return (x - 2) ** 2


if __name__ == '__main__':
    points = []
    res = m.min(f, -5, 5, 0.01)
    print("%.2f %.2f" % (res["f"], res["x"]))
    x = p.arange(-5, 5, 0.01)
    p.figure()
    p.plot(x, f(x))
    p.plot(res["points"], map(f, res["points"]), 'ro')
    p.ylim([-1, 30])
    p.xlim([-5, 5])
    p.xlabel('X')
    p.ylabel('F(X)')
    p.show()

