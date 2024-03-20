# Michael Maniatis - 100876436
# The Teacher gave me permission to do both Quicksort and Mergesort

import time

delay = .5 

def validate_input(message):
    while True:
        current = input(message)
        if current.isdigit():
            return int(current)
        else:
            print("That is not a correct input, please try again")

def quicksort(input_list, start, end):
    time.sleep(delay)
    if start < end:
        pivot = partition(input_list, start, end)

        print(f"Left: {input_list[start:pivot]}")
        print(f"Pivot: {input_list[pivot]}")
        print(f"Right: {input_list[pivot+1:end+1]}\n")

        quicksort(input_list, start, pivot - 1)
        quicksort(input_list, pivot + 1, end)
    return input_list


def partition(input_list, start, end):
    pivot = input_list[end]
    i = start - 1
    for j in range(start, end):
        if input_list[j] < pivot:
            i += 1
            input_list[i],input_list[j] = input_list[j],input_list[i]
    input_list[i + 1],input_list[end] = input_list[end],input_list[i + 1]
    return i + 1

def merge_sort(input_list):
    if len(input_list) > 1:
        time.sleep(delay)
        middle_point = len(input_list) // 2  # Gets Middle Point of Array
        left_list = input_list[:middle_point]  # Splits Array into 2 halves
        right_list = input_list[middle_point:]

        print(f"Left: {left_list}")  # Print the left side
        print(f"Right: {right_list}\n")  # Print the right

        merge_sort(left_list)  # Sorting the first half
        merge_sort(right_list)  # Sorting the second half

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):

            if left_list[i] < right_list[j]:
                input_list[k] = left_list[i]
                i += 1
            else:
                input_list[k] = right_list[j]
                j += 1
            k += 1
        while i < len(left_list):
            input_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            input_list[k] = right_list[j]
            j += 1
            k += 1
        time.sleep(delay)
        print(f"Merged: {input_list}\n")

    return input_list

def main():
    n = validate_input("Please enter the value for n:\n")
    unsorted = []
    for i in range(n):
        unsorted.append(validate_input(f"Please enter the value for item {i+1}: "))

    print("Calling quicksort on the unsorted array")
    time.sleep(delay)
    quicksorted_array = quicksort(unsorted,0, len(unsorted)-1)
    time.sleep(delay)
    print("The sorted array (using quicksort):")
    print(quicksorted_array)


    print("\nCalling mergesort on the unsorted array")
    time.sleep(delay)
    mergesorted_array = merge_sort(unsorted)
    time.sleep(delay)
    print("The sorted array (using mergesort):")
    print(mergesorted_array)


if __name__ == "__main__":
    main()