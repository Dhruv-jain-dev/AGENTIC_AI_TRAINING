for i in range(8):
    for j in range(8):
        if i==6:
            print('\u265F',end=' ')
        elif i==1:
            print('\u2659',end=' ')
        elif ((i==0 and j==0) or(i==0 and j==7)):
            print('\u2656',end=' ')
        elif((i==0 and j==1) or (i==0 and j==6)):
            print('\u2658',end=' ')
        elif((i==0 and j==2) or (i==0 and j==5)):
            print('\u2657',end=' ')
        elif(i==0 and j==3):
            print('\u2655',end=' ')
        elif(i==0 and j==4):
            print('\u2654',end=' ')
        elif((i==7 and j==0) or (i==7 and j==7)):
            print('\u265C',end=' ')
        elif((i==7 and j==1) or (i==7 and j==6)):
            print('\u265E',end=' ')
        elif((i==7 and j==2) or (i==7 and j==5)):
            print('\u265D',end=' ')
        elif((i==7 and j==3)):
            print('\u265B',end=' ')
        elif((i==7 and j==4)):
            print('\u265A',end=' ')
        elif(i%2==0 and j%2!=0):
            print('\u25A0',end=' ')
        elif(i%2!=0 and j%2==0):
            print('\u25A0',end=' ')
        else:
            print('\u25A1',end=' ')
    print()
