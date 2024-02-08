class Node:
    def __init__ (self) :
        self.data = None
        self.link = None

def print_nodes(start) :
    current = start
    if current is None :
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link
        print(current.data, end=' ')
    print()

def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data == find_data:
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insert_data
    current.link = node
def delete_node(delete_data) :
    global head, current, pre

    if head.data == delete_data :
        current = head
        head = head.link
        print(f"{delete_data}이(가) 삭제됨")
        del(current)
        return

    current = head
    while current.link is not None :
        pre = current
        current = current.link
        if current.data == delete_data :
            pre.link = current.link
            print(f"{delete_data}이(가) 삭제됨")
            del(current)
            return
    print(f"{delete_data}은(는) 삭제할 수 없음")

def find_node(find_data) :
    global head, current, pre

    current = head
    if current.data == find_data :
        return current
    while current.link is not None :
        current = current.link
        if current.data == find_data :
            return current
    return Node()

head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효", "태간"]

if __name__ == "__main__" :
    node = Node()
    node.data = dataArray[0]
    head = node
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
    print_nodes(head)
    insert_node("다현","화사")
    print_nodes(head)
    insert_node("사나","솔라")
    print_nodes(head)
    insert_node("정국","문별")
    print_nodes(head)
    delete_node("쯔위")
    print_nodes(head)
    delete_node("정국")
    print(head)
    print(find_node("다현").data)
    print(find_node("재남").data)
    print(find_node("사나").data)