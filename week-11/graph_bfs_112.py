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

class BFSPaths(object):
  def __init__(self, g, s):
    self.g = g
    self.s = s
    #Once queued we mark the vertex so we dont queue it again
    #prevents us going in circles
    self.marked = [False for i in range(g.V)]
    #We store each vertex that we came from
    #Every node has a parent except s
    self.parent = [False for i in range(g.V)]
    #explore
    self.bfs(s)

  def bfs(self, s):
    #start from s
    #its a place we want to go
    #queue it so it adds to end
    queue = [s]
    #mark s since we are there now and we dont go again
    self.marked[s] = True

    #Not recursive we just have the queue
    #for aslong is queue not empty
    while queue:
      #remove vertex at the front of the queue
      v = queue.pop(0)
      #look at where we can go from v
      for w in self.g.adj[v]:
        #if not previously marked
        #either we've been there or we know its in queue
        #Well get there eventually
        if not self.marked[w]:
          #add it to queue for future
          queue.append(w)
          #Remember where we came from
          self.parent[w] = v
          #Dont queue again
          #No longer false now its w
          self.marked[w] = True

#Return True if there is a path from s to v
#Was v ever marked in the process
  def hasPathTo(self, v):
    return self.marked[v]

  def pathTo(self, v):
    #verify a path actually exists
    if not self.hasPathTo(v):
      return None
    path = [v]
    #while you havent reached our destination s
    while v != self.s:
      #look up parent of v
      v = self.parent[v]
      #append to path
      path.append(v)
      #path is backwards
    return path[::-1]
