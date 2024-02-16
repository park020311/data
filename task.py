import random
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def distance_store(store_data):
    dis = ((store_data[1]**2) + (store_data[2]**2))**0.5
    return dis

def add_node(start,data):
    new_node = Node()
    new_node.data = data
    if start is None:
        new_node.link = new_node
        return new_node
    else:
        current = start
        while current.link != start:
            current = current.link
        current.link = new_node
        new_node.link = start
        return start
def print_nodes(start):
    current = start
    while True:
        print(current.data, end='')
        current = current.link
        if current == start:
            break
        print()

if __name__ == "__main__":
    stores = []
    for i in "abcdefghij":
        x=random.randint(1, 100)
        y=random.randint(1,100)
        store = (i,x,y)
        stores.append(store)
    stores.sort(key=distance_store)
    head = None
    for store in stores:
        head = add_node(head,store)
    print_nodes(head)