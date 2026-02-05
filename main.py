import random
import time

print("Sorting Algorithm Visualizer ")
print("-" * 40)

def generate_list(size=8):
    return [random.randint(1, 50) for _ in range(size)]

arr = generate_list()
print("Original list:", arr)
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
print("\nBubble sort visualization:")
steps = bubble_sort(arr.copy())
print("Sorted result:", arr)
print("Total swaps:", steps)
