class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def reorder_students(head):
    if not head or not head.next:
        return None
    prev = None
    slow = head
    fast = head 
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Detach second half from first half
    prev.next = None
    second_half_start =  slow

    # 3 pointers to reverse the second half
    prev = None
    current = second_half_start
    nextt = None
    while current:
        nextt = current.next
        current.next = prev
        prev = current 
        current = nextt

    return print_list(prev)

# Create a linked list with 6 nodes: A -> B -> C -> D -> E -> F
head = Node("A")
head.next = Node("B")
head.next.next = Node("C")
head.next.next.next = Node("D")
head.next.next.next.next = Node("E")
head.next.next.next.next.next = Node("F")

# Print original list
print("Original list:")
print_list(head)

# Reorder students
print("Reversed second half list:")
reorder_students(head)
