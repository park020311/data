import time
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"time elapsed : {end - start}")
        return result
    return wrapper
# def factorial(number) -> int :
#     """
#     factorial by repititon
#     :param number: number(int)
#     :return: factorial result(int)
#     """
#     result = 1
#     for i in range(1, number +1):
#         result = result * i
#     return result

def factorial(number) -> int:
    """
    factorial by recursion
    :param number: number(int)
    :return: factorial(int)
    """
    if number == 1:
        return 1
    else:
        return number * factorial(number -1)

@timer
def nCr(n,r) -> int : #SRP, 0CP violation
    """
    조합 함수
    :param n:
    :param r:
    :return:
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)