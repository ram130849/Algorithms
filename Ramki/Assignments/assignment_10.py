
class UnionFind:
    def __init__(self,n):
        self.parent = []
        self.count = n
        self.UnionFind(self.count)

    def UnionFind(self,n):
        self.parent = [0]*(n+1)
        for i in range(n):
            self.parent[i] = i
        
    def find(self,x):
        par_x = x
        while(self.parent[par_x]!=par_x):
            par_x = self.parent[par_x]
        while(x !=par_x):
            fx = self.parent[x]
            self.parent[x] = par_x
            x = fx
        return par_x

    def get_count(self):
        return self.count
    def Union(self,a:int,b:int):
        par_a = self.find(a)
        par_b = self.find(b)
        if(par_a!=par_b):
          self.parent[par_a] = par_b
          self.count-=1

def removeStones(stones: list[list[int]]):
    no_stones = len(stones)
    union_find = UnionFind(no_stones)
    for i in range(no_stones):
      for j in range(i+1,no_stones):
          if(stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]):
              union_find.Union(i,j)

    return no_stones - union_find.get_count()

from collections import defaultdict
def find(parent, i):
    if parent[i] != -1:
      return find(parent, parent[i])
    else:
      return i

def union(parent, a, b,count):
    rootA = find(parent,a)
    rootB = find(parent,b)
    if rootA != rootB:
      parent[rootA] = rootB
      count -= 1
    return count

def no_of_islands(map_grid):
    # Return the number of islands
    if(len(map_grid) == 0 or len(map_grid[0]) == 0):
        return 0
    if(len(map_grid)==1 and len(map_grid[0])==1):
        if(map_grid[0][0]=='1'):
            return 1
        else:
            return 0
    count = 0
    no_rows = len(map_grid)
    no_cols = len(map_grid[0])
    adj_cells = [(1,0),(0,1),(-1,0),(0,-1)]
    parent = defaultdict()
	  
    for i in range(no_rows):
        for j in range(no_cols):
            if(map_grid[i][j] == "1"):
                parent[i*no_cols+j] = -1
                count+=1

    for i in range(no_rows):
        for j in range(no_cols):
            if map_grid[i][j] == "1":
                r,c = i,j
                for (dr,dc) in adj_cells:
                    adj_r, adj_c = r + dr, c + dc
                    if(0<=adj_r<no_rows and 0<=adj_c<no_cols and map_grid[adj_r][adj_c] == "1"):
                        count = union(parent, r*no_cols+c, adj_r*no_cols+adj_c,count)
    return count


from math import inf
from collections import defaultdict
import heapq
def cheapest_flight(n, tickets, start):    
    # return get_shortest_path(tickets,start,n)
     # Initialize the distances to all airports to infinity
    dist = [float('inf')] * n
    # Set the distance to the start airport to 0
    dist[start] = 0
    
    # Use a priority queue to keep track of the vertices to visit
    heap = [(0, start)] # (distance, vertex)
    
    while heap:
        # Get the vertex with the smallest distance
        d, u = heapq.heappop(heap)
        
        # Skip this vertex if we've already found a shorter path to it
        if d > dist[u]:
            continue
        
        # Iterate over all neighbors of u
        for v in range(n):
            # Skip this neighbor if there's no flight from u to v
            if tickets[u][v] == 0:
                continue
            # Compute the distance to this neighbor
            alt = dist[u] + tickets[u][v]
            # Update the distance if it's smaller than the current value
            if alt < dist[v]:
                dist[v] = alt
                # Add the neighbor to the priority queue
                heapq.heappush(heap, (alt, v))
    
    return dist

def get_shortest_path(weight_mat, start, end):             
    n = len(weight_mat) # get the number of nodes
    distances = [inf]*n # Set all initial distances to every node as infinity
    distances[start] = weight_mat[start][start]  # set the start node as 0
    visited_nodes = [False]*n
    for k in range(n-1):
        dist_at_min = inf
        u = start
        for v in range(start, len(visited_nodes)): 
            if visited_nodes[v] == False and distances[v] <= dist_at_min:
                dist_at_min = distances[v]
                u = v
        visited_nodes[u] = True
        
        for v in range(n): # check if 
            if not(visited_nodes[v]) and weight_mat[u][v] != 0 and distances[u] + weight_mat[u][v] < distances[v]:
                distances[v] = distances[u] + weight_mat[u][v]

    return distances


from collections import deque

def number_of_moves(start_config, end_config, forbidden_config):
    # Create the graph
    graph = defaultdict(None)
    for config in forbidden_config:
        graph[config] = []
    for i in range(10000):
        config = str(i).zfill(4)
        if config not in forbidden_config:
            neighbors = []
            for i in range(4):
                for d in (-1, 1):
                  new_digit = (int(config[i]) + d) % 10
                  new_config = config[:i] + str(new_digit) + config[i+1:]
                  if new_config not in forbidden_config:
                      neighbors.append(new_config)
            graph[config] = neighbors
    
    # Perform BFS search
    queue = deque([(start_config, 0)])
    visited = set([start_config])
    while queue:
        config, min_moves = queue.popleft()
        if config == end_config:
            return min_moves
        for neighbor in graph[config]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, min_moves + 1))
    
    return -1 # No path found


from collections import deque
def word_games(word1, word2, dictionary):
    queue = deque([(word1, 0)]) # initial word and number of operations
    visited = set([word1])
    all_words = "abcdefghijklmnopqrstuvwxyz"
    min_moves = 0
    while queue:
        word, min_moves = queue.popleft()
        if word == word2:
            return min_moves
        for i in range(len(word)):
            for c in all_words:
                new_word = word[:i] + c + word[i+1:]
                if new_word in dictionary and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, min_moves + 1))
    
    return -1





















