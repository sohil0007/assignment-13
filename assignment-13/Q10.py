a = int(input("Enter a number :"))

L = []
while a!=0:
    x=a%10
    L.append(x)
    a=a//10

L.reverse()
print("digit of a given number is:",L)    