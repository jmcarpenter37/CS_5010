# Author: John Carpenter
# ID: jmc7dt
# Course: CS 5010
# Screen capture(JPEG) or copy & paste three runs of your programs.

# Output:
# The index of the element in the list
# If the element is not in the list, the function should return a sentinel value
# If the element is in the list multiple times, return the first position

# Sequential search allows us to brute force our way through the array
# that we provide to the functions and find the target we are looking for.
def seq_search(array , target):
    pos = 0 # using pos object as a counter
    found = False # the default is set to false becuase we haven't found anything yet
    while pos < len(array): # begin to move through the array
        if array[pos] == target:
            return "Your target was: {}".format( array[pos]) , "The position of the target is: {}".format( pos)
        pos += 1 # We still need to check if the target exists elsewhere in the array
    return found , "Your target was not found in the array provided."

# Testing
list1 = [1,2,3,4,5,6,32,89,4,5]
ret = seq_search(list1 , 3)
print(ret)

# Find 4 since it exists twice
list1 = [1,2,3,4,5,6,32,89,4,5]
ret = seq_search(list1 , 4) # This algorithm will always return minimum index for a value if the target appears more than twice in the array
print(ret)

# Find 89
list1 = [1,2,3,4,5,6,32,89,4,5]
ret = seq_search(list1 , 89)
print(ret)

# Find 9000
list1 = [1,2,3,4,5,6,32,89,4,5]
ret = seq_search(list1 , 9000)
print(ret)


