def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"move disk 1 from {source} to {target}")
        return

    hanoi(n - 1, source, target, auxiliary)

    print(f"move disk {n} from {source} to {target}")

    hanoi(n - 1, auxiliary, source, target)


def main():
    n = int(input("enter number of disks (n < 6): "))

    if n <= 0 or n >= 6:
        print("error: n must be 1 to 5.")
        return

    print("solution steps:")
    hanoi(n, "A", "B", "C")


if __name__ == "__main__":
    main()
