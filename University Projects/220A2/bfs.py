
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




def bfs (vertexlist, arclist):
    empty_queue = Queue()
    colour_list = list(range(len(vertexlist)))
    pred_list = list(range(len(vertexlist)))
    depth = list(range(len(vertexlist)))

    for vertex_index in range(len(vertexlist)):
        colour_list[vertex_index] = "WHITE"
        pred_list[vertex_index] = "NULL"

    for vertex_index_2 in range(len(vertexlist)):
        if colour_list[vertex_index_2] == "WHITE":
            colour_list[vertex_index_2] = "GREY"
            depth[vertex_index_2] = 0
            empty_queue.enqueue(vertexlist[vertex_index_2])
            while not empty_queue.isEmpty():
                top_vertex = empty_queue.peek()
                for adjacent in arclist[top_vertex]:
                    location = vertexlist.index(adjacent)
                    if colour_list[location] == "WHITE":
                        colour_list[location] = "GREY"
                        pred_list[location] = vertexlist[top_vertex]
                        depth[location] = depth[top_vertex] + 1
                        empty_queue.enqueue(vertexlist[location])
                empty_queue.dequeue()
                colour_list[top_vertex] = "BLACK"

    return colour_list, pred_list, depth


print(bfs([0,1,2,3],[[1,3],[2,3],[0],[]]))
