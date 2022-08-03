
import os
import sys

sys_path = os.getcwd()
sys.path.append(sys_path)

from Medium.utils import Node

class SinglyLinkedList:
    def __init__(self) -> None:
        self.linked_list = None

    def get_node_from_index(self, index):
        """
        """
        count = 1
        head = self.linked_list
        while count <= index and head:
            if count == index:
                return head.data
            head = head.next
            count+=1
        
        return -1

    def add_at_head(self, data):
        """
        """
        node = Node(data)
        node.next = self.linked_list
        self.linked_list = node

    def add_at_tail(self, data):
        """
        """
        node = Node(data)
        head = self.linked_list
        while self.linked_list.next:
            self.linked_list = self.linked_list.next
        
        self.linked_list.next = node
        self.linked_list = head

    def print_list(self):
        head = self.linked_list
        print("Singly Linked List: ")
        while head:
            print(head.data, end="->")
            head = head.next
        print()

    def add_at_index(self, index, value):
        """
        """
        
        head = self.linked_list
        count = 1
        node = Node(value)
        if index == 0:
            node.next = self.linked_list.next
            self.linked_list = node
        else:
            while count <=index and self.linked_list:
                if count == index:
                    node.next = self.linked_list.next
                    self.linked_list.next = node
                
                self.linked_list = self.linked_list.next
                count+=1
            
            self.linked_list = head

    def delete_at_index(self, index):
        """
        """
        head = self.linked_list
        count = 0
        prev = self.linked_list
        if index == 0 and self.linked_list.next:
            self.linked_list = self.linked_list.next
        else:
            while count <= index and self.linked_list:
                self.linked_list = self.linked_list.next
                count+=1
                if count == index:
                    prev.next = self.linked_list.next
                prev = self.linked_list

            self.linked_list = head

def main():
    ll = SinglyLinkedList()
    ll.add_at_head(10)
    ll.add_at_head(20)
    ll.add_at_head(30)
    ll.add_at_tail(5)
    ll.add_at_tail(1)
    ll.add_at_head(40)
    ll.add_at_index(5, 999)
    ll.print_list()
    ll.delete_at_index(1)
    ll.print_list()

    print(ll.get_node_from_index(10))



if __name__ == "__main__":
    main()


    



