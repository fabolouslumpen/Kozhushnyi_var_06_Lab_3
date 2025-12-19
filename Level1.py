def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        n = int(input("Enter a intager number: "))

        if n < 0:
            print("Enter a positive integer")

        print(f"{n}! = {factorial(n)}")

    except ValueError:
        print("Error: Only integer!")

if __name__ == "__main__":
    main()