from collections import Counter

with open('input.txt', 'r') as file:
    lines = file.readlines()

def quick_sort(arr):
    if len(arr) <= 1:
        return arr # Base case for recursion
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

left = []
right = []
for line in lines:
    a, b = line.strip().split()
    left.append(int(a))
    right.append(int(b))

sorted_left = quick_sort(left)
sorted_right = quick_sort(right)

count_left = Counter(sorted_left)
count_right = Counter(sorted_right)

#total_distance = 0

#for i in range(len(sorted_left)):
#    total_distance += abs(sorted_left[i] - sorted_right[i])

#print(f'Total distance: {total_distance}')

total_similarity = 0
for i in range(len(sorted_left)):
    total_similarity += sorted_left[i] * count_right[sorted_left[i]]

print(f'Total similarity: {total_similarity}')

