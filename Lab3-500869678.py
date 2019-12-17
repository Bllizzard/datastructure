#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:47:41 2019

@author: weijoe
"""

import heapq

class MyHuffman():
    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs
        
        node_list = []
        for i in weights:
            a = Node()
            a.frequency = weights[i]
            a.name = i 
            node_list.append(a)
        while len(node_list) > 1:
            node_list.sort(reverse = True)
            node_1 = node_list.pop()
            node_2 = node_list.pop()
            new_node = Node()
            new_node.frequency = node_1.frequency + node_2.frequency
            new_node.lchild = node_1
            new_node.rchild = node_2
            node_list.append(new_node)
        return new_node 

        
        
        
    def encode(self, word):
        # Return the bitstring of word encoded by the rules of your huffman tree
        """Return bit string for encoding."""
        code = list()
        if self.data:
            self.update({self.data:word})
            return 
        code += '0'

        self.left.encode(word)
        word = word[:-1]
        code += '1'
        self.right.encode(word)
        return code

  
    def decode(self, bitstring):
        # Return the word encoded in bitstring, or None if the code is invalid
        """Decode ASCII bit string for simplicity."""
        bits = ''
        for i in bitstring:
            if i == '0':
                b = self.left
                if b.value:
                    bits += b.value
                    a = self
                else:
                    a = b 

            elif i == '1':
                b = a.right
                if b.value:
                    bits += b.value 
                    a = self
                else:
                    a = b 

            else:
                bits += '\n'
        return bits


# This node structure might be useful to you
class Node:
    def __init__(self,value,data,left=None,right=None):
        
        self.left = left
        self.right = right
        self.data = data
        self.value = value

    def __lt__(self, other):
        pass
    
    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass
    
    def __ge__(self, other):
        pass