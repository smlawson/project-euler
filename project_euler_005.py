i = 2520 #main index (looking for the smallest number that divides evenly into numbers 1,2,3,...,20)

while i < 999999999: #assuming the desired i is in this range . . .
    if i%20 == 0: 
        if i%19 == 0:
            if i%18 == 0:
                if i%17 == 0:
                    if i%16 == 0:
                        if i%15 == 0:
                            if i%14 == 0:
                                if i%13 == 0:
                                    if i%12 == 0:
                                        if i%11 == 0:
                                            print(i)
                                            break
    i += 20 
