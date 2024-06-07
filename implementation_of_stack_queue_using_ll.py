#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,val):
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            self.head=newnode
            newnode.next=temp
    def pop(self):
        pop_node=None
        if self.head is None:
            sys.exit("POP cant be done cuz stack is empty")
        pop_node=self.head
        self.head=self.head.next
        return pop_node.data
    def __repr__(self):#magic method to print object
        temp = self.head
        ans = ''
        while temp is not None:
            ans += str(temp.data) + " -> "
            temp = temp.next
        return ans[:-4]
    #peak means self.head.data will be returned
    
stack=Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.pop()


# In[12]:


print(stack)


# In[23]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def isEmpty(self):
        return self.rear==None
    def enQueue(self,val):
        newnode=Node(val)
        if self.isEmpty():
            self.front=self.rear=newnode
        self.rear.next=newnode
        self.rear=newnode
    def deQueue(self):
        deque_node=None
        if self.isEmpty():
            return "Cant be dequeued queue is empty"
        deque_node=self.front
        self.front=self.front.next
        if self.front==None:
            self.rear=None
        return deque_node.data
    def __repr__(self):#magic method to print object
        temp = self.front
        ans = 'EXISTING QUEUE\n'
        while temp is not self.rear:
            ans += str(temp.data) + " -> "
            temp = temp.next
        return ans+str(self.rear.data)
    #peak means self.head.data will be returned
    
q=Queue()
q.enQueue(10)
q.enQueue(11)
print(q)
q.deQueue()
print(q)
q.enQueue(15)
q.enQueue(18)
print(q)
q.deQueue()
print(q)


# In[ ]:




