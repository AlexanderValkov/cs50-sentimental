def main():
    while True:
        try:
            change = float(input("Change owed: "))
            if change > 0:
                change = int(change * 100) # convert to cents
                break
        except ValueError:
            pass

    coins = [25,10,5,1]

    i = 0
    coinsTotal = 0

    while change > 0:
        coinAdd = int(change / coins[i])
        #for j in range(coinAdd):
            #print(f"{coins[i]} ", end="")
        coinsTotal += coinAdd
        change = change % coins[i] 
        i += 1

    print(f"{coinsTotal}")


if __name__ == "__main__":
    main()
