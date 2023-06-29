#!/usr/bin/env python
# coding: utf-8

# In[289]:


# def get_distance(arr):
#     sum_of_pair_distances = 0
# #     n = len(arr)
#     for i in range(32):
#         cnt = 0
#         for j in range(len(arr)):
#             if(arr[j] & (1 << i)):
#                 cnt += 1
#         sum_of_pair_distances += (cnt*(len(arr)-cnt)*2)
#     return sum_of_pair_distances


# In[291]:


# get_distance([58,72])


# In[278]:


# def move_steps(k):
#     if(k==1):
#         return 1
#     if(k==2):
#         return 2
#     answer = 0
#     answer += move_steps(k-1)+move_steps(k-2)
#     return answer


# In[279]:


# move_steps(4)


# In[280]:


# def decode_message(s):
#     message=''
#     for i in range(len(s)):
#         if(int((i+1)%3)==0 and s[i]==s[i-1]):
#             continue
#         message+=s[i]
#     return message


# In[281]:


# decode_message("this is a test")


# In[282]:


# def count_sub_strs(s: str) ->int:
#     # Count the number of substrings that have equal number of consecutive a's followed by b's or vice versa
#     groups=[1]
#     number_of_sub_strings = 0
#     for i in range(1,len(s)):
#         if(s[i]!=s[i-1]):
#             groups.append(1)
#         else:
#             groups[-1]+=1
#     for i in range(1,len(groups)):
#         number_of_sub_strings+=min(groups[i],groups[i-1])
#     return number_of_sub_strings


# In[283]:


# count_sub_strs('aabba')


# In[284]:


# def check_transformation(s1, s2):
#     # your code here
#     canTransform=True
#     map_dict={}
#     for i in range(len(s1)):
#         if(s1[i] not in map_dict):
#             map_dict[s1[i]] = s2[i]
#         else:
#             if(map_dict[s1[i]]!=s2[i]):
#                 canTransform=False
#     return canTransform


# In[285]:


# check_transformation('abb','abc')


# In[ ]:


# rmnbhv,abacde


# In[ ]:


# bcba,bcbc


# In[ ]:


# test case: aabbcddeefgghhijjkklmmnnoppqqrssttuvvwwxyyzz
# expected_result: aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz


# In[334]:


# def depth(s:str):
#     stack = []
#     max_length = 0
#     not_finished = True
#     count = 1
#     for i in range(len(s)):
#         if(i==len(s)-1):
#             not_finished = False
#         if(s[i]=="("):
#             stack.append(s[i])
#             print("i,s[i]:",i,s[i],not_finished,stack,count)
#         elif(s[i]==')'):
#             if(len(stack)==0 and not_finished):
#                 count = 0
#                 continue
#             elif(len(stack)==0):
#                 return count
#             stack.pop()
#             count += 1
#             max_length = max(max_length,count)
#             print("i,s[i]:",i,s[i],not_finished,stack,count)
#     return max_length


# In[336]:


# print(depth('()(())'))


# In[337]:


def depth(s):
    count = 0
    stack = []
    for i in range(len(s)):
        if(s[i]=='('):
            stack.append('(')
        elif(s[i]==')'):
            if(count<len(stack)):
                count = len(stack)
            stack.pop()
    return count


# In[338]:


depth('()(())')


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




