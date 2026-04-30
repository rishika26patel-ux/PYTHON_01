#STRING FUNCTIONS

# str = "i am a coder."

# str.endswith("er.") #returns true if string ends with substr

# str.capitalize() #capitalizes 1st char

# str.replace(old,new) #replaces all occurrences of old with new

# str.find(word) #returns 1st index of 1st occurrence

# str.count("am") #counts the occurrence of substr in string

str= "i am rishika patel"
print(str.endswith("tel"))


str= "i am rishika"
print(str.capitalize())
print(str)

str="i am rishika"
print(str.replace("i","a"))
print(str.replace("rishika","tanu"))

str="i am rishika "
print(str.find("a"))
print(str.find("am"))

str="i am rishika from from mekh"
print(str.count("from"))

