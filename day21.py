class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current.link is None :
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()

def insert_node(find_data, insert_data) :
    global head, current, pre

    if head.data is find_data :
        node = Node()
        node.data = insert_data
        node.link = head
        last = head
        while last.link is not head :
            last = last.link
        last.link = node
        head = node
        return

    current = head

    while current.link is not head :
        pre = current
        current = current.link
        if current.data is find_data :
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insert_data
    current.link = node
    node.link = head

def delete_node(delete_data) :

    global head, current, pre

    if head.data == delete_data:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del (current)
        return

    current = head
    while current.link is not head:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del (current)
            return

def find_node(find_data) :
    global head, current, pre

    current = head
    if current.data == find_data:
        return current
    while current.link is not head:
        current = current.link
        if current.data is find_data:
            return current
    return Node()

head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__" :

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head


    for data in dataArray[1:] :
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head

    print_nodes(head)

    insert_node("다현", "화사")
    print_nodes(head)

    insert_node("사나", "솔라")
    print_nodes(head)

    insert_node("재남", "문별")
    print_nodes(head)

    delete_node("화사")
    print_nodes(head)

    delete_node("솔라")
    print_nodes(head)

    print(find_node("쯔위"))



