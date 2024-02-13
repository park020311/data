import webbrowser
import time


def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else :
        return False

def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    else :
        return False

def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if is_stack_empty() :
        print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("스택이 비었습니다.")
        return None
    return stack[top]

def check_bracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass
    if is_stack_empty():
        return True
    else:
        return False


SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1


if __name__ == "__main__":
    urls = ['naver.com', 'daum.net', 'nate.com']

    exprAry = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']

    for expr in exprAry:
        top = -1
        print(expr, '==>', check_bracket(expr))
