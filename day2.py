# 902
# a = int(input())
# 1 <= a <= 12
# if 1 <= a <=3:
#     print("Initial")
# elif 4 <= a <= 6:
#     print("Average")
# elif 7 <= a <= 9:
#     print("Sufficient")
# elif 10 <= a <= 12:
#     print("High ")

# 8242
# n = int(input())
# if n > 0:
#     print('Positive')
# elif n == 0:
#     print('Zero')
# else:
#     print('Negative')

# 8371
# number = int(input())
# if number % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

# 8521
# x = int(input())
# y = (x**3 + 5*x)
# z = (x**2 - 2*x +4)
# if x >= 10:
#     print(y)
# elif x < 10:
#     print(z)

# 8520
# x = int(input())
# y = (x**2 - 3*x +4)
# z = (x + 7)
# if x < 5:
#     print(y)
# elif x >= 5:
#     print(z)

# 8522
# a,b = map(int, input().split())
# if (a % b) != 0 :
#     print(f"{a//b} {a % b}")
# elif a % b == 0:
#     print("Divisible")

# 8526
# x = int(input())
# y = x + 5
# z = x**2 - 3*x
# c = x**3 +2*x
# if x < -4:
#     print(y)
# elif -4 <= x <= 7:
#     print(z)
# elif x > 7:
#     print(c)

# 8531
# n, a, b = map(int,input().split())
# if n % a == 0 and n % b == 0:
#     print("yes")
# else:
#     print("no")

# 935
# num1 = int(input())
# if num1 < 0:
#     num1*=(-1)

# a = int(num1 / 100)
# b = int(num1 / 10) % 10
# c = int(num1 % 10)
# print(f"{a}\n{b}\n{c}")

# num1 = int(input())
# if num1 < 0:
#     num1 *= (-1)

# a = int(num1 / 1000)
# b = int(num1 / 100) % 10
# c = int(num1 / 10) % 10
# d = int(num1 % 10)
# print(f"{a}\n{b}\n{c}\n{d}")


# 2606
# a, b = map(int, input().split())
# num1 = [a, b]
# print(min(num1),max(num1))

# 6278
# a, b = map(int, input().split())
# num1 = int(a)
# num2 = int(b)
# if (num1 + num2) % 2 != 0:
#     print(0)
# else:
#     print(1)

# 7460
# import math
# # a,b,c = map(int,input().split())
# # n = int(a)
# # m = int(b)
# # k = int(c)
# # room = math.ceil(n / k) + math.ceil(m / k)
# # print(room)