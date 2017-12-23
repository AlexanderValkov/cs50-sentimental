from sys import argv

def main():
    while True:
        try:
            num = int(input("Height: "))
            if num > 0 and num < 23:
                break
        except ValueError:
            pass

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
