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



def main():
    values = []
    vertex_input = int(input())
    adjlist = []
    vertexlist =  list(range(vertex_input))
    while vertex_input != 0:
        how_many = vertex_input
        while how_many > 0:
            adjval = [int(x) for x in input().split()]
            print(adjval)
            how_many -= 1
            adjlist.append(adjval)
            print(vertexlist, adjlist)
        values.append(bfs(vertexlist, adjlist))
        vertex_input = int(input())
        adjlist = []
        vertexlist =  list(range(vertex_input))
    for val in values:
        print(val)
    

def bfs(vertexlist, edgelist):
    q = Queue()
    colour = list(range(len(vertexlist)))
    pred = list(range(len(vertexlist)))
    d = list(range(len(vertexlist)))
    shortest_cycle = 0
    
    for u in vertexlist:
        colour[u] = "WHITE"
        pred[u] = "NULL"

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
                                shortest_cycle = d[adjacent] + 1                        
                        q.enqueue(adjacent)
                q.dequeue()
                colour[u] = "BLACK"

                
    return colour, pred, d, shortest_cycle


    
main()
