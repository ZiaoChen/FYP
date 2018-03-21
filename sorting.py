def mergeSort(first, last, array):
    if last == first:
        return [array[last]]
    else:
        mid = (first + last) / 2
        first_half = mergeSort(first, mid, array)
        second_half = mergeSort(mid + 1, last, array)
    return merge(first_half, second_half)


def merge(first, second):
    first_index = 0
    second_index = 0
    merged_list = []
    while first_index <= len(first) - 1 and second_index <= len(second) - 1:
        if first[first_index] <= second[second_index]:
            merged_list.append(first[first_index])
            first_index += 1
        else:
            merged_list.append(second[second_index])
            second_index += 1
    merged_list += first[first_index:]
    merged_list += second[second_index:]
    return merged_list


def insertionSort(array):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp
            else:
                break
    return array


def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        first_half, second_half, mid = partition(array)
        first_half = quickSort(first_half)
        second_half = quickSort(second_half)
        return first_half + mid + second_half


def partition(array):
    if len(array) <= 1:
        return [], [], array
    else:
        first_half = []
        second_half = []
        mid = array[len(array) / 2]
        array.remove(mid)
        for i in range(len(array)):
            if array[i] <= mid:
                first_half.append(array[i])
            else:
                second_half.append(array[i])
        return first_half, second_half, [mid]

def heapSort(array):
    new_array = []
    for i in range(len(array)):
        max = getMax(array)
        deleteMax(array)
        new_array = [max] + new_array
    return new_array




a = [22, 23, 123, 66, 4, 42, 32, 7777, 324, 234, 32, 321, 421, 312, 7, 23, 34, 1, 4, 2343243232, 2, 5425, 212412412, 32, 6675, 444, 122143]
import time
start = time.time()
print mergeSort(0, len(a) - 1, a)
print time.time() - start
start = time.time()
print insertionSort(a)
print time.time() - start
start = time.time()
print quickSort(a)
print time.time() - start

