def selection_sort(items):
    result = list(items)

    for i in range(len(result)):
        min_index = i

        for j in range(i + 1, len(result)):
            if result[j] < result[min_index]:
                min_index = j

        result[i], result[min_index] = result[min_index], result[i]

    return result


if __name__ == "__main__":
    numbers = [64, 25, 12, 22, 11]
    sorted_numbers = selection_sort(numbers)

    print("Original:", numbers)
    print("Sorted:  ", sorted_numbers)
