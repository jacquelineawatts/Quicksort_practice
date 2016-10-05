from random import choice

# --------------------------------- DEFINING FUNCTIONS -------------------------

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


def select_random_pivot(given_array):
    """Define the pivot element using random module."""

    pivot = choice(given_array)
    pivot_index = given_array.index(pivot)
    return pivot, pivot_index


def swap(item1, item2):
    """Swaps the placement of two elements in a list. """

    x = item1
    item1 = item2
    item2 = x 
    return item1, item2


def run_recursion(count, given_array, a, b = None):
    """Execute a single recursion loop around the randomly selected pivot element. """

    if len(given_array[a:b]) > 2:
        # Grabs a random pivot and its index
        pivot, pivot_index = select_random_pivot(given_array[a:b])
        print "\nThis is recursion #{}:".format(count)
        print "The pivot element is {}.".format(pivot)
        
        # Swaps the selected pivot with the 0th element in the array
        given_array[a], given_array[pivot_index] = swap(given_array[a], pivot)

        # Initiates i and j to the first non-pivot element
        i = 1
        j = 1
        
        # Loops through all non-pivot elements in array to compare > or < pivot element
        for int in given_array[a+1:b]:
            if  int < pivot:
                given_array[i], given_array[j] = swap(given_array[i], int)
                i += 1
            j += 1

        # When elements sorted around pivot, swaps pivot to absolute place
        given_array[a], given_array[pivot-1] = swap(given_array[a], given_array[pivot-1])

        # Replaces int_array elements will corresponding given_array elements
        int_array[a:pivot-1] = given_array[a:pivot-1]
        int_array[pivot-1] = pivot
        int_array[pivot:b] = given_array[pivot:b]

        # FOR TROUBLESHOOTING: Prints the breakdown of one recursive loop
        print "\nBreakdown after recursion #{}:".format(count)
        print int_array[a:pivot-1]
        print ""
        print int_array[pivot-1]
        print ""
        print int_array[pivot:b]
        count += 1
        
        # Calls a new recursion on the two new slices of array divided by our pivot
        run_recursion(count, given_array, a, pivot-1)
#         run_recursion(count, given_array[pivot:b], pivot, b)
    
    else:
        # Checks for base case of two items and runs basic swap if needed
        if (len(given_array) == 2) and (given_array[0] > given_array[1]):
             given_array[0], given_array[1] = swap(given_array[0], given_array[1])

    return int_array

# --------------------------------- EXECUTABLE CODE --------------------------

int_array = read_file_to_be_sorted('QuickSort_mini.txt')

count = 1
int_array = run_recursion(count, int_array, 0)
print int_array

