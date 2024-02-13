def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("스택이 비었습니다")
        return
    return stack[top]

SIZE = 5
stack = ["커피", "사이다", "아이스티", "흑당버블밀크티", None]
top = 3

print(stack)
retData = pop()
print("추출한 데이터 -->", retData)
print(stack)
retData = pop()
print("추출한 데이터 -->", retData)
