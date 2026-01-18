def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def binary_search(arr, target):
    beg = 0
    end = len(arr) - 1
    while beg <= end:
        mid = (beg + end) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif target < mid_val:
            end = mid - 1
        else:
            beg = mid + 1
    return -1

if __name__ == "__main__":
    print("MOHIT PRAJAPATI")
    print("FYCS")
    print("22549")
    # Get user input for the list
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

    # Get user input for the target number
    target1 = int(input("Enter the number to search for: "))
    # Perform linear search
    linear_result = linear_search(nums, target1)
    if linear_result != -1:
        print(f"Linear Search: Found {target1} at index {linear_result} in the original list.")
    else:
        print(f"Linear Search: {target1} not found.")

    # Sort the list and perform binary search
    sorted_nums = sorted(nums)
    binary_result = binary_search(sorted_nums, target1)
    if binary_result != -1:
        print(f"Binary Search: Found {target1} at index {binary_result} in the sorted list{sorted_nums}.")
    else:
        print(f"Binary Search: {target1} not found not found in sorted list{sorted_nums}.")