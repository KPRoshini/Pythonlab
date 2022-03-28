l=[-3,93,27,83,48,-12,-1,77]
def number(num):
  pos= 0
  neg=0
  for j in num:
      if(j>0):
        pos=pos+1
      else:
        neg=neg+1
  print("Number of positive numbers:",pos)
  print("Number of negative number:",neg)
number(l)
