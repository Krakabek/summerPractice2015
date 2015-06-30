__author__ = 'Danil Radkovsky, Stas Chmilenko'
import minimization as m
import pylab as p

def f(x):
    return (x - 2) ** 2


if __name__ == '__main__':
    points = []
    res = m.min(f, -5, 5, 0.01)
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

