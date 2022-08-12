def binary_search(data, target, low, high):

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)


def binary_search_iterative(data, target):
    low = 0

    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == '__main__':
    data = [int(x) for x in str.split(
        input('Please enter data seperated by commas \n'), ',')]
    target = int(input('Please enter the target... \n'))
    output = binary_search_iterative(data=data, target=target)
    print(output)
