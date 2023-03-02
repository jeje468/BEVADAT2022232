# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list, start_index, end_index):
    return input_list[start_index:end_index + 1]

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list, step_size):
    return input_list[::step_size]

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    input_set = set(input_list)

    return len(input_set) == len(input_list)

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    result = []
    for l in input_list:
        if isinstance(l, list):
            result.extend(flatten(l))
        else:
            result.append(l)
    
    return result

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args

# %%
def merge_lists(*args):
    result = []

    for arg in args:
        result.extend(arg)
    
    return result

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    result = []

    for tup in input_list:
        result.append(tup[::-1])

    return result

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_duplicates(input_list):
    return list(set(input_list))

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    result = []

    for j in range(0, len(input_list[0])):
        column = []
        for i in range(0, len(input_list)):
            column.append(input_list[i][j])
        result.append(column)
    
    return result


# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list, chunk_size):
    result = []

    for item in input_list:
        chunks = divide_chunks(item, chunk_size)
        result.extend(chunks)
    
    return result

def divide_chunks(l, n):
    result = []
    for i in range(0, len(l), n):
        result.append(l[i:i + n])

    return result

list = [[0, 3, 6, 9], [1, 4, 7, 10], [2, 5, 8, 11]]
print(split_into_chunks(list, 3))

    

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict):
    result = {}

    for d in dict:
        result.update(d)
    
    return result

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    result = {"even" : [], "odd" : []}

    for num in input_list:
        if num % 2 == 0:
            result["even"].append(num)
        else:
            result["odd"].append(num)
    
    return result

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    result = input_dict.copy()

    for key, value in input_dict.items():
        result[key] = sum(value) / len(value)
    
    return result

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


