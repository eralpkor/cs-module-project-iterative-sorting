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

            
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr

print(selection_sort([0, 2, 34, 22, 10, 19, 17]))