class Node():
    def __init__(self):
        self.data = None
        self.link = None

def add_data(katok_list,new):
    kLen = len(katok_list)
    index = 0
    count = new[1]
    while index < kLen and katok_list[index][1]>count:
        index = index + 1

    katok_list.insert(index,new)

katok = [('다현',200),("정연",150),('쯔위',90),('사나',30),('지효',15)]

if __name__ == "__main__":
    add_data(katok,('미나',40))
    print(katok)