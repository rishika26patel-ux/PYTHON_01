#DICTINARY IN PYTHON
#Dictionaries are used to store data values in key:value pairs
#they are unordered,mutable(changeable)& dont allow duplicate keys


#CREATE A DICTIONARY #to assign or new 
dict={
    "name":"rishika",
    "study":"b-tech",
    "topics":("dict","set"),#tuples
    "subjects":["python","c","java"],#list
    "age":19,#int
    "is_adult":True,#boolean
    "marks":95.8#float
}
# print(dict)
print(dict["name"])  #print particular value
print(dict["study"])
print(dict["topics"])
print(dict["subjects"])
print(dict["age"])

#add and assign new value in dictionary
dict["name"]="tanu!!" #overwrite
print(dict)

#create empty dictinary
null_dist={}
null_dist["name"]="rishuu"
print(null_dist)