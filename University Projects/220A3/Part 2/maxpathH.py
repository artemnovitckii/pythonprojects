'''
Author: Artem Novitckii
ID: 207428057
Input method was taken from lecturer Dr Michael J. Dinneen
'''

class Node:

    def __init__(self,data):
        self.ID = data
        self.parent = None
        self.cost_to_parent = 0
        self.children = 0
        self.cost = [0,0]
        self.used = False

    def add_cost_to_parent(self,costTo):
        self.cost_to_parent = costTo

    def add_parent(self,parent):
        self.parent = parent

    def children_count(self):
        self.children += 1

    def add_cost(self,value): #NEED FIXING!
        self.cost.append(value)
        self.cost.sort(reverse=True)
        self.cost.pop()

        

def main():
    nodes = []
    leafs =[]
    local_sum = []
    global_best = 0
    values = []
    while True:
        num_vertices = int(input())
        if num_vertices == 0:
            break
        tree_list = []
        while len(tree_list) < 2*(num_vertices-1):
            tree_list += [int(x) for x in input().split()]

        count = 0
        for i in range(num_vertices): 
            node = Node(i)
            nodes.append(node)
            if i != 0:
                if tree_list != []:
                    node.add_parent(tree_list[count]) 
                    count += 1
                    node.add_cost_to_parent(tree_list[count]) 
                    count += 1
                if nodes[i].parent == nodes[nodes[i].parent].ID:
                    nodes[nodes[i].parent].children_count()

        for i in range(num_vertices):
            if nodes[i].children == 0:
                leafs.append(i)
                
        update_leafs = []
        
        while nodes[0].children != 0:
            for i in leafs:
                if i != 0:
                    if nodes[i].children == 0 and nodes[i].used == False:
                        
                        cost_to_parent = nodes[i].cost_to_parent
                        parent = nodes[i].parent
                        nodes[parent].add_cost(cost_to_parent + nodes[i].cost[0])
                        nodes[i].used = True
                        if nodes[i].cost_to_parent > global_best:
                            global_best = nodes[i].cost_to_parent
                        if nodes[i].cost[0] > global_best:
                            global_best = nodes[i].cost[0]
                        if nodes[i].cost[0]+nodes[i].cost[1] > global_best:
                            global_best = nodes[i].cost[0]+nodes[i].cost[1]
                        nodes[parent].children = nodes[parent].children - 1
                        if nodes[parent].children == 0:
                            update_leafs.append(nodes[parent].ID)
                        
                    local_sum = []
            leafs = update_leafs
                    

        if nodes[0].children == 0:
            if nodes[0].cost[0] + nodes[0].cost[1] > global_best:
                global_best = nodes[0].cost[0] + nodes[0].cost[1]
                
        print(global_best)

        nodes = []
        leafs =[]
        global_best = 0
          
main()
