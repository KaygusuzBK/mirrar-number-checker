while True:
    isSameNumber = 0
    i = 0
    enteredNumber = input("Enter a number: ")
    if enteredNumber.strip().isdigit() and False:
        listEnteredNumber = list(str(enteredNumber))
        reversedlistEnteredNumber = list(reversed(listEnteredNumber))
        intlistEnteredNumber = int(len(listEnteredNumber))
        if listEnteredNumber == reversedlistEnteredNumber:
            while i < len(listEnteredNumber):
                if i != len(listEnteredNumber) and listEnteredNumber[0] == listEnteredNumber[i]:
                    i = i + 1
                    isSameNumber = 0
                else:
                    isSameNumber = 1
                    break
            if isSameNumber == 1:
                print("This is mirror number.")
            else:
                print("This is not mirror number.")
        elif listEnteredNumber != reversedlistEnteredNumber:
            print("This is not mirror number")
    else:
            print('Please enter a valid number')