__author__ = 'Danil Radkovsky, Stas Chmilenko'


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

