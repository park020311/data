class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def print_nodes(start) :
    current = start
    if current is None :
        return
    print(current.data, end = ' ')
    while current.link is not None:
        current = current.link
        print(current.data, end = ' ')
    print()

def make_simple_linked_list(email_) :
    global head, current, pre
    print_nodes(head)

    node = Node()
    node.data = email_

    if head == None :
        head = node
        return

    if head.data[1] > email_[1]:
        node.link = head
        head = node
        return


    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > email_[1]:
            pre.link = node
            node.link = current
            return


    current.link = node


head, current, pre = None, None, None
dataArray = [["혜리", "herry@girls.com"], ["유라", "youra@girls.com"],["소진","sojin@girls.com"],["방민아","bma@girls.com"]]


if __name__ == "__main__" :

    for data in dataArray :
        make_simple_linked_list(data)

    print_nodes(head)
