import operator
'''
Author: Artem Novtickii
Reference for the Disjoint set class was taken from open source licensed by MIT website:
https://www.nayuki.io/page/disjoint-set-data-structure
'''

class DisjointSet(object):
    
    # Constructs a new set containing the given number of singleton sets.
    # For example, DisjointSet(3) --> {{0}, {1}, {2}}.
    def __init__(self, num_of_vertices):
            self.num_sets = num_of_vertices
            self.parents = list(range(num_of_vertices))
            self.ranks = [0] * num_of_vertices
            self.sizes = [1] * num_of_vertices
            #print(self.parents)

    def find(self, elemindex): #find
            # Follow parent pointers until we reach a representative
            parent = self.parents[elemindex]
            if parent == elemindex:
                    return elemindex
            while True:
                    grandparent = self.parents[parent]
                    if grandparent == parent:
                            return parent
                    self.parents[elemindex] = grandparent  # Partial path compression
                    elemindex = parent
                    parent = grandparent

    # Tests whether the given two elements are members of the same set. Note that the arguments are orderless.
    def are_in_same_set(self, elemindex0, elemindex1):
            return self.find(elemindex0) == self.find(elemindex1)

    def union(self, elemindex0, elemindex1):
            # Get representatives
            repr0 = self.find(elemindex0)
            repr1 = self.find(elemindex1)
            if repr0 == repr1:
                    return False #Not Merged
            
            # Compare ranks
            cmp = self.ranks[repr0] - self.ranks[repr1]
            if cmp == 0:  # Increment repr0's rank if both nodes have same rank
                    self.ranks[repr0] += 1
            elif cmp < 0:  # Swap to ensure that repr0's rank >= repr1's rank
                    repr0, repr1 = repr1, repr0
            
            # Graft repr1's subtree onto node repr0
            self.parents[repr1] = repr0
            self.sizes[repr0] += self.sizes[repr1]
            self.sizes[repr1] = 0
            self.num_sets -= 1
            return True #Merged

def krustal(num_of_vertices,edge_cost_list):
    sets = DisjointSet(num_of_vertices)
    sorted_edges = sorted(edge_cost_list, key=operator.itemgetter(2))
    #print("Sorted",sorted_edges)
    total_weight = 0
    for i in range(len(sorted_edges)):
        start,final,weight = sorted_edges[i]
        if sets.find(start) != sets.find(final):
            sets.union(start,final)
            total_weight += weight

    return total_weight
            

def main():
    values_list = []
    vertex_input = int(input())
    matrix =[]
    row = vertex_input
    column = vertex_input
    edge_cost_list = []
    while vertex_input != 0:
        if vertex_input > 0:
            matrix = [[int(x) for x in input().split()] for y in range(row)]
            #print(matrix)
            for y in range(len(matrix)):
                #print("This is y is the row",y)
                starting_vertex = y #row
                for x in range(len(matrix[y])):
                    #print("This is x is a column",x)
                    if matrix[y][x] != 0:
                        #print("This is matrix[y][x]",matrix[y][x])
                        #target_vertex = matrix[y].index(matrix[y][x])
                        target_vertex = x
                        cost = matrix[y][x]
                        #if starting_vertex > target_vertex:
                        edge_cost_list.append([starting_vertex,target_vertex,cost])
                        #print("starting final cost",edge_cost_list,"\n")
    
            values_list.append(krustal(vertex_input,edge_cost_list))
    
        vertex_input = int(input())
        matrix = []
        edge_cost_list = []
        row = vertex_input
        column = vertex_input
    #print(values_list)
    for val in values_list:
        print(val)
main()
#matrix looks like this = [[0, 1, 3], [1, 0, 2], [3, 2, 0]]
#edge_cost_list looks like this = [[0, 1, 1], [0, 2, 3], [1, 0, 1], [1, 2, 2], [2, 0, 3], [2, 1, 2]]

    
