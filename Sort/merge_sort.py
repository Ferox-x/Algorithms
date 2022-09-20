from random import randint


def merge(left_arr: list, right_arr: list) -> list:
    """Merging left and right sides"""
    left_index = 0
    right_index = 0
    sorted_array = []
    while True:

        if left_arr[left_index] > right_arr[right_index]:
            sorted_array.append(right_arr[right_index])
            right_index += 1
        else:
            sorted_array.append(left_arr[left_index])
            left_index += 1
        if left_index == len(left_arr):
            sorted_array.extend(right_arr[right_index:])
            break
        if right_index == len(right_arr):
            sorted_array.extend(left_arr[left_index:])
            break

    return sorted_array


def split_array(array: list) -> list:
    """Splitting the array into left and right sides"""
    if len(array) == 1:
        return array
    splited_array = array[:len(array)//2], array[len(array)//2:]
    left_array = split_array(splited_array[0])
    right_array = split_array(splited_array[1])
    return merge(left_array, right_array)


def merge_sort(array: list) -> list:
    """Starting merge sort"""
    return split_array(array)


if __name__ == '__main__':
    non_sorted_array = [randint(0, 100) for _ in range(0, 15)]
    print(non_sorted_array)
    print(merge_sort(non_sorted_array))
