class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    #  Display a linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data , end = " -> ")
            temp = temp.next
        print("None")

    
    # Insertion At start

    def insert_at_start(self,data):
        print(f"Inserting {data} at start")
        node = Node(data)
        node.next = self.head
        self.head = node

    # Insertion at End

    def insert_at_end(self,data):
        print(f"Inserting {data} at end")
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        temp = self.head 
        while temp.next:
            temp = temp.next
        
        temp.next = node
    
    # Insertion at any index

    def insert_at_index(self,idx,data):
        print(f"Inserting {data} at index {idx}")
        if idx == 0:
            insert_at_start(data)
            return
        
        node = Node(data)
        temp = self.head
        for _ in range(idx-1):
            if temp is None:
                print("Index out of Range")
                return
            temp = temp.next
        
        node.next = temp.next 
        temp.next = node 


    
    # Deletion at start

    def delete_at_start(self):
        print("Deleting node at start")
        if self.head is None:
            print("Empty list")
            return
        
        if self.head.next is None:
            self.head = None 
            return
        
        self.head = self.head.next

    # deletion at end

    def delete_at_end(self):
        print("Deleting node at end")
        if self.head is None:
            print("Empty list")
            return
        
        temp = self.head 
        while temp.next.next :
            temp = temp.next
        temp.next = None 


    # Delete at any index

    def delete_at_index(self,idx):
        print("Deleting node at index {idx}")
        if self.head is None:
            print("Empty list")
            return
        
        if idx == 0:
            delete_at_start()
            return
        
        temp = self.head
        for _ in range(idx-1):
            if temp is None or temp.next is None : 
                print("Index Out of bound")
                return
            temp = temp.next 
        
        temp.next = temp.next.next 