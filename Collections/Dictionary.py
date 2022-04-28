print("DICTIONARY OPERATIONS")
dic1={"flower":"lilly","cartoon":"tomandjerry","drinks":"rosemilk","ice-cream":"chocolate"}
print("1.Display the elements \n2.Display the datatype \n3.Length of a dictionary \n4.Adding items to the dictionary \n5.Updating the value of a key \n6.Creating a copy of the dictionary \n7.Removing items from the dictionary \n8.Removing all the items from the dictionary \n9.Displaying only keys \n10.Displaying only values \n11.Display full dictionary using for loop \n12.To Check whether an element exists or not" )
n=int(input("Enter your choice:"))
if(n==1):
    print("Displaying dictionary elements:",dic1)
elif(n==2):
    print("Datatype of the elements:",type(dic1))
elif(n==3):
    print("Length of the dictionary:",len(dic1))
elif(n==4):
    print("Adding elements in the dictionary:")
    i=str(input("Enter key:"))
    j=str(input("Enter value"))
    dic1[i]=j
    print("After adding elements in the dictionary:",dic1)
elif(n==5):
    print("Updating the value in the dictionary:",dic1)
    s=str(input("Enter key:"))
    r=str(input("Enter value"))
    dic1[s]=r
    print("After updating the value in the dictionary",dic1)
elif(n==6):
    print("Creating copy of a dictionary:")
    dic2=dic1.copy()
    print ("dictionary1:",dic1)
    print ("dictionary2 :",dic2)
elif(n==7):
    print("Removing items from the dictionary")
    del dic1["drinks"]
    print("After removing:",dic1)
elif(n==8):
    print("Removing all items from the dictionary")
    dic1.clear()
    print(dic1)
elif(n==9):
    print("Displaying only keys:")
    for a in dic1.keys():
      print("Keys are:",a)
elif(n==10):
    print("Displaying only Values:")
    for a in dic1.values():
       print("Values are:",a)
elif(n==11):
    print("Display full dictionary using for loop:")
    for x,y in dic1.items():
      print(x," is to ", y)
elif(n==12):
    print("To Check whether an element exists or not:")
    if dic1.get("flower")==None:
      print ("No such element")
    else:
      print("Element exists")
else:
    print("Invalid Input!!!!")
