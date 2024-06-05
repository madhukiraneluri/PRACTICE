#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Node:
    
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
        
class Linked_List:
    
    
    def __init__(self):
        self.head=None
        
        
        
        
    def insert(self,val):#method to insert only one value
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            new_node.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            
            
            #method overloading
            

    def __repr__(self):
        temp = self.head
        ans = ''
        if temp:
            while True:
                ans += str(temp.data) + " -> "
                temp = temp.next
                if temp == self.head:
                    break
        return ans
    
ll=Linked_List()
ll.insert(1)
ll.insert(2)
ll.insert(5)
print(ll)


# In[ ]:





# In[ ]:




