from sys import argv

def main():
    while True:
        try:
            height = int(input("Height: "))
            if height > 0 and height < 23:
                break
        except ValueError:
            pass

    # printing
    for i in range(height):
        j = height - i - 1
        for k in range(j):
            print(f" ", end="")
        for k in range(i + 1):
            print(f"#", end="")
        print("#")
        
if __name__ == "__main__":
    main()
