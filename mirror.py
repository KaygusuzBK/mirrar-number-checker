import text
while True:
    isSameNumber = 0
    i = 0
    enteredNumber = input(text.ask)
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
                print(text.succesfull)
            else:
                print(text.error)
        elif listEnteredNumber != reversedlistEnteredNumber:
            print(text.error)
    else:
            print(text.valid)