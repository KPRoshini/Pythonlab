t1=('blue',6,'green',43.2,'yellow')
t2=('red','brown','black')
t3=('Roseisaflower')
t5=(46,72,12,95)
print("Tuple elements are:",t1)
print("Tuple elements are:",t2)
print("Tuple elements are:",t3)
print("1.Data type\n2.Length\n3.Indexing\n4.Unpacking\n5.Concatenation\n6.Removing\n7.Repeating Elements\n8.Print all characters except last 5\n9.Display last element of the t1 \n10.Reversed the order of  t1 \n11.Fetch middle elements of t1 \n12.Fetch portion of an element \n13.Maximum of elements in t2 \n14.Minimum of elements in t2 \n15.Sum of all elements in t2\n16.Sort the tuple t2\n17.Reverse sorting the tuple t2 \n18.Delete a tuple \n19. convert into immutable sequence of elements")
n=int(input("Enter the number:"))
if(n==1):
 print("The date type is:",type(t1))
elif(n==2):
 print("The total length of tuple1 is:",len(t1))
elif(n==3):
 print("The element in the index is:")
 print(t2[2])
elif(n==4):
 print("Unpacking the elements:")
 a,b,c,d,e=t1
 print("After unpacking the elements:",a,b,c,d,e)
elif(n==5):
 t4=t1+t2
 print("After concatenation of elements:",t4)
elif(n==6):
 print("After removing:",t3[4:])
elif(n==7):
   r=str(input("enter the tuple to be repeated : "))
   rn=int(input("enter no of times the tuple to be repeated : "))
   if(r=='t1'):
     print("tuple1 repeatation : ",t1*rn)
   else:
     print("tuple2 repeatation : ",t2*rn)
elif(n==8):
 print("Printing all characters except last 5 characters:",t3[:-5])
elif(n==9):
  print("last element of tuple t1 : ",t1[-1])
elif(n==10):
 print("Reversing the elements in tuple:",t3[::-1])
elif(n==11):
 print("Fetching elements from 4 to 8 :",t3[4:8])
elif(n==12):
 print("Fetching a portion of an element :",t2[1][2:7])
elif(n==13):
 print("The maximum of Tuple6 is :",max(t5))
elif(n==14):
 print("The minimum of Tuple6 is :",min(t5))
elif(n==15):
 print("The sum of elements Tuple6 is :",sum(t5))
elif(n==16):
 print("T5 in sorted order :",sorted(t5))
elif(n==17):
 print("T5 in reverse sorted order :",sorted(t5,reverse=True))
elif(n==18):
  del t2
  print("t5 is deleted : ",t5)
elif(n==19):
  stv="Programmer"
  print("Datatype of stv is : ",type(stv))
  t5=tuple(stv)
  print("Converted into immutable sequence of elements : ",type(t5))
else:
 print("Enter valid input!!!")
