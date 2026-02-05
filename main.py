import random
import time

print("Sorting Algorithm Visualizer ")
print("-" * 40)

def generate_list(size=8):
    return [random.randint(1, 50) for _ in range(size)]

arr = generate_list()
print("Original list:", arr)
