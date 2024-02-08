def print_poly(f_x) -> str:
    term = len(f_x) - 1
    poly_expression = "f(x) = "

    for i in range(len(fx)):
        coefficient = f_x[i]
        if coefficient == 0:
            term = term -1
            continue
        elif coefficient >= 0 and i !=0 :
            poly_expression = poly_expression + "+"
        poly_expression = poly_expression + f"{coefficient}x^{term} "
        term = term - 1

    return poly_expression

def calculation_poly(xVal, f_x):
    return_value = 0
    term = len(f_x) - 1  

    for i in range(len(fx)):
        coef = f_x[i]
        return_value += coef * pow(xVal,term)
        term = term - 1

    return return_value

fx = [2,3, 4, 0, -9]


if __name__ == "__main__":

    print(print_poly(fx))
    print(calculation_poly(int(input("X 값--> ")), fx))