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



# updated swaping last and first element 

def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList

print(swapList([1, 2,3,4,5,6,7,8,9,0]))

# updated swapping any known two elements

def swap_two(list, pos_1, pos_2):
    list[pos_1], list [pos_2] = list[pos_2], list[pos_1]
    return list

print(swap_two([1,2,3,4,5,6,7,8,9,0], 3, 7))

def swap_three(list, pos_1, pos_2, pos_3):
    list[pos_1], list[pos_2], list[pos_3] = list[pos_3], list[pos_2], list[pos_1]
    return list

print(swap_three([1,2,3,4,5,6,7,8,9], 2,5,8))

