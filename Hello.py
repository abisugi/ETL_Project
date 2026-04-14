n = int(input().strip())

print("value of n is "n)
if not n % 2 == 0:
    print("weird")
elif n%2 ==0 :
    if  n>= 2 and n <=5 :
        print("Not weird")

    elif  n>=6 and n<=20:
        print("weird")

    elif  n > 20:
        print("Not weird")

