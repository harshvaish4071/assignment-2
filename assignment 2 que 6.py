#to check if three lines can form a triangle
len1=int(input('enter the length of first line:'))
len2=int(input('enter the length of second line:'))
len3=int(input('enter the length of third line:'))
if (len1>len2+len3):
    print('triangle can not form')
elif (len2>len1+len3):
    print('triangle can not form')
elif (len3>len2+len1):
    print('triangle can not form')

else:
    print('triangle can be formed')