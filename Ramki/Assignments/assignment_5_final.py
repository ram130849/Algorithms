# -*- coding: utf-8 -*-
"""Assignment_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DjaeXu45N5w3vPK3Nc-vv5M9gHn_3Nmx
"""

import math
import copy

def DTB(n):
    return bin(n).replace("0b", "")

class amor_dict():
    def __init__(self, num_list = []):
        n = len(num_list)
        if(n<=1):
            k = 0
        else:
            k = math.ceil(int(math.log(n)))+1
        self.total_items = 0
        self.amor_list = [[] for _ in range(k+1)]
        binary_no = list(DTB(n))
        count = 0
        new_list = num_list
        for i in range(len(binary_no)-1,-1,-1):
            no_items = ((2**count)*int(binary_no[i])) 
            if(int(binary_no[i])==1):
                self.amor_list[count].extend(sorted(list(set(new_list).difference(new_list[:-no_items]))))
                new_list = new_list[:-no_items]
                self.total_items += no_items
            count+=1
        self.levels = len(self.amor_list)

    def merge(self,arr1,arr2):
        if(len(arr1)==0):
            return arr2
        if(len(arr2)==0):
            return arr1
        result = []
        i = j = 0
        total = len(arr1) + len(arr2)
        while(len(result)<total):
            if(arr1[i] < arr2[j]):
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
            if(i==len(arr1) or j==len(arr2)):
                result.extend(arr1[i:] or arr2[j:])
                break
        return result

    def insert(self, num):
        arr = [num]
        self.total_items+=1
        k = math.ceil(int(math.log(self.total_items)))+2
        i=0
        while(i<len(self.amor_list)):
            arr = self.merge(arr,self.amor_list[i])
            self.amor_list[i].clear()
            if(len(arr)<=2**(i)):
                self.amor_list[i].extend(arr)
                break
            if(i==len(self.amor_list)-1 and k>len(self.amor_list)):
                self.amor_list.append([])
            i+=1
        if(self.amor_list[-1]==[]):
            last = self.amor_list.pop()
        
    
    def search(self, num):
        n_levels = len(self.amor_list)
        for level in range(n_levels):
            arr = self.amor_list[level]
            if(len(arr)==1):
                if(arr[0]==num):
                    return level
                continue
            if(len(arr)==2):
                if(arr[0]==num or arr[1]==num):
                    return level
                continue
            left = 0 
            right = len(arr)-1
            while(left<=right):
                mid = (left + right)//2
                if(arr[mid]==num):
                    return level
                elif(arr[mid]>num):
                    right = mid-1
                else:
                    left = mid+1
        return -1

    def print(self):
        # your code here
        t = []
        temp_dict = copy.deepcopy(self.amor_list)
        for i in range(len(temp_dict)):
            t.append(temp_dict[i])
        return t

ad = amor_dict([10])
print(ad.print())
# [[], [], [12, 23, 24, 42]]
ad.insert(10)
print(ad.print())
# # [[11], [], [12, 23, 24, 42]]
ad.insert(16)
print(ad.print())
# # [[], [11, 74], [12, 23, 24, 42]]
ad.insert(18)
print(ad.print())
# # 1
ad.insert(18)
print(ad.print())
# # -1
ad.insert(20)
print(ad.print())



def implement_queue(operations):
    s1 = []
    s2 = []
    output = []
    
    for ops in operations:
        if(ops.startswith("push")):
            _, x = ops.split("(")
            s1.append(int(x[:-1]))
        elif(ops == "pop()"):
            if(len(s2)==0):
                while(len(s1)>0):
                    s2.append(s1.pop())
            output.append(s2.pop() if(s2) else "#")
        elif(ops == "peek()"):
            if(len(s2)==0):
                while(len(s1)>0):
                    s2.append(s1.pop())
            output.append(s2[-1] if(s2) else "#")
        elif(ops == "empty()"):
            output.append(not(s1 or s2))
        else:
            output.append("#")
            
    return output

operations = ["empty()","push(7)", "push(2)","push(3)", "peek()", "pop()","pop()", "empty()", "pop()", "empty()"]
# output = [1, 1, False, 2, True]

ans = implement_queue(operations) 
print(ans)

operations = ["push(1)", "push(2)", "peek()", "pop()", "empty()", "pop()", "empty()"]
ans = implement_queue(operations) 
print(ans)
output = [1, 1, False, 2, True]
print(output)






























