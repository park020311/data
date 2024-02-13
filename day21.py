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

def insert_node(findData, insertData) :
    global memory, head, current, pre

    if head.data is findData :
        node = Node()
        node.data = insertData
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
        if current.data is findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node
    node.link = head


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