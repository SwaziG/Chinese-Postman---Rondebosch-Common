# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:08:27 2023

@author: SwaziG
"""

import numpy as np
import pylab 
import pandas as pd
import re
import random 


def Outer_nodes(filename):
    '''
    Opens file holding a list of the outer nodes (ie. starting and ending point)
    
    return list of outer nodes
    '''
    f = open(filename, 'r')
    
    for line in f:
        node_list = line.strip().split(',')

    return node_list

def Adjacency_list(filename):
    '''
    Returns a dictionary key = intersection nodes and values = list of adjacent nodes
    '''
    Adj_dict = {}
    df = pd.read_excel(filename)
    header = df.columns.tolist()
    
    for _, row in df.iterrows():
        intersection = row['Intersection']
        adj_list = [row['C1'], row['C2'], row['C3'], row['C4'], row['C5'], row['C6'], row['C7']]
        
        if intersection not in Adj_dict:
            Adj_dict[intersection] = adj_list
        
    return Adj_dict

class Position(object):
    def __init__(self, Adj_list, Start, Node):
        self.Adj_list = Adj_list
        self.Start = Start
        self.Node = Node

    def get_Start(self):
        """
        Returns the
        """
        return self.Start
    
    def get_Last_position(self):
        '''
        Takes the adjacency list excel file  
        '''
        return self.Node

    def get_New_position(self):
        """
        Using the last known node, the get_New_position picks the next node at random
        """
        if self.Node not in self.Adj_list:
            raise NotADirectoryError #This node is not in the Adjacency List
        choices = ['C1','C2','C3','C4','C5','C6','C7']
        choose = ""
        i = 7
        while i > 0: 
            choose = random.choice(choices)
            choices.remove(choose)
            if
            i -= 1




### Testing
## print(Outer_nodes('OuterNodes.txt'))
print(Adjacency_list('Intersections & Connections.xlsx'))