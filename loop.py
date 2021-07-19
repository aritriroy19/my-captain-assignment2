num =int( input ( " enter the range number:"))
a=0
b=1
for n in range ( 0,num):
    if (n<=1):
          next=1
    else:
          next=a+b
          a=b
          b=next
    print(next)       

          
