def print_poly(f_x,t_x) -> str:

    poly_expression = "f(x) = "

    for i in range(len(fx)):
        term = t_x[i]
        coefficient = f_x[i]
        if coefficient >= 0 and i !=0 :
            poly_expression = poly_expression + "+"
        poly_expression = poly_expression + f"{coefficient}x^{term} "


    return poly_expression

def calculation_poly(xVal, f_x,t_x):
    return_value = 0


    for i in range(len(fx)):
        term = t_x[i]
        coef = f_x[i]
        return_value += coef * pow(xVal,term)


    return return_value
tx= [300,20,0]
fx = [7,-4,5]
#x=0일때 오류남. 상수일때 x^0 이 붙지 않게 바꿔야함..

if __name__ == "__main__":

    print(print_poly(fx,tx))
    print(calculation_poly(int(input("X 값--> ")), fx,tx))