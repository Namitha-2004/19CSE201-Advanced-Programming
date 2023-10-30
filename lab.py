y=int(input("Enter the year to be checked: "))
li=[]
if(y%100==0):
    if(y%400==0):
        print(y," is a leap year")
    else:
        print(y," is not a leap year")
elif (y%4==0):
    print(y," is a leap year")
else:
    print(y," is not a leap year")

for i in range(5):
    li.append(y)
    y=y+4
    i=i+1
    
print(li)
print(li[-2])
print(li[2])
print(li[1:6])


