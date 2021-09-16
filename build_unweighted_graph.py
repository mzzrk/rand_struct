'''building randomly generated graphs'''
import random

'''vertex and edge lists'''

def gen_rand_vertices_VaEL():
    v_list = []
    v_size = input("How many vertices?\n")
    for i in range(int(v_size)):
        while True:#generates unique values in the list
            a = random.randint(0,100)
            try:
                if v_list.index(a) >= 0:
                    continue
            except ValueError:
                v_list.append(a)
                break
    return v_list

def gen_rand_edges(vertex_list):
    number_of_vertices = len(vertex_list)
    max_number_of_edges = number_of_vertices * (number_of_vertices - 1) / 2 #formula for max possible number of edges
    number_of_edges = random.randint(0, max_number_of_edges)
    e_list = []
    for i in range(number_of_edges):
        while True: #pick two random numbers different from each other within index of vertices
            a = random.randint(0, number_of_vertices - 1)
            b = random.randint(0, number_of_vertices - 1)
            while a == b:
                b = random.randint(0, number_of_vertices - 1)
            try:
                if e_list.index([vertex_list[a],vertex_list[b]]) >= 0:
                    continue
                elif e_list.index([vertex_list[b],vertex_list[a]]) >= 0:
                    continue
            except:
                e_list.append([vertex_list[a],vertex_list[b]])
                break
    return e_list

'''adjacency list'''

def gen_rand_vertices_AJ():
    v_list = []
    v_size = input("How many vertices?\n")
    for i in range(int(v_size)):
        while True:#generates unique values in the list
            a = random.randint(0,100)
            try:
                if v_list.index(a) >= 0:
                    continue
            except ValueError:
                v_list.append(a)
                break
    return v_list

def gen_rand_adj_dict(vertices):
    adj_list = {}
    for i in vertices:
        adj_list[i] = []
    for i in vertices:
        degree = random.randint(0,len(vertices))
        while degree > 0: #select other nodes to form edges with
            neighbors = adj_list[i]                     
            pair = vertices[random.randint(0,len(vertices) - 1)]
            if pair == i: #prevent forming edges with self
                degree = degree - 1
                continue
            else: 
                try:
                    if neighbors.index(pair) >= 0: #prevent forming duplicate edges
                        degree = degree - 1
                except:               
                    update_i = adj_list[i] + [pair]
                    adj_list.update({i:update_i})
                    update_pair = adj_list[pair] + [i]
                    adj_list.update({pair:update_pair})
                    degree = degree - 1
    return adj_list

'''write data to txt file'''

def data_output():
    output = open("output/graph.txt",'w')
    print("This will generate a random graph in the specified representation.")
    print("Specify graph representation type:")
    print("1) Value/Edge list")
    print("2) Adjacency list")
    graph_type = input()
    while True:
        if graph_type == "1":
            V = gen_rand_vertices_VaEL()
            E = gen_rand_edges(V)
            output.write("Value list on top, Edge list is on bottom:\n")
            output.write(str(V) + "\n")
            output.write(str(E))
            break
        elif graph_type == "2":
            V = gen_rand_vertices_AJ()
            E = gen_rand_adj_dict(V)
            output.write("Adjacency list:\n")
            output.write(str(E))
            break
        else:
            print("Invalid input. Please type either 1 or 2 to indicate your desired graph representation format.")
            continue
    output.close()
    print("Graph saved to graph.txt in the output subfolder.")
    print("Press Enter to exit.")
    input()