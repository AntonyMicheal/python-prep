#logic 

list = [1,2,3,4,5,6,7,8,9,0]
temp = list[0]
list[0] = list[len(list)-1]
list[len(list)-1] = temp

print(list)

# logic using function

def swap_elements(list):
    temp = list[0]
    list[0] = list[len(list)-1]
    list[len(list)-1] = temp

    return list

print(swap_elements([1,2,3,4,5,6,7,8,9,0]))


#improvised logic 

# swap elements in any known positions

def swap_elements(list, pos_1, pos_2):

    temp = list[pos_1]
    list[pos_1] = list[pos_2]
    list[pos_2] = temp

    return list

print(swap_elements([1,2,3,4,5,6,7,8,9,0], 1, 6))