print("This program generates a structure of your choosing filled with random integers.")
print("Choose a structure to generate:")
print("1) List")
print("2) Dictionary")
print("3) Unweighted graph")

def generate():
    struct = input()
    while True:
        if struct == "1":
            import build_list
            return build_list.data_output()
        elif struct == "2":
            import build_single_value_pair_dict
            return build_single_value_pair_dict.data_output()
        elif struct == "3":
            import build_unweighted_graph
            return build_unweighted_graph.data_output()
        else:
            print("Invalid input. Please type 1, 2, or 3 for your desired structure.")
            continue

generate()