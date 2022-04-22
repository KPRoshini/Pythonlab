def prod_or_sum(n1,n2):
  s=0
  rem=0
  pro=n1*n2
  if(pro > 500):
    print("product of ",n1," and ",n2," is greater than 500 ")
    print("Their product is : ",pro)
    while(pro>0):
      rem = pro % 10
      s=s+rem
      pro=pro//10
    print("So, sum of their product is: ",s)
  else:
    print("product is : ",pro)

num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
prod_or_sum(num1,num2)
