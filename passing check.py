s1 = int(input("Enter marks of physics :"))
s2 = int(input("Enter marks of chemistry :"))
s3 = int(input("Enter marks of mathematics :"))

total_percentage = (s1 + s2 + s3)/3

if total_percentage >= 40 and s1>=33 and s2 >= 33 and s3 >= 33:
   
   print("Total percentage is :",total_percentage)
   print("you are passed, congratulations")

else:
    print("Total percentage :",total_percentage)
    print("you have failed,try again ")




