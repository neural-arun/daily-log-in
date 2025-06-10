# DICTIONARY AND SETS 
# dictionary contains key value pairs 
marks  = {"Harry" : 100, "Arun" : 100 ,"sarita" : 23 , "uday" : 67}
print(type(marks),marks)
print(marks["uday"])  
a=marks.items()  # returns a list of (key,value) tuples
print(a)
print(len(marks))
print(marks.keys())  # returns a list of containing dictinary keys
print(marks.get("Arun"))  # returns the value of the specified keys 
marks.update({"sanni" : "12" })  # ye nayi key value ko jod deta hai 
print(marks)
marks.update({"Arun" : 98})  # existing key ke values ko bhi update kar sakte ho 
print(marks)
print(marks.get("Arun"))
print(marks["Arun"])  # in dono mein fark hai 
print(marks.get("Arun2"))  # ye none dega 
#print(marks["Arun2"]) # ye error dega x
#SETS IN PYTHON
#   set is defined as a collection of objects 
empty_dict = {}  # agar aise kiya to empty dict bn jayegi
empty_dict1 = {1,2,34,}  # ab ye set hai 
print(type(empty_dict))   # dict
print(type(empty_dict1))  # SET
# ab question ye hai ki empty set kaise banaye
a = set() # ye hai empty set
print(type(a))   # set
# set mein elements repeat nhi ho sakta
#SETS METHODS
set = {344,3344,52,52,23355,344,3344,52,52,23355,223,"arun yadav","Subash yadav" ,"cooked"}
print(set)
print(len(set))
print(type(set))
set.add(565)  # ye khali 1 argument leta hai bro dhyan se
print(set)    
# set properties ;
'''unorderd,un indexed ,there is no way to change items in sets ,sets cannot contain duplicate values'''
#OPERATIONS ON SETS 
set = {344,3344,52,52,23355,344,3344,52,52,23355,223,"arun yadav","Subash yadav" ,"cooked"}
set.remove(3344) # ye remove kar dega elements ko no matter kitni baar vo element aaya hai set mein
print(set)
set.pop() #ye kisi bhi random element ko delete kar dega
print(set)
set.clear()
print(set)  # ye set ko clear kar deta hai 
                    
## operations on sets 
s1 = {1,2,3,4,56}                        
s2 = {4,5,6,7,8,56}
print(s1.union(s2))                 

print(s1.intersection(s2))
print(s1-s2)  # s2 ko bahar fk dega (jo s1 mein ho but s2 mein na ho)                                          
print(s2-s1)  # jo 2 mein ho but 1 mein na ho 

                                        
                                                                                
                                                                                                                        
                                                                                                                                                                
                                                                                                                                                                                                        
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                            
                                             
                                                  
                                                       
                                                            
                                                                      
      
        






