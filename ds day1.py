#!/usr/bin/env python
# coding: utf-8

# In[23]:


'''
Linked List implementation
'''

class Node:
    
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
        
class Linked_List:
    
    
    def __init__(self):
        self.head=None
        
        
        
        
    def insert(self,val):#method to insert only one value
        if self.head==None:
            self.head=Node(val)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(val)
            
            #method overloading
            
    def insert(self,*l):#method to insert more than one value
        l=list(l)
        for val in l:
            if self.head==None:
                self.head=Node(val)
            else:
                temp=self.head
                while temp.next!=None:
                    temp=temp.next
                temp.next=Node(val)
                
                
    def insert_at_begin(self,val):
        node=Node(val)
        node.next=self.head
        self.head=node
                
    def __repr__(self):#magic method to print object
        temp=self.head
        ans=''
        while temp.next!=None:
            ans+=str(temp.data) + " -> "
            temp=temp.next
        ans+=str(temp.data)
        return ans
    
    
ll=Linked_List()
ll.insert(1)
ll.insert(2)
ll.insert(5)
ll.insert(5,7,8,9,10)
ll.insert_at_begin(111)
print(ll)


# In[27]:


"""
Doubly Linked List
"""
class Node:
    
    
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
        
        
class Doubly_Linked_List:
    
    
    def __init__(self):
        self.head=None
    
    def insert(self,val):
        if self.head==None:
            self.head=Node(val)
        else:
            new_node=Node(val)
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
            
    def __repr__(self):
        if self.head is None:
            return "Empty Doubly Linked List"
        linked_list_str = ""
        temp = self.head
        while temp is not None:
            linked_list_str += str(temp.data)
            if temp.next is not None:
                linked_list_str += " <-> "
            temp = temp.next
        return linked_list_str
    def insert_at_begin(self,val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        
dll=Doubly_Linked_List()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert_at_begin(111)
print("Original Doubly Linked List:", dll)


# In[13]:





# In[ ]:





# In[ ]:




