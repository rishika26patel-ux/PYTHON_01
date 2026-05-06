#DICTINARY_METHODS
#MyDict.keys() #return all keys
student={
    "name":"rishika",
    "subjet":{
        "phy":97,
        "chem":98,
        "math":95
    }
}

print(student.keys())#print all the outer keys(not print nested keys)
print(list(student.keys()))#print key in list form
print(len(student))#print count of outer keys in dict





#myDict.values()#return all values
print(student.values())
print(list(student.values()))#store dict values in list



#myDict.items()#return all (key,val)pairs as tuples
# print(student.items)
# print(list(student.items))#function ke andar function it is called type casting

# pairs=print(list(student.items))
# print(pairs[0])#print index pairs


#myDict.get("key")#return the key according to value
# print(student["name2"])#error we can egnore this type
# print(student.get("name2"))#no erroe->None


#myDict.update(newDict)#inserts the specified iems to the dictionary
student.update({"city":"delhi" "mumbai"})
print(student)