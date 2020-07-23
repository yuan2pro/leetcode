# 选择排序
def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            arr[minIndex], arr[i] = arr[i], arr[minIndex]
    return arr


arr = [2, 3, 48, 3, 4, 66, 3]
print(selectionSort(arr))
