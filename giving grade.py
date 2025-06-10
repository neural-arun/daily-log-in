name = input("Entar your name : ")
roll_no  = int(input("Enter your roll number :"))


phy = int(input("Enter your marks in physics : "))
che = int(input("Enter your marks in chemistry : "))
math = int(input("Enter your marks in mathematics : "))
hindi = int(input("Enter your marks in hindi : "))
eng = int(input("Enter your marks in english : "))
art = int(input("Enter your marks in art : "))

print("Here is your markssheet")

print("Students name : ",name)
print("School : new cambridge sr sec school phoolpur azamgarh")
print("Students roll number : ",roll_no)
print("="*10,"SUBJECT WISE MARKS","="*10)
print("CHEMISTRY",   "-"*10,che)
print("ARTS",        "-"*10,art)
print("PHYSICS",     "-"*10,phy)
print("ENGLISH",     "-"*10,eng)
print("HINDI",     "-"*10,hindi)
print("MATHEMATICS","-"*10,math)

total_marks = phy + che + math + hindi + eng + art
percentage = total_marks/6

if total_marks >= 601 or total_marks <= -1:
    print("Please enter correct marks")

else:
    print("your total marks is ",total_marks,"/600")
    print("Your percentage is : ",percentage)
    
if percentage >= 90:
    print("Your grade is EX(excellent),keep up the good work")

elif percentage >= 80:
    print("Your grade is A,keep up the good work")

elif percentage >= 70:
    print("Your grade is B,keep grinding")
elif percentage >= 60:
    print("Your grade is C,improve")
elif percentage >= 50:
    print("Your grade is D,work hard,you can mprove")
elif percentage >= 33:
    print("Your grade is F,work hard or choose another field")
elif percentage >= 00:
    print("You have failed the exam try again next year")














