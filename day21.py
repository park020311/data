import random

## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current.link is None:
        return
    print(current.data, end=' ')
    while current.link is not start:
        current = current.link
        print(current.data, end=' ')
    print()

def  count_odd_even() :
    global head, current, pre

    odd, even = 0, 0
    if head is None :
        return False

    current = head
    while True:
        if current.data % 2 == 0:
            even += 1
        else :
            odd += 1
        if current.link is not head :
            break
        current = current.link

    return odd, even

def make_zero_number(odd, even):

    if odd > even :
        reminder = 1
    else :
        reminder = 0

    current = head
    while True:
        if current.data % 2 is reminder:
            current.data *= -1
        if current.link is head :
            break
        current = current.link


head, current, pre = None, None, None


if __name__ == "__main__":

    data_array = [random.randint(1, 100) for _ in range(7)]

    node = Node()
    node.data = data_array[0]
    head = node
    node.link = head


    for data in data_array[1:] :
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head


    print_nodes(head)

    oddCount, evenCount = count_odd_even()
    print('홀수 -->', oddCount, '\t', '짝수 -->', evenCount)

    make_zero_number(oddCount, evenCount)
    print_nodes(head)
