
#write a program to print the number ooccurence of a specofied element in the list 

list4=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
def check(a):
  matched=0
  for i in list4:
    if i==a:
      matched=matched+1
  print(a," occured ",matched," times in list3")

a=int(input('enter the number you want to check:'))
check(a)

