a = int(input())
if a % 4 == 0:
    if a % 100 == 0:
        if (a % 400 == 0):
            print("leap")
            exit()
        else:
            print("not leap")
            exit()
    print("leap")
else:
    print("not leap")