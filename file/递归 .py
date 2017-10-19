def power(x,y):
    if y == 1:
        return x
    else:
        return x * power(x,y-1)
tem = int(input())
tem2 = int(input())
print(power(tem,tem2))
input()
