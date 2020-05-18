# TO-DO: Complete the selection_sort() function below
# places small values into sorted position
# 1. Store the first element as the smallest value you've seen so far.
# 2. Compare this item to the next item in the array until you find a smaller number.
# 3. If a smaller number is found, designate that smaller number to be a new 
# "minimum" and continue until the end of the array.
# 4. If the 'minimum is not the value (index) you initially began with,
# swap the two values.
# 5. Repeat this with the next element until the array is sorted
def selection_sort(arr):
    for i in range(0, len(arr)):
        lowest = i
        # identify the lowest
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest] :
                lowest = j
        # do the swap
        if i != lowest:
            temp = arr[i]
            arr[i] = arr[lowest]
            arr[lowest] = temp
        
    return arr

# def swap2(arr, idx1, idx2):
#     return arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
# swap indexes            
def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
# TO-DO:  implement the Bubble Sort function below
# Where the largest values bubble up to the top! to the end
# 1. Start looping from 
# 2. Inner loop with j from the begining until i - 1
# 3. If arr[j] is greater than arr[j+1], swap those two values!
# 4. Return sorted array
def bubble_sort(arr):
    # no_swaps = None
    for i in range(0, len(arr) - 1):
        no_swaps = True
        for j in range(0, len(arr) - i - 1):
            # print(arr, arr[j], arr[j + 1])
            if arr[j] > arr[j + 1]:
                # swap
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                no_swaps = False
        if no_swaps:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr

# print('Selection sort: ', selection_sort([0, 2, 34, 22, 10, 19, 17]))
print('Bubble sort: ', bubble_sort([27, 45, 29, 8]))
print('Bubble sort: ', bubble_sort([8, 1, 2, 3, 4, 5, 6, 7]))
