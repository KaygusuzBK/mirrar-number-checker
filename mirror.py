while True:
    isSameNumber = 0
    i = 0
    enteredNumber = list(input('Enter a number: '))
    reversedEnteredNumber = list(reversed(enteredNumber))
    intenteredNumber = int(len(enteredNumber))
    if enteredNumber == reversedEnteredNumber:
        while(i < len(enteredNumber)):
            if i != len(enteredNumber) and enteredNumber[0] == enteredNumber[i]:
                i = i + 1
                isSameNumber = 0
            else:
                isSameNumber = 1
                break
        if isSameNumber == 1:
            print("this is mirror number.")
        else:
            print("this is not mirror number.")
    elif enteredNumber != reversedEnteredNumber:
        print("this is not mirror number")