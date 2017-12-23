from sys import argv

def main():
    # check for argument
    if len(argv) != 2:
        print("Usage: python3.6", argv[0], "keyword")
        return 1

    keyword = argv[1]

    # check if it's alphabetical
    if not isAlphaWord(keyword):
        print("Only alphabetical keywords are allowed")
        return 1

    plaintext = input("plaintext:  ")
    ciphertext = ""

    j = 0

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

        k = getCharAlphaIndex(keyword[j])
        j += 1
        j = j % len(keyword)

        alphaIndex = asciiIndex - startIndex
        s = chr((alphaIndex + k) % 26 + startIndex)
        ciphertext += s

    print(f"ciphertext: {ciphertext}")
    return 0

        
def isAlphaWord(word):
    for c in word:
        asciiIndex = ord(c)
        if asciiIndex >= 65 and asciiIndex <= 90:
            continue
        elif asciiIndex >= 97 and asciiIndex <= 122:
            continue
        else:
            return False
    return True

def getCharAlphaIndex(ch):
    chAsciiIndex = ord(ch)
    if chAsciiIndex >= 65 and chAsciiIndex <= 90:
        chStartIndex = 65
    elif chAsciiIndex >= 97 and chAsciiIndex <= 122:
        chStartIndex = 97

    chAlphaIndex = chAsciiIndex - chStartIndex
    return chAlphaIndex


if __name__ == "__main__":
    main()
