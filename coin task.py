#coin task
for coin1 in range(11):     # coin1 in range of 0 to 10
    for coin2 in range(6):  # coin2 in range of 0 to 5
        for coin5 in range(3):  # coin5 in the range of 0 to 2
            for coin10 in range(2):  # coin10 in the range of 0 to 1
                #Calculating the total amount
                total=coin1*1 +coin2*2 +coin5*5 +coin10*10
                if total==10:
                    #Print the combinations
                    print(f"Rs. 1 coins: {coin1}, Rs. 2 coins: {coin2}, Rs. 5 coins: {coin5}, Rs. 10 coins: {coin10}")

