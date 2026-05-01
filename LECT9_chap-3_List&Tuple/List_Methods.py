#LIST METHODS
list=[1,2,3,5,4]
list.append(7)#adds one element at the end of list
print(list)



list=[1,3,4,2]
list=["banana","mango","litchi","guava","apple"]
list=["b","c","a","d","f","e"]
list.sort()#sorts in ascending order
print(list)



list=[1,2,3,4,5]
list=["banana","mango","litchi","apple"]
list=["b","c","a","d","f","e"]
list.sort(reverse=True)#sort in decending order
print(list)



list=["rishika","tanushka","anuvansh","rachna","prakash"]
list.reverse()#reverse list
print(list)


list=[1,2,3,4,5]
#list.insert(idx,element)
list.insert(1,5)#insert element at index(particular index)
print(list)


list=[2,1,3,1]
list.remove(1)#remove first occurence of element
print(list)


list=[2,1,3,1]
list.pop(2)#remove element at idx
print(list)


list=["ab","cde"]
list.count(2)
print(list)