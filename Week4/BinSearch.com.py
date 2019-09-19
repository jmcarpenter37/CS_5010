# Name: John Carpenter
# ID: jmc7dt
# Class: CS 5010

import math
target_num = 8
list_num = [0,1,2,3,9,5,8]
def BinarySearch(item_list  , target  ):
    sorted_list = sorted(item_list)
    first_num = 0 # 0 is the first index in the item_list
    final_num = len(item_list) - 1 # gets the index of the last item in item_list
    found_num = False # Start found number as False because we haven't found the number yet. Once we find it then it will turn to true
    while(first_num <= final_num and not found_num):
        mid_point_index = math.floor((first_num+final_num)/2) # Using the build in floor function
        if sorted_list[mid_point_index] == target: # Now that the list is sorted we check to see if the middle number in the sorted list is our target
            found_num = True # The previous line passes then we can stop here
        else: # If the previous line fails then we begin to play with the indexing of the midpoint and shift +-1
            if target < sorted_list[mid_point_index]: # If the target is less than the mid_point value then we shift down by 1 until we find it
                final_num = mid_point_index - 1
            else: # Else if the target is larger thatn the mid point number then we continue to shift up by one until we find it
                first_num = mid_point_index + 1
    return found_num
# If all of this fails then it will return the default of found_num which is False! 

result = BinarySearch(list_num , 8)
print(result)





