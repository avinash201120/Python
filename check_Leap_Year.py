a = int(input("Enter the number: "))
if (a%4)==0:
    if(a%10)==0:
        if(a%400):
            print("Leap Year")
        else:
            print("Not")
    else:
        print("Leap Year")
else:
    print("Not")                    