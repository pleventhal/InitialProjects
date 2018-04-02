array = [['','I','II','III','IV','V','VI','VII','VIII','IX'],
         ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
         ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
         ['','M','MM','MMM']]

while True:

    numeral = input('What is the Roman Numeral: ')

    if numeral == "0" :
        break;

    number = 0
    breakflag = 0
    level = len(array) - 1 #starts in the thousands and ends in ones

    while level >= 0 and len(numeral) > 0:
        counter = len(array[level]) - 1  # iterates through each element in the level
        levelcounter = 0

        while counter >= 0 and len(numeral) > 0:

            numstring = ''.join(array[level][counter:counter - 1:-1]) #turns list element into a string, this is the list element we are looking for in the numeral

            #print("Looking for ", numstring, " in ", numeral)

            if len(numstring) > 0 and numstring == numeral[:len(numstring)]: #if we find the list element in the numeral
                numeral = numeral[len(numstring):] #take the matched part out of the numeral
                number = number + (counter * 10**level) #add the value of the matched part
                levelcounter = levelcounter + 1

                if levelcounter > 1:
                    breakflag = 1

                #print("Found it!")

            #else:
                #print("Didn't find it!")

            counter = counter - 1 #move to next element in the list

        level = level - 1 #move to the next level in the array

    if len(numeral) > 0 or number == 0 or breakflag == 1:
        print("Not a Roman Numeral")
    else:
        print(number)
