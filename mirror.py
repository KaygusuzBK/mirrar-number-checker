while True:
    middleControl = 0
    i = 0
    gs = list(input('Enter a number: '))
    r = list(reversed(gs))
    intgs = int(len(gs))
    if gs == r:
        while(i < len(gs)):
            if i != len(gs) and gs[0] == gs[i]:
                i = i + 1
                middleControl = 0
            else:
                middleControl = 1
                break
        if middleControl == 1:
            print("this is mirror number.")
        else:
            print("this is not mirror number.")
    elif gs != r:
        print("this is not mirror number")