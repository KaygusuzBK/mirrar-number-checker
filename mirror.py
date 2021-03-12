while True:
    middleControl = 0
    i = 0
    gs = list(input('Sayı giriniz: '))
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
            print("Bu bir ayna sayıdır.")
        else:
            print("Bu bir ayna sayı değildir.")
    elif gs != r:
        print("Bu bir ayna sayı değildir.")