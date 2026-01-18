def tower_of_hanoi(n, source, target, auxiliary):
    # Solve Tower of Hanoi problem recursively
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Testing Example
if __name__ == "__main__":
    print("MOHIT PRAJAPATI")
    print("FYCS")
    print("22549")
    n = int(input("Enter the number of disk:"))
    print("The moves involved in the Tower of Hanoi are:")
    tower_of_hanoi(n, 'A', 'C', 'B')  # A = source, B = auxiliary, C = target