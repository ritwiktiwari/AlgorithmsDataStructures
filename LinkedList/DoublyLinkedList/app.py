from DoublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList()
dll.insert_at_beginning(5)
dll.insert_at_beginning(4)
dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)
dll.insert_at_end(6)
dll.insert_at_end(7)
dll.insert_at_end(8)
dll.insert_at_end(9)
print(dll.traverse_forward())
dll.insert_after_position(150, 5)
print(dll.traverse_forward())
dll.delete_at_beginning()
print((dll.traverse_forward()))
dll.delete_at_end()
print(dll.traverse_forward())
dll.delete_after_position(4)
print(dll.traverse_forward())