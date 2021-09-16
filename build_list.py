import random

def gen_rand_list(list_size):
    list_build = []
    for i in range(list_size):
        list_build.append(random.randint(0,100))
    return list_build

def data_output():
    output = open("output/list.txt",'w')
    print("This will generate a list of random integers from 0 to 100 of a specified length.")
    print("Please specify the length of the list:")
    length = input()
    output.write(str(gen_rand_list(int(length))))
    output.close()
    print("List saved to list.txt in the output subfolder.")
    print("Press Enter to exit.")
    input()