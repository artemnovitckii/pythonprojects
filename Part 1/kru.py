#class of priority queue goes here

def main():
    pass_list = []
    vertex_input = int(input())
    matrix =[]
    row = vertex_input
    column = vertex_input
    while vertex_input != 0:
        if vertex_input > 0:
            matrix = [[int(x) for x in input().split()] for y in range(row)]
            print(matrix)
        vertex_input = int(input())
        matrix = []
        row = vertex_input
        column = vertex_input
main()
