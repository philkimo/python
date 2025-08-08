num = 17
print("Table of 17")
for i in range(1,11):
  mul = num*i
  print("17 x %d= %d" % (i,mul))
  num = 9 
  
  flag = False
  
  if num > 1:
    # check for factors 
    for i in range(2, num):
        if (num% i) ==0 :
        Flag = True 
        break
    
    
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is  a prime number")