__author__ = 'Danil Radkovsky, Stas Chmilenko'

def f(x):
    return (x - 2) ** 2

def min(f, a, b, eps):
    delta = (b - a) / 1000.0
    x1 = (a + b) / 2 - delta
    x2 = (a + b) / 2 + delta

    if f(x1) < f(x2):

        if (x2 - a) < eps:

            x_min = (x2 + a) / 2

            return f(x_min), x_min

        else:
            return min(f, a, x2, eps)

    else:

        if (b - x1) < eps:

            x_min = (b + x1) / 2

            return f(x_min), x_min

        else:
            return min(f, x1, b, eps)

if __name__ == '__main__':
    print("%.2f %.2f " % min(f, -5, 5, 0.01))
