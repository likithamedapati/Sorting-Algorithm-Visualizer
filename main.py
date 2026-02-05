import random
import time

print("Sorting Algorithm Visualizer ")
print("-" * 40)

def generate_list(size=8):
    return [random.randint(1, 50) for _ in range(size)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    steps = 0

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps += 1
                print("Step:", arr)
                time.sleep(0.5)

    return steps

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    steps = 0

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            steps += 1
            print("Step:", arr)
            time.sleep(0.5)

    return steps

# Insertion Sort
def insertion_sort(arr):
    steps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            steps += 1
            print("Step:", arr)
            time.sleep(0.5)

        arr[j+1] = key

    return steps

# Bubble Sort Run
arr = generate_list()
print("\nOriginal list:", arr)
print("\nBubble sort visualization:")
sorted_arr = arr.copy()
steps = bubble_sort(sorted_arr)
print("Sorted result:", sorted_arr)
print("Total swaps:", steps)

# Selection Sort Run
arr2 = generate_list()
print("\nNew list for selection sort:", arr2)
print("\nSelection sort visualization:")
sorted_arr2 = arr2.copy()
steps2 = selection_sort(sorted_arr2)
print("Sorted result:", sorted_arr2)
print("Total swaps:", steps2)

# Insertion Sort Run
arr3 = generate_list()
print("\nNew list for insertion sort:", arr3)
print("\nInsertion sort visualization:")
sorted_arr3 = arr3.copy()
steps3 = insertion_sort(sorted_arr3)
print("Sorted result:", sorted_arr3)
print("Total shifts:", steps3)
