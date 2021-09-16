import random

def gen_rand_dict(dict_size):
    dict_build = {}
    def gen_unique_list(list_size): #modified definition of the gen_rand_list function to prevent duplicate values
        list_build = []
        for i in range(list_size):
            while True:
                a = random.randint(0,100)
                try:
                    if list_build.index(a) >= 0:
                        print("Repeated key. Rerolling...")
                        continue
                except ValueError:
                    list_build.append(a)
                    break
        return list_build    
    keys = gen_unique_list(dict_size)
    for i in keys:
        dict_build[i] = random.randint(0,100)
    return dict_build

def data_output():
    output = open("output/dict.txt",'w')
    print("This will generate a dict using random single integer key-value pairs.")
    print("Please specify the length of the dict:")
    length = input()
    output.write(str(gen_rand_dict(int(length))))
    output.close()
    print("Dict saved to dict.txt in the output subfolder.")
    print("Press Enter to exit.")
    input()