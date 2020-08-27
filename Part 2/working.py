
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
    values = []
    while num_vertices != 0:
        if num_vertices > 0:
            tree_list = [int(x) for x in input().split()]
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
            
            
            values.append(global_best)
        
        num_vertices = int(input())
        tree_list = []
        nodes = []
        leafs =[]
        local_sum = []
        global_best = 0
    for val in values:
        print(val)
                
            
main()
