from zad2testy import runtests


class Node:
    def __init__(self):
        self.val = None
        self.next = None


# def insert_element(p, element):
#     while p.next is not None and p.next.val < element.val:
#         p = p.next
#
#     element.next = p.next
#     p.next = element
#
#
# def SortH(p, k):
#     # tu prosze wpisac wlasna implementacje
#     sorted_head = Node()
#     while p is not None:
#         q = p.next
#         insert_element(sorted_head, p)
#         p = q
#
#     return sorted_head.next

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def heapify_min(arr, n, i):
    l = left(i)
    r = right(i)
    min_ind = i

    if l < n and arr[l] < arr[min_ind]:
        min_ind = l

    if r < n and arr[r] < arr[min_ind]:
        min_ind = r

    if min_ind != i:
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
        heapify_min(arr, n, min_ind)

def build_heap(arr, n):
    for i in range(parent(n - 1), -1, -1):
        heapify_min(arr, n, i)


from queue import PriorityQueue


def SortH(p, k):
    head_sorted = Node()
    q = PriorityQueue()
    for _ in range(k + 1):
        q.put(p.val)
        p = p.next

    tail = head_sorted
    while p is not None:
        new_element = Node()
        new_element.val = q.get()
        tail.next = new_element
        tail = tail.next
        q.put(p.val)
        p = p.next

    while not q.empty():
        new_element = Node()
        new_element.val = q.get()
        tail.next = new_element
        tail = tail.next


    return head_sorted.next




runtests( SortH )
