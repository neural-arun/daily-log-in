# WAP  to find the greatest of four numbers entered by the user 
a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))
c = int(input("Enter number 3 :"))
d = int(input("Enter number 4 :"))

if a>b and a>c and a>d:
    print(a)    
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
elif d>a and d>b and d>c:
    print(d)



if a<b and a<c and a<d:
    print(a)    


elif b<a and b<c and b<d:
    print(b)
elif c<a and c<b and c<d:
    print(c)
elif d<a and d<b and d<c:
    print(d)













else:
    print("incorrect number entered")
    
print("program finished")
