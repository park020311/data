
def print_poly(t_x, p_x):
    poly_str = "P(x) = "

    for i in range(len(p_x)):
        term = t_x[i][0]
        coef = p_x[i][0]

        if (coef >= 0):
            poly_str += "+"
        poly_str += str(coef) + "x^" + str(term) + " "

    return poly_str


def calc_poly(xVal, t_x, p_x):
    ret_value = 0

    for i in range(len(px)):
        term = t_x[i][0]
        coef = p_x[i][0]
        ret_value += coef * x_value ** term

    return ret_value

tx = [[300], [20], [0]]
px = [[7], [-4], [5]]

if __name__ == "__main__":
    p_str = print_poly(tx, px)
    print(p_str)

    x_value = int(input("X 값-->"))

    px_value = calc_poly(x_value, tx, px)
    print(px_value)