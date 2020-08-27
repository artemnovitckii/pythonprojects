'''
input format is
9
0 1 0 1 0 5 1 4 1 8 2 2 2 3 4 1
5
0 -1 1 3 0 2 1 2
5
0 1 1 -3 0 -2 1 -2
5
0 -1 1 -3 0 -2 1 -2
10
0 -1 0 -1 0 0 1 3 1 4 2 4 2 2 3 3 3 3
0
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

    def add_cost(self,value):
        self.cost.append(value)
        self.cost.sort(reverse=True)
        self.cost.pop()

    def change_cost(self):
        self.local_max
        
    

    

def main():
    num_vertices = int(input())
    tree_list = []
    nodes = []
    leafs =[]
    local_sum = []
    global_best = 0

    #Getting input from the user
    tree_list = [int(x) for x in input().split()]

    #Analysis of data
    for i in range(num_vertices):
        node = Node(i)
        nodes.append(node)
        if i != 0:
            if tree_list != []:
                node.add_parent(tree_list.pop(0))
                node.add_cost_to_parent(tree_list.pop(0))
    
    for i in range(1,num_vertices):
        parent = nodes[i].parent
        compare = nodes[parent].ID
        if parent == compare:
            nodes[parent].children_count()
            
    #All nodes and their information is saved in list called nodes

    #Step 2 analyze leafs to get their cost to parent
    while nodes[0].children != 0:
        for i in range(num_vertices):
            if nodes[i].children == 0 and nodes[i].used == False: #LEAF NODE
                cost_to_parent = nodes[i].cost_to_parent
                parent = nodes[i].parent
                nodes[parent].add_cost(cost_to_parent + nodes[i].cost[0])
                nodes[i].used = True
                local_sum.append(nodes[i].cost_to_parent)
                local_sum.append(nodes[i].cost[0])
                local_sum.append(nodes[i].cost[0]+nodes[i].cost[1])
                local_sum.sort(reverse=True)
                if local_sum[0] > global_best:
                    global_best = local_sum[0]
                nodes[parent].children = nodes[parent].children - 1
            local_sum = []

    if nodes[0].children == 0:
        zero_sum = nodes[0].cost[0] + nodes[0].cost[1]
        if zero_sum > global_best:
            global_best = zero_sum
    
    
    print(global_best)
        
    
main()
