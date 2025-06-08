print("PROBLEM 1")
# WAP to create a dictionary of Hindi words with values as their english translation.provide user with an optin to look it up!

words = {"madad" : "help" ,"billi" : "cat" ,"kutta" : "dog"  , "kursi" : "chair"}
word = input("Enter the word you want meaning of : ")
print(words[word])


print("PROBLEM 2")
#WAP to input 8 numbers from the user and display all unique numbers (once)
set = set()

nums1 =int(input("Enter  random numbers : "))
nums2 =int(input("Enter  random numbers : "))
nums3 =int(input("Enter  random numbers : "))
nums4 =int(input("Enter  random numbers : "))
nums5 =int(input("Enter  random numbers : "))
nums6 =int(input("Enter  random numbers : "))
nums7 =int(input("Enter random numbers : "))
nums8 =int(input("Enter  random numbers : "))
set.add(nums1)
set.add(nums2)
set.add(nums3)
set.add(nums4)
set.add(nums5)
set.add(nums6)
set.add(nums7)
set.add(nums8)
print("your unique values are : ",set)
