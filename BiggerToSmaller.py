def findWinner(a, n):
    win = 0
    if (n%2==0):
        win = 1
    else:
        win = 0
    for i in range(n -2,-1,-1):
        if(i%2==1):
            if(win == 0 and a[i] > 1):
                win = 1
            else:
                if (win == 1 and a[i] > 1):
                    win = 0
        if (win == 0):
            print("A")
        else:
            print("B")                            
          