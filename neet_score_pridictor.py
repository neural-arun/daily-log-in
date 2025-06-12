zoology = int(input("Enter number of CORRECT questions in ZOOlOGY : "))
unzoology = int(input("Enter number of unattempted questions : "))

botony = int(input("Enter number of CORRECT questions in BOTONY : "))
unbotony = int(input("Enter number of unattempted questions : "))

che = int(input("Enter number of CORRECT questions in CHEMISTRY : "))
unche = int(input("Enter number of unattempted questions : "))

phy = int(input("Enter number of CORRECT questions in PHYSICS : "))
unphy = int(input("Enter number of unattempted questions : "))


total_marks = ((zoology*4)-(45-unzoology-zoology)) + ((botony*4)-(45-unbotony-botony)) + ((phy*4)-(45-unphy-phy)) + ((che*4)-(45-unche-che))


if zoology + unzoology > 45 :
    print("WRONG INPUT,please enter correct values")
if botony + unbotony > 45 :
    print("WRONG INPUT,please enter correct values")
if che + unche > 45 :
    print("WRONG INPUT,please enter correct values")
if phy + unphy > 45 :
    print("WRONG INPUT,please enter correct values")
else:
    print("                                       ")
    print("*"*10, "YOUR EVALUATION " ,"*"*10)
    print("                                  ")
    print(" "*10 , "PHYSICS" ,"="*10)

    print(f""" 
           CORRECT MARKS  = {phy*4}
           NEGATIVE MARKS = {45-phy-unphy}
           TOTAL MARKS IN PHYSICS = {((phy*4) - (45-phy-unphy))}
           """)

    
    print(" "*10 , "CHEMISTRY" ,"="*10)

    print(f""" 
           CORRECT MARKS  = {che*4}
           NEGATIVE MARKS = {45-che-unche}
           TOTAL MARKS IN CHEMISTRY = {((che*4) - (45-che-unche))}
           """)

    
    
    print(" "*10 , "BOTONY" ,"="*10)

    print(f""" 
           CORRECT MARKS  = {botony*4}
           NEGATIVE MARKS = {45-botony-unbotony}
           TOTAL MARKS IN BOTONY = {((botony*4) - (45-botony-unbotony))}
           """)

    
    
    print(" "*10 , "ZOOLOGY" ,"="*10)

    print(f""" 
           CORRECT MARKS  = {zoology*4}
           NEGATIVE MARKS = {45-zoology-unzoology}
           TOTAL MARKS IN ZOOLOGY = {((zoology*4) - (45-zoology-unzoology))}
           """)

    negative_marks = (45-che-unche) +(45-phy-unphy) + (45-botony-unbotony) + (45-            zoology-unzoology)
    
    
    print(f"""
          TOTAL CORRECT MARKS : {(che+phy+botony+zoology)*4} ,
          TOTAL NEGATIVE MARKS : {negative_marks} ,
          TOTAL MARKS : {total_marks}
          """)
    if total_marks >= 680 :
        print("""
                       FEEDBACK,
                          WELL DONE , keep grinding""")
    
    elif total_marks >= 650 and total_marks < 680 :
        print("""
                       FEEDBACK,
                          GOOD JOB, keep grinding""")
    
    elif total_marks >= 600 and total_marks < 650 :
        print("""
                 FEEDBACK,
                          IMPROVEMENT NEEDED""")
    
    
    elif total_marks >= 500 and total_marks < 600 :
        print("""
                  FEEDBACK,
                         NEED TO WORK HARD""")
    elif total_marks <500 :
        print("""
                  FEEDBACK,
                          NEED TO WORK VERY HARD OTHERWISE
                          YOU WILL NOT SUCCEED""")
    
    
    