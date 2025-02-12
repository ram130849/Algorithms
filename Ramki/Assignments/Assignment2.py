#!/usr/bin/env python
# coding: utf-8

# In[251]:


def postfix_string(arr):
    postfix=[]
    i=0
    while(i<len(arr)):
        if(type(arr[i])==int or arr[i].isalpha() or arr[i]==''):
            postfix.append(arr[i])
        if(arr[i]=='+' and len(postfix)>1):
            var1 = postfix.pop()
            var2 = postfix.pop()
            postfix.append(var2+var1)
        elif(arr[i]=='-' and len(postfix)>1):
            var1 = postfix.pop()
            var2 = postfix.pop()
            postfix.append(var2[:var1] + var2[var1+1:])
        elif(arr[i]=='*' and len(postfix)>1):
            var1 = postfix.pop()
            var2 = postfix.pop()
            postfix.append(var1*var2)
        i+=1 
    result = postfix.pop()
    return result


# In[255]:


X= ['a','b','+','c','+','d','+','e','+',3,'-']
postfix_string(X)


# In[230]:


class ListNode():
      def __init__(self, val, next=None):
            self.val = val
            self.next = next

class AstronomicalInt():
        def convert(self, num:str) -> ListNode:
            if(num is None or num==''):
                return None
            head_node = ListNode(int(num[0]))
            n = len(num)
            curr_node = head_node
            for i in range(n-1):
                curr_node.next = ListNode(int(num[i+1]))
                curr_node = curr_node.next 
            return head_node
    
        def reverse(self,num:ListNode) -> ListNode:
            if(num is None or num.next is None):
                return num
            prev_node = None
            next_node = None
            curr_node = num
            while(curr_node):
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
            num = prev_node
            return num
        
        def add(self, num1:ListNode, num2: ListNode) -> ListNode:
            # Returns head of new linked list after adding the given lists
            num1 = self.reverse(num1)
            num2 = self.reverse(num2)
            sum_val = 0
            carry = 0
            add_result = None
            prev = None
            while(num1 or num2):
                sum_val = carry + (num1.val if num1 else 0) + (num2.val if num2 else 0) 
                carry = 1 if sum_val>=10 else 0
                sum_val %= 10
                temp = ListNode(sum_val)
                if(add_result is None):
                    add_result = temp
                else: 
                    prev.next = temp
                prev = temp
                if(num1 is not None):
                    num1 = num1.next
                if(num2 is not None):
                    num2 = num2.next
            if(carry>0):
                prev.next = ListNode(carry)
            ans = self.reverse(add_result)
            return ans

        def to_string(self, head):
            num = []
            curr = head
            while(curr):
                num.append(curr.val)
                curr = curr.next
            num = ''.join([str(i) for i in num])
            return num


# In[231]:


ast = AstronomicalInt()
n1 = ast.convert("1234")
n2 = ast.convert("16")


# In[232]:


print(ast.to_string(n1))
print(ast.to_string(n2))


# In[233]:


n3 = ast.add(n1, n2)
print(n3)


# In[234]:


print(ast.to_string(n3))


# In[265]:


# Import the collections module
from collections import defaultdict

def countAtoms(formula):
    var = formula
    n=len(var)
    count_map = defaultdict(int)
    st = [1]
    digits = ""
    lower = ""
    for i in range(n-1,-1,-1):
        if(var[i].isdigit()):
            digits = var[i] + digits
            continue
        elif(var[i].islower()):
            lower = var[i] + lower
            continue
        elif(var[i] == ')'):
            st.append(st[-1]*int(digits or 1))
            digits = ''
            continue
        elif(var[i] == '('):
            st.pop()
            continue
        else:
            element = var[i]+lower
            count_map[element] = count_map[element] + (st[-1]*int(digits or 1))
            digits = ''
            lower = ''
    
    string = ''
    count_map = sorted(count_map.items())
    for key,value in count_map:
        string += key + str('' if(value==1) else value)
    return string


# In[269]:


countAtoms('K4(Fe(CN)6)')


# In[271]:


def combination_check(n,st):
    n = str(n)
    st = st.split(" ")
    unique_digits = list(sorted(set(n)))
    unique_words = list(set(st)) if(len(st) != len(set(st))) else st
    if(len(n)!=len(st)):
        return False
    for i in range(len(n)):
        first_idx = unique_digits.index(n[i])
        second_idx = unique_words.index(st[i])
        if(first_idx!=second_idx):
            return False
    return True


# In[273]:


combination_check(123123,'ape cat dog ape cat dog')


# In[189]:


# Reference: https://www.geeksforgeeks.org/sum-of-maximum-elements-of-all-possible-sub-arrays-of-an-array/.
def diff_max_min(arr):
    difference_max_min = 0
    n = len(arr)
    
    # Calculate maximum from all the contiguous subarray.
    left_sum = [0]*n
    right_sum = [0]*n
    
    max_stack = []
    for i in range(0,n):
        while(len(max_stack)>0 and arr[max_stack[-1]]<=arr[i]):
            left_sum[i] += left_sum[max_stack[-1]] + 1
            max_stack.pop()
        max_stack.append(i)
    max_stack.clear()
    
    for j in range(n-1,-1,-1):
        while(len(max_stack)>0 and arr[max_stack[-1]]<arr[j]):
            right_sum[j] += right_sum[max_stack[-1]] + 1
            max_stack.pop()
        max_stack.append(j)
    max_stack.clear()
    
    max_sum = 0
    # Calculate the final sum.
    for i in range(0,n):
        max_sum += (left_sum[i]+1)*(right_sum[i]+1)*arr[i] 
    
    # Calculate minimum from all the contiguous subarray.
    left_sum = [0]*n
    right_sum = [0]*n
    
    min_stack = []
    for i in range(0,n):
        while(len(min_stack)>0 and arr[min_stack[-1]]>=arr[i]):
            left_sum[i] += left_sum[min_stack[-1]] + 1
            min_stack.pop()
        min_stack.append(i)
    min_stack.clear()    
    
    for j in range(n-1,-1,-1):
        while(len(min_stack)>0 and arr[min_stack[-1]]>arr[j]):
            right_sum[j] += right_sum[min_stack[-1]] + 1
            min_stack.pop()
        min_stack.append(j)
    min_stack.clear()
    
    min_sum = 0
    # Calculate the final sum.
    for i in range(0,n):
        min_sum += (left_sum[i]+1)*(right_sum[i]+1)*arr[i]
        
#     print("max_sum:",max_sum)
#     print("min_sum:",min_sum)
    difference_max_min = max_sum - min_sum
    return difference_max_min


# In[190]:


arr = [3,1,2]
diff_max_min(arr)


# In[163]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




