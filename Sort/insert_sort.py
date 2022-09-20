from random import randint


def insert_sort(array: list) -> list:
    """Insert sort"""
    for index_x in range(len(array)):
        for index_y in range(index_x):
            if array[index_x] < array[index_y]:
                array[index_x], array[index_y] = array[index_y], array[index_x]
    return array


if __name__ == '__main__':
    non_sorted_array = [randint(0, 15) for _ in range(0, 15)]
    print(non_sorted_array)
    print(insert_sort(non_sorted_array))
