"""
1129. Shortest Path with Alternating Colors
Difficulty: Medium
Link: https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
"""

class Solution(object):
    def buildDict(self, edges):
        d = {}
        for elem in edges:
            sender = elem[0]
            receiver = elem[1]
            if receiver in d:
                lst = d[receiver]
                lst.append(sender)
                d[receiver] = lst
            else:
                d[receiver] = [sender]
        return d

    def searchInBlue(self, nodes, counter):
        # there is a red edge to i
        # all the elements in nodes point to i
        if 0 in nodes:
            return counter
        
        while len(nodes) > 0: 
            node = min(nodes)
            if node not in self.blueDict:
                nodes.remove(node)
            else:
                new_nodes = self.blueDict[node]
                counter += 1
                r = searchInRed(self, new_nodes, counter)
                
                if r == -1
                    nodes.remove(node)

    
    def searchInRed(self, nodes, counter):
        pass

    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]] [[0,1],[1,2]]
        :type blueEdges: List[List[int]] []
        :rtype: List[int]
        """
        
        #redEdges = sorted(redEdges, key=lambda x: x[0])
        #blueEdges = sorted(blueEdges, key=lambda x: x[0])

        #redEdges = [[sender, receiver]]

        #key: receiver node
        #values: list of all starting nodes
        self.redDict = self.buildDict(redEdges)
        self.blueDict = self.buildDict(blueEdges)

        answer = [0]
        for i in range(1, n):
            if i not in self.redDict:
                if i not in self.blueDict:
                    answer[i] = -1
                    pass
            
            if i in self.redDict:
                # there is a red edge to i
                sender_nodes = self.redDict[i]
                r1 = searchInBlue(sender_nodes, 1)
            
            if i in self.blueDict:
                sender_nodes = self.blueDict[i]
                r2 = searchInBlue(sender_nodes, 1)

            answer[i] = min(r1, r2)
