# -*- coding: utf-8 -*-
"""Assignment_7.ipynb

def subset_sum(nums: list[int], sum: int) -> bool:
    # your code here
    n = len(nums)
    dp = [[False for j in range(sum+1)] for i in range(n+1)]
    dp[0][0] = True
    for i in range(1,n+1):
        dp[i][0] = True
    
    for j in range(1,sum+1):
        dp[0][i] = False

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if(nums[i-1]<=j):
                dp[i][j] = (dp[i-1][j] or dp[i-1][j - nums[i-1]])
            else:
                dp[i][j] = dp[i-1][j] 
    return dp[n][sum]

num_list = [3, 34, 4, 12, 5, 2]
sum = 9
subset_sum(num_list,sum)

num_list = [1, 2, 4, 8]
sum = 11
subset_sum(num_list,sum)

num_list = [1, 2, 4, 8]
sum = 16
subset_sum(num_list,sum)

import sys
def min_trials(n,k):
    # n represents number of eggs and k represents number of floors.
    dp_table = [[0 for _ in range(k+1)] for _ in range(n+1)]
    # print('rows,cols:',len(dp),len(dp[0]))
    # print('before:',dp)

    for floor in range(1,k+1):
        dp_table[1][floor] = floor

    for no in range(1,n+1):
        dp_table[no][1] = 1
        dp_table[no][0] = 0

    for no in range(2,n+1):
      for floor in range(2,k+1):
          dp_table[no][floor] = sys.maxsize
          for x in range(1,floor+1):
              result = 1 + max(dp_table[no-1][x-1],dp_table[no][floor-x])
              dp_table[no][floor] = min(result,dp_table[no][floor]) 

    return dp_table[n][k]

min_trials(2,4)

import sys
def split_rope(prices, n):
    dp_table = [0 for x in range(n+1)]
    dp_table[0] = 0
    for i in range(1,n+1):
        best = -999999
        for j in range(i):
            best = max(best,prices[j]+dp_table[i-j-1])
        dp_table[i] = best
    return dp_table[n]

prices = [1, 5, 6, 9]
n = 4
split_rope(prices,n)

def sumCount(m,n,x):
    dp_table = [[0 for j in range(x+1)] for i in range(n+1)]

    # initializing the 
    for k in range(1,min(m+1,x+1)):
        dp_table[1][k] = 1


    for i in range(2,n+1):
        for j in range(1,x+1):
            for k in range(1,min(m+1,j)):
                dp_table[i][j]+=dp_table[i-1][j-k]

    return dp_table[n][x]

m = 6
n = 3
x = 8
sumCount(m,n,x)

import math
def num_combinations(code, M):
    m,n = len(code),math.floor(math.log10(M)+1)
    mod = 10**(9) + 7   
    dp_table = [0] * (m + 1)
    dp_table[0] = 1

    for i in range(m):
      if(code[i]=='0'):
          continue
      for j in range(i,m):
          if(int(code[i:j+1])>M):
              break
          dp_table[j+1] += dp_table[i]
          dp_table[j+1] %= mod
    return dp_table[m]

num_combinations('19930613',1000)

code = "3129"
M = 4000
num_combinations(code,M)

code = "500"
M = 1000
num_combinations(code,M)































