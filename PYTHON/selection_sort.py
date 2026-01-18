def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    print("MOHIT PRAJAPATI")
    print("FYCS")
    print("22549")
    user_input = input("Enter a list of numbers (separated by spaces): ")
    arr = list(map(int, user_input.split()))
    print("Before sorting:", arr)
    arr = selection_sort(arr)
    print("After sorting:", arr)
