n = int(input())

for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        if x%2==0:
            continue
        else:
            print("Solo")
    elif x % 5 == 0:
        if x%2==0:
            continue
        else:
            print("Learn")
    elif x%2==0:
        continue
    else:
        print(x)