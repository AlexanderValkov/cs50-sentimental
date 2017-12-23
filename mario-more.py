from sys import argv

def main():
    # check for argument
    if len(argv) != 2:
        print("Usage: python3.6", argv[0], "number")
        exit()

    # check that argument is int
    try:
        num = int(argv[1])
    except ValueError:
        print(argv[1], "is not a number")
        exit()

    # printing
    for i in range(num):
        j = num - i - 1
        for k in range(j):
            print(f" ", end="")
        for k in range(i + 1):
            print(f"#", end="")

        print(f" ", end="")

        for k in range(i + 1):
            print(f"#", end="")
        for k in range(j):
            print(f" ", end="")

        print()

if __name__ == "__main__":
    main()
