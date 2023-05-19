# Problem - Rotated Lists

# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
# Your function should have the worst-case complexity of O(log N), where N is the length of the list.
# You can assume that all the numbers in the list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
# We define "rotating a list" as removing the last element of the list and adding it before the first element.
# E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

num_list = [5,7,-3,-2]

def count_rotations_of_a_list(num_list):
    print("Implementing binary search for rotations")
    print('List:', num_list)

    start = 0
    end = len(num_list) - 1

    if(len(num_list) == 0 or (num_list[start]<num_list[end])):
        return 0

    while(start <= end):
        mid = (start + end)//2
        if((num_list[mid] < num_list[mid-1])):
            return mid
        elif(num_list[mid] > num_list[end]):
            start = mid + 1
        else:
            end = mid - 1
    return 0 

result = count_rotations_of_a_list(num_list)
if(result==0):
    print("No rotations were made")
else:
    print("The total rotations where  " + str(result))

