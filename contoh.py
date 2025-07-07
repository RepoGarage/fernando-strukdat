#!/usr/bin/env python

from typing import Optional

def array():
    a: list[int] = [1, 2, 3];
    print(f"the value of array are : {a}")
    return

class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def append(self, ll):
        current = self
        while current.next is not None:
            current = current.next
        current.next = ll

    def print_list(self):
        current = self
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def linkedlist():
    a: LinkedList = LinkedList(1)
    b: LinkedList = LinkedList(20)
    a.append(b)
    print("the value of LinkedList are : ", end="")
    a.print_list()
    return

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def length(self):
        return len(self.stack)

def stack():
    print("it just an array that use LIFO (Last in First Out) principle. Check the source code.")
    return

class Queue:
    def __init__(self):
        self.begin: Optional[LinkedList] = None
        self.end: Optional[LinkedList] = None
        self.len = 0

    def push(self, data):
        node = LinkedList(data)
        if self.begin is None:
            self.begin = node
            self.end = node
        else:
            # not really needed, but just to please the python lsp...
            if self.end is None:
                self.end = node
                return
            # -----------------------
            self.end.next = node
            self.end = node
        self.len += 1

    def dequeue(self):
        if self.begin is None:
            return None
        data = self.begin.data
        self.begin = self.begin.next
        self.len -= 1
        return data

    def get_current(self):
        if self.begin is None:
            return None
        return self.begin.data

def queue():
    a: Queue = Queue()
    a.push(5)
    if a.begin and a.end is not None:
        print(f"the current queue are : {a.begin.data}")
        a.push(2)
        print(f"the end queue are : {a.end.data}")
        a.dequeue()
        print("will dequeue...")
        print(f"the current queue are : {a.begin.data}")
        print(f"the end queue are : {a.end.data}")
    return

def tree():
    print("Its a linked list but not only 1 link but more.")

def heap():
    print("NOT YET IMPLEMENTED")

def trie():
    print("NOT YET IMPLEMENTED")

def set_():
    print("NOT YET IMPLEMENTED")

def graph_with_weight():
    print("NOT YET IMPLEMENTED")

if __name__ == "__main__":
    array()
    linkedlist()
    stack()
    queue()
    tree()
    heap()
    trie()
    set_()
    graph_with_weight()
