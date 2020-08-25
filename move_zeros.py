'''
    Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

    move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]

'''


def move_zeros(array):
    zeros_num = sum(x == 0.0 and not isinstance(x, bool) for x in array)
    new_array = [x for x in array if x != 0.0 or isinstance(x, bool)]
    new_array.extend([0]*zeros_num)
    return new_array