from random import choice

def read_file_to_be_sorted(filename):
    """Load file and save as list to iterate over numbers."""
	
    quiz_file = open(filename)
    array_all = quiz_file.read().splitlines()
    quiz_file.close()
    
    # convert str list to int
    int_array = []
    for x in array_all:
        y = int(x)
        int_array.append(y)
    return int_array


def select_random_pivot(int_array):
    """Define the pivot element using random module."""
    return choice(int_array)

def swap(item1, item2):
    """Swaps the placement of two elements in a list. """

    x = item1
    item1 = item2
    item2 = x 
    return item1, item2


def recursion_loop(int_array):
    """Execute a single recursion loop around the randomly selected pivot element. """
    
    pivot = select_random_pivot(int_array)
    pivot_index = int_array.index(pivot)
    print "" 
    print "The pivot element is {}.".format(pivot)
    print ""
    int_array[0], int_array[pivot_index] = swap(int_array[0], pivot)

    i = 1
    j = 1
	
    if len(int_array) >= 2:         
        for int in int_array[1::]:
            if  int < pivot:
                int_array[i], int_array[j] = swap(int_array[i], int)
                i += 1
            j += 1

        int_array = swap_pivot(int_array, i, pivot)
        return int_array

#         recursion_loop(int_array[0:(i-2)])
#         recursion_loop(int_array[i::])
#     
#     else:
#         return int_array

def swap_pivot(int_array, i, pivot):
    """Swap pivot element with (i-1)th element to put pivot in its absolute place. """
    
    int_array[0] = int_array[i-1]
    int_array[i-1] = pivot
    return int_array 

# --------------------------------- CALLING FUNCTIONS --------------------------

int_array = read_file_to_be_sorted('QuickSort.txt')    
int_array = recursion_loop(int_array)
print int_array


# while len(int_array) > 1:
# 	recursion_loop(int_array)

