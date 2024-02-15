import random
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def linked_list(rand):
    head = Node()
    head.data = rand[0]
    current = head

    for num in rand[1:]:
        node = Node()
        node.data = num
        current.link = node
        current = node

    return head
    
if __name__ == "__main__":
    Lotto = [random.randint(1,45)for i in range(6)]
    head = linked_list(Lotto)

    while head:
        print(head.data)
        head = head.link


