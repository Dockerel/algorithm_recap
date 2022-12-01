def merge_sort(arr):

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


unsorted_list = [3, 9, 5, 8, 4, 7, 0, 6, 1, 2]
l1 = [2, 4, 3, 1]
print(merge_sort(l1))
