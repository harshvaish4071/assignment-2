#to find the greatest value
num1=int(input('enter the 1st number:'))
num2=int(input('enter the 2nd number:'))
num3=int(input('enter the 3rd number:'))
if (num1>num2)and(num1>num3):
    print('the greatest number is :',num1)
elif (num2>num3)and(num2>num1):
    print('the greatest number is :',num2)
elif (num3>num2)and(num3>num1):
    print('the greatest number is :',num3)