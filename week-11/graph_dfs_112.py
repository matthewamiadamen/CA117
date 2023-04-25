#!/usr/bin/env python3

class Graph(object):

  def __init__(self, V):
    self.V = V
    self.adj = {}
    for v in range(V):
      self.adj[v] = []

  def addEdge(self, v, w):
    self.adj[v].append(w)
    self.adj[w].append(v)

  def degree(self, v):
    return len(self.adj[v])

  def maxDegree(self):
    return max([self.degree(v) for v in range(self.V)])

  def avgDegree(self):
    return sum([self.degree(v) for v in range(self.V)]) / self.V

class DFSPaths(object):
  def __init__(self, g, s):
    self.g = g
    self.s = s
    self.visited = [False for _ in range(g.V)]
    self.parent = [False for _ in range(g.V)]
    self.dfs(s)

  def dfs(self, v):
    #we are at node v
    #if we are at node v then we have visited it
    self.visited[v] = True
    #where can we go from node v
    #for each node w that is alr connected directly to v
    for w in self.g.adj[v]:
      #have we been to w before?
      #if not then go there
      if not self.visited[w]:
        #now lets record how we got there
        #when can backtrack through parent to find path
        self.parent[w] = v
        #lets go to w and continue
        self.dfs(w)

  #Return true if there is a path from s to v
  def hasPathTo(self, v):
    return self.visited[v]

  #Return path form s to v(or None should one not exist)
  def pathTo(self, v):
    if not self.hasPathTo(v):
      return []
    path = [v]
    while v != self.s:
      v = self.parent[v]
      path.append(v)
    return path[::-1]
