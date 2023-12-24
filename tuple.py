n, a, b = map(int,input().split())
if (n % a and n % b) == 0:
    print("YES")
elif (n % a and n % b) != 0:
    print("NO")