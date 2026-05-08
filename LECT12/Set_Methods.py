#SET METHODS
#IMPORATANT REMARK: set-> mutable
# #:set-> element-> immutable
#UNHASHABLE VALUE(change ho jati hai) -> DICTONARY,LIST


# METHOD1==set.add(el) adds an element

# myinfo={"rishika",19}
# myinfo.add("patel")
# myinfo.add([1,2,33])#unhashable value
# print(myinfo)



# METHOD2==set.remove(el) remove the element an

# myinfo.remove(19)
# print(myinfo)



# METHOD==3 set.clear() empties the set

# myinfo.clear()
# print(len(myinfo))



# METHOD4== set.pop() remove a random value

# print(myinfo.pop())
# print(myinfo.pop())



# METHOD5== set.union(set) combines both set values & returns new

 
# set1 = {1,2,2,3,4,5,5}
# set2 = {6,7,8,9}
# print(set1.union(set2))
# print(set1)



# METHOD6 ==set.intersection(set) combines common values & return new


myname={1,2,3}
mysis={2,3,4}

print(myname.intersection(mysis))