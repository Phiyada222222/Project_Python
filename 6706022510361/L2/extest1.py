print("***calculate sum of odd and even number (Exit press 0)")

num2 = 0
num3 = 0

while True :
    number = int(input("Enter number :"))

    if number == 0 :
        break

    elif number%2 == 0:
       num2 = num2+number

    elif number%2 != 0:
        num3 = num3 +number
print("sum of even number :",num2)
print("sum of odd number :",num3)