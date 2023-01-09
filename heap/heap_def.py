import math

l1 = [23, 56, 11, 9, 56, 99, 27, 34]


def make_heap(list):

    heap = [0] * (len(list) + 1)

    child = 1

    for nb in list:
        heap[child] = nb
        parent = math.floor(child / 2)

        if child == 1:
            pass
        else:  # 비교
            temp_child = child
            temp_parent = parent
            while 1:
                if temp_child == 1:
                    break

                if heap[temp_child] >= heap[temp_parent]:
                    break
                else:
                    temp = heap[temp_parent]
                    heap[temp_parent] = heap[temp_child]
                    heap[temp_child] = temp
                    temp_child = temp_parent
                    temp_parent = math.floor(temp_child / 2)

        child += 1
    return heap[1:]


heap1 = make_heap(l1)
while heap1:
    min_value = heap1.pop(0)
    print(min_value)
    heap1 = make_heap(heap1)
