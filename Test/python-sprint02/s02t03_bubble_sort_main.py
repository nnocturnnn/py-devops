from bubble_sort import bubble_sort


test_case_1 = [1, 2, 3, -1230]
test_case_2 = [3, 2, 1, 2, 2, 2, 3, 9, 8, 1, 3, 12, 32]


if __name__ == '__main__':
    print(f'Before sorting: {test_case_1}')
    bubble_sort(test_case_1)
    print(f'After sorting: {test_case_1}')

    print('***')
    print(f'Before sorting: {test_case_2}')
    bubble_sort(test_case_2)
    print(f'After sorting: {test_case_2}')
