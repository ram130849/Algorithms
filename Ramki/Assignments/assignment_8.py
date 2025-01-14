# -*- coding: utf-8 -*-

class MaxHeap:
  def __init__(self, ls=None):
      if(ls is None):
          self.heap = []
      else:
          self.heap = ls
          self.buildHeap()

  def buildHeap(self):
      for i in reversed(range(len(self.heap)//2)):
            self.heapify(i)

  def heapify(self, index):
      large_idx = index
      l_child = 2*index + 1
      r_child = 2*index + 2
      if(l_child < len(self.heap) and self.heap[l_child] > self.heap[large_idx]):
            large_idx = l_child
      if(r_child < len(self.heap) and self.heap[r_child] > self.heap[large_idx]):
            large_idx = r_child
      if(large_idx != index):
            self.heap[index], self.heap[large_idx] = self.heap[large_idx], self.heap[index]
            self.heapify(large_idx)
    
  def insert(self, element):
      self.heap.append(element)
      i = len(self.heap) - 1
      parent = (i-1) // 2
      while(i > 0 and self.heap[parent] < self.heap[i]):
          self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
          i = parent
          parent = (i-1) // 2

  def getMax(self):
      if(len(self.heap) == 0):
            return None
      max_elem = self.heap[0]
      self.heap[0] = self.heap[-1]
      self.heap.pop()
      self.heapify(0)
      return max_elem

  def print(self):
      return self.heap

def test_max_heap(input):
    mx = None
    result = []
    i = 0
    while i < len(input):
      if input[i] == 'MaxHeap':
        mx = MaxHeap(input[i+1])
        result.append(None)
        i += 2
      elif input[i] == 'insert':
        result.append(mx.insert(input[i+1]))
        i += 2
      elif input[i] == 'getMax':
        result.append(mx.getMax())
        i += 1
      elif input[i] == 'print':
        res = mx.print()
        result.append(res[:])
        i += 1
      else:
        i += 1
    return result

# input = ['MaxHeap', [2, 3, 4], 'print', 'insert', 1, 'insert', 5, 'insert', 6, 'insert', 7, 'getMax', 'insert', 8, 'print']
# print(test_max_heap(input)) # [None, [4, 3, 2], None, None, None, None, 7, None, [8, 4, 6, 1, 3, 2, 5]]

from collections import OrderedDict
import heapq as hq
class node:
    def __init__(self, count, symbol, lchild=None, rchild=None):
        self.symbol = symbol
        self.count = count
        self.lchild = lchild
        self.rchild = rchild
        self.code = ''
        
class HuffmanCoding:
      def __init__(self):
          self.huffman_tree = OrderedDict()
          self.root = node(count=0,symbol='')

      # Implement this function for Q2
      def encode(self, s):
        # Return the encoded message and codes used
        if(len(s)==0):
            return
        if(len(s)==1):
            encoded = '0'
            return node(symbol=s[0],frequency=1)
        frequency = [(s.count(i),i) for i in set(s)]
        codewords = {}

        # Maintain all nodes - used to create huffman tree
        self.huffman_tree = OrderedDict()
        for element in frequency:
            self.huffman_tree[element[1]] = node(symbol = element[1], count = element[0])

        hq.heapify(frequency)

        while(len(frequency)>1):
            min1 = hq.heappop(frequency)
            min2 = hq.heappop(frequency)
            new_symbol = min1[1] + min2[1] 
            new_count = min1[0] + min2[0]

            # Creating the Huffman Tree.
            min1_node = self.huffman_tree[min1[1]]
            min2_node = self.huffman_tree[min2[1]]
            min1_node.edge = 0
            min2_node.edge = 1
            parent_node = node(symbol = new_symbol, count = new_count, lchild = min1_node, rchild = min2_node)
            self.huffman_tree.pop(min1[1])
            self.huffman_tree.pop(min2[1])
            self.huffman_tree[new_symbol] = parent_node
            for cw in min1[1]:
                if(not codewords.get(cw)):
                    codewords[cw] = '0'
                else:
                    codewords[cw] = '0' + codewords[cw]

            for cw in min2[1]:
                if(not codewords.get(cw)):
                    codewords[cw] = '1'
                else:
                    codewords[cw] = '1' + codewords[cw]

            hq.heappush(frequency, (new_count, new_symbol))
        
        encoded = ''
        for i in s:
            encoded+=codewords[i]
        
        self.root = self.huffman_tree[new_symbol]
        return encoded,codewords
      
      # Implement this function for Q3
      def decode(self, s, d):
        # Return the decoded message
        decoded = ''
        d = {v:k for k,v in d.items()}
        code = s[0]
        for bit in s[1:]:    
            if(code in list(d.keys())):
                decoded += d[code]
                code = bit
            else:
                code+= bit
        if(code in list(d.keys())):
            decoded+=d[code]
        return decoded

# hc = HuffmanCoding()
# input = 'aabc'
# print(hc.encode(input))

# input = 'football'
# print(hc.encode(input))
# print('Encoding outputs', hc.encode(input))
# print('Decoding outputs hii', hc.decode(*hc.encode(input)))
# print('Is matching with string = ', input == hc.decode(*hc.encode(input)))

# hc = HuffmanCoding()
# print(hc.decode('001011', {'a': '0', 'b': '10', 'c': '11'})) 
# print(hc.decode('0011110110', {'a': '00', 'l': '01', 'e': '10', 'p': '11'}))



















































