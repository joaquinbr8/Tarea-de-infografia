def get_line(x0, y0, x1, y1):
    points = [(x0, y0)]
    dx = x1 - x0
    dy = y1 - y0
    xk = x0
    yk = y0
    # parametro de decision inicial
    Pk = 2 * dy - dx

    while xk < x1:
        xk += 1
        if Pk < 0:
            Pk = Pk + 2 * dy
        else:
            Pk = Pk + 2 * dy - 2 * dx
            yk += 1
        points.append((xk, yk))

    return points


if __name__ == "__main__":
    x0 = 20
    y0 = 22
    x1 = 300
    y1 = 250
    points = get_line(x0, y0, x1, y1)
    print(points)