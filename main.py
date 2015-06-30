__author__ = 'Danil Radkovsky, Stas Chmilenko'
import minimization as m




def f(x):
    return (x - 2) ** 2


if __name__ == '__main__':
    print("%.2f %.2f " % m.min(f, -5, 5, 0.01))
