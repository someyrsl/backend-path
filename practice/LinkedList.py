# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)

# new_node = Node(5)
# new_node.next = head
# head = new_node

# new_node = Node(15)
# new_node.next = head.next
# head.next = new_node

# # new_node = Node(40)

# # current = head

# # while current.next:
# #     current = current.next

# # current.next = new_node
# # head = head.next
# # head.next.next = head.next.next.next
# current = head
# print(current.next.next.value)

# while current.next.next:
#     current = current.next

# current.next = None
# while current:
#     print(current.value, end = " -> ")
#     current = current.next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next

def length(head):
    link_count = 0
    current = head
    while current is not None:
        link_count += 1
        current = current.next
    return link_count

def prepend(head,value):
    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head

def append(head, value):
    if head is None:
        return prepend(head, value)
    new_node = Node(value)
    current = head
    while current.next: 
        current = current.next
    current.next = new_node
    return head

def find(head, value) -> bool:
    current = head
    while current is not None:
        if current.value == value:
            return True
        current = current.next
    return False

def delete(head, value):
    if head is None:
        return head
    if head.value == value:
        head = head.next
        return head
    previous = head
    current = head.next
    while current is not None:
        if current.value == value:
            previous.next = current.next
            return head
        previous = current
        current = current.next
    return head

def reverse(head):
    previous = None
    current = head
    while current is not None:
        next_link = current.next
        current.next = previous
        previous = current
        current = next_link
    return previous
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
# print_list(head)    # 1, 2, 3 (по строке)
# print(length(head)) # 3
# print(length(None)) # 0  (пустой список)

# head = prepend(head, 0)
# print_list(head)    # 0, 1, 2, 3, 4
# print(length(head)) # 5
# head = append(None, 7)
# print_list(head)    # 7

# head = delete(head, 3)    # 1, 2, 4
# print_list(head)
# head = delete(head, 4)    # 1, 2
# print_list(head)
# head = delete(head, 99)   # без изменений
# print_list(head)
# head = delete(head, 1)    # 2
# print_list(head)
# head = delete(head, 2)    # None
# print_list(head)
head = reverse(head)
print_list(head)             # 3, 2, 1
print_list(reverse(None))    # пусто, без ошибки