__author__ = 'Danil Radkovsky, Stas Chmilenko'

def f(x):
    return (x - 3) ^ 2

def min(f, a, b, eps):
    delta = (b - a) / 1000
    x1 = (a + b) / 2 - delta
    x2 = (a + b) / 2 + delta

    if f(x1) < f(x2):

        if (x2 - (a + b) / 2) < eps:

            x_min = (x2 + a) / 2

            return f(x_min), x_min

        else:
            return min(f, a, x2, eps)

    else:

        if ((a + b) / 2 - x1) < eps:

            x_min = (b + x1) / 2

            return f(x_min), x_min

        else:
            return min(f, x1, b, eps)

if __name__ == '__main__':
    print(min(f, -5, 5, 0.1))
