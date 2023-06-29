# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
import math
from collections import deque

def minimumCost(n:int,connections:list[list[int]]):
    if(n==1):
        return connections[0][2]
    # Find function to determine the parent of the current node.
    def find(x):
        if(par[x]!=x):
            par[x] = find(par[x])
        return par[x]

    par = list(range(n))
    # sorting the connections by minimum cost order from smallest to largest based on their weights.
    connections.sort(key=lambda x: x[2])
    # total cost of the connections
    ans = 0
    for x,y,cost in connections:
        x,y = x-1, y-1
        # if both the parent of current and neighbor matches then we don't add the cost of the edge in the total cost.
        if(find(x)==find(y)):
            continue
        # make the parent of the neighbor as the parent for the current node. (Union of the sets) 
        par[find(x)] = find(y)
        ans += cost
        n -= 1
        if(n==1):
            return ans
    return -1

n = 1
connections = [[1,1,0]]
minimumCost(n,connections)
# Output: 5

n = 4
connections = [[1,2,3],[3,4,4]]
minimumCost(n,connections)
# Output: -1

def is_feasible_graph(n, edges_list):
    if(n==1 or len(edges_list)==0 or (not edges_list)):
        return True
    # creating a graph from the edge list
    graph = [[] for i in range(n)]
    for (u,v) in edges_list:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n
    color[0] = 0
    queue = deque([0])
    
    while(len(queue)>0):
        node = queue.popleft()
        for neighbor in graph[node]:
            if(color[neighbor] == -1):
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            elif(color[neighbor] == color[node]):
                return False
    return True

n = 1
edges_list=[]
is_feasible_graph(n,edges_list)
# False

n = 3
edges_list = [[0,1], [1,2]]
is_feasible_graph(n,edges_list)
# True





import math
def word2int(word):
    base = 32 # assuming we have 26 lowercase letters and 6 special characters
    res = 0
    n = len(word)-1
    for i,c in enumerate(word[:-1]):
        res += ((ord(c)-97+1) * (base**(n))) 
        n-=1
    res += (ord(word[-1]) - 97+1)
    return res

def get_min_C_value(words):
    n = len(words)
    # Table size is the amount of size required to store the hash without collision.
    table_size = n *(n - 1) + 1
    c_min = 0
    perf_hash = False
    # Iterate till perfect hash has been found
    while(not perf_hash):
        # Initialize every time a new table with table size.
        table = [False] * table_size
        if(not perf_hash):
            perf_hash = True
            c_min += 1 
            # Iterate through all the words and find the minimum hash value.
            for word in words:
                # Hash Function index
                h = (math.floor(c_min // word2int(word)) % n)
                if(table[h]):
                    perf_hash = False
                    break # collision detected, try again with higher C value
                table[h] = True 
    return c_min

words = ['a', 'b']
min_C = get_min_C_value(words)
print(min_C)





def generate_points(n):
    points = []
    count = 0
    for i in range(n):
        a = random.uniform(-1, 1)
        b = random.uniform(-1, 1)
        points.append((a,b))
        if a*2 + b*2 < 1:
            count += 1
    return count

points = range(100, 10000, 100)
values = []
for point in points:
    count = generate_points(point)
    value = 4 * count / point
    values.append(value)

plt.plot(points, values)
plt.xlabel('n')
plt.ylabel('4*count/n')
plt.show()