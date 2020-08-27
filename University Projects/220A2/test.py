'''
to check the queue use this:
    dis = q.size()
    while dis > 0:
        print(q.dequeue())
        dis = dis -1

'''



class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def printQueue(self):
      return self.queue



def bfs(vertexlist, edgelist):
    q = Queue()
    colour = list(range(len(vertexlist)))
    pred = list(range(len(vertexlist)))
    d = list(range(len(vertexlist)))
    shortest_cycle = []
    
    for u in vertexlist:
        colour[u] = "WHITE"
        pred[u] = "NULL"
        

    for starting_index in range(len(vertexlist)):
        
        for s in vertexlist:
            if colour[s] == "WHITE":
                colour[s] = "GREY"
                d[s] = 0
                q.enqueue(s)
                while not q.isEmpty():
                    u = q.peek()
                    for v in edgelist[u]:
                        adjacent = v
                        if colour[adjacent] == "WHITE":
                            colour[adjacent] = "GREY"
                            pred[adjacent] = u
                            d[adjacent] = d[u] +  1
                            if d[adjacent] > 0:
                                if s in edgelist[adjacent]:
                                    shortest_cycle.append(d[adjacent] + 1)
                            q.enqueue(adjacent)
                    q.dequeue()
                    colour[u] = "BLACK"        
        print(colour, pred, d, shortest_cycle)
        q = Queue()
        colour = list(range(len(vertexlist)))
        pred = list(range(len(vertexlist)))
        d = list(range(len(vertexlist)))        



        
        
            
    




bfs([0,1,2,3],[[1,3],[2,3],[0],[]]))
#bfs([0,1,2],[[1,2],[],[1]]))
