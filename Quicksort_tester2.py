from random import choice
from sys import argv

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


def select_random_pivot(int_array, a, b):
    """Define the pivot element using random module."""

    pivot = choice(int_array[a:b])
    pivot_index = int_array.index(pivot)
    return pivot, pivot_index


def swap(item1, item2):
    """Swaps the placement of two elements in a list. """

    x = item1
    item1 = item2
    item2 = x
    return item1, item2


def print_breakdown(count, int_array, start_index, end_index, pivot):

    print "\nBreakdown after recursion #{}:".format(count)
    print int_array[start_index:pivot-1]
    print ""
    print int_array[pivot-1]
    print ""
    print int_array[pivot:end_index]


def handle_base_case(int_array, start_index, end_index):
    """Checks for base case of two items and runs basic swap if needed"""

    if end_index is not None:
        end_index = end_index + 1

    if (len(int_array[start_index:end_index]) == 2) and (int_array[start_index] > int_array[start_index +1]):
        int_array[start_index], int_array[start_index+1] = swap(int_array[start_index], int_array[start_index+1])


def run_quicksort(depth, int_array, start_index, end_index):
    """Execute a single recursion loop around the randomly selected pivot element. """

    depth += 1

    if end_index is not None:
        end_index += 1

    if len(int_array[start_index:end_index]) > 2:

        i, j = start_index + 1, start_index + 1
        # Grabs a random pivot and its index
        pivot, pivot_index = select_random_pivot(int_array, start_index, end_index)
        # pivot = int_array[start_index]
        print "This is a recursion of depth: {}".format(depth)
        print "The pivot element is {}.\n".format(pivot)

        # Swaps the selected pivot with the 0th element in the array
        int_array[start_index], int_array[pivot_index] = swap(int_array[start_index], pivot)

        # Loops through all non-pivot elements in array to compare > or < pivot element
        for x in int_array[start_index+1:end_index]:
            if x < pivot:
                int_array[i], int_array[j] = swap(int_array[i], x)
                i += 1
            j += 1

        # When elements sorted around pivot, swaps pivot to absolute place
        int_array[start_index], int_array[pivot-1] = swap(int_array[start_index], int_array[pivot-1])

        # UNCOMMENT FOR TROUBLESHOOTING: Prints the breakdown of one recursive loop
        # print_breakdown(count, int_array, start_index, end_index, pivot)

        run_quicksort(depth, int_array, start_index, pivot-1)
        run_quicksort(depth, int_array, pivot, end_index)

    else:
        handle_base_case(int_array, start_index, end_index)



# --------------------------------- EXECUTABLE CODE --------------------------

int_array = read_file_to_be_sorted(argv[1])

depth = 0
start_index = 0
end_index = None

run_quicksort(depth, int_array, start_index, end_index)

print int_array
