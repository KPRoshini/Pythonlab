n=int(input("Enter a number:"))

def prime(n):
  for i in range(2,n):
    if (n % i ==0):
      print("It is not a Prime number")
      break
    else:
      print("It is a Prime number")
      break
prime(n)
