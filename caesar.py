from sys import argv

def main():
    # check for argument
    if len(argv) != 2:
        print("Usage: python3.6", argv[0], "number")
        return 1

    # check that argument is int
    try:
        k = int(argv[1])
    except ValueError:
        print(argv[1], "is not a number")
        return 1

    k = k % 26

    plaintext = input("plaintext:  ")
    ciphertext = ""


    for c in plaintext:
        asciiIndex = ord(c)
        if asciiIndex >= 65 and asciiIndex <= 90:
            startIndex = 65
        elif asciiIndex >= 97 and asciiIndex <= 122:
            startIndex = 97
        else:
            s = c
            ciphertext += s
            continue

        alphaIndex = asciiIndex - startIndex
        s = chr((alphaIndex + k) % 26 + startIndex)
        ciphertext += s

    print(f"ciphertext: {ciphertext}")
    return 0

        

if __name__ == "__main__":
    main()
