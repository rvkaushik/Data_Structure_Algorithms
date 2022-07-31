

class Node:
    def __init__(self, data, next=None, previous= None):
        self.data = data
        self.next = next
        self.prev = previous
    


def insert_end(ll, data):
    pass


def print_singly_ll(ll):
    while ll:
        print(ll.data)
        ll=ll.next
    print("LINK List ENDed")


def print_doubly_ll(ll):
    while ll.next:
        print("data ------- ", ll.data)
        print("next ------- ", ll.next.data)
        print("prev ------- ", ll.previous.data)
        ll=ll.next
    print("Last Node data ------- ", ll.data)
    print("prev ------- ", ll.previous.data)
    print("LINK List ENDed")

def create_singly_ll(array):
    head = Node(None)
    temp = head

    for data in array:
        node = Node(data)
        head.next = node
        head = head.next

    head = temp.next
    print_singly_ll(head)

def create_doubly_ll(array):
    head = Node(None)
    temp =head
    for data in array:
        node = Node(data)
        head.next = node
        node.previous = head
        head = node
    head = temp.next
    print_doubly_ll(head)

def main():
    array = [0, 1 ,2 ,3]
    create_singly_ll(array)
    create_doubly_ll(array)

if  __name__ == "__main__":
    main()