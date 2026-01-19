from linked_list import LinkedList

ll = LinkedList()

ll.insert_at_start(10)
ll.insert_at_start(20)
ll.insert_at_start(30)
ll.insert_at_start(40)
ll.insert_at_start(50)

ll.display()

ll.insert_at_end(9)
ll.insert_at_end(8)
ll.insert_at_end(7)
ll.insert_at_end(6)
ll.insert_at_end(5)

ll.display()

ll.insert_at_index(2,100)
ll.display()

ll.delete_at_end()
ll.display()

ll.delete_at_start()
ll.display()