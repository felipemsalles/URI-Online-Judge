while True:
    X, Y = map(int, input().split())
    if X == 0 or Y == 0:
        break
    else:
        if X > 0 and Y > 0:
            print('primeiro')
        elif X > 0 and Y < 0:
            print('quarto')
        elif X < 0 and Y < 0:
            print('terceiro')
        else:
            print('segundo')

