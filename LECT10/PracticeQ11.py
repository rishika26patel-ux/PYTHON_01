#Write a program to check if a list contains a pallindrome pf element.(Hint:use copy()method)
list1=[1,"hello",1]
list2=[1,2,"hello"]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list1):
    print("pallindrome hai")
else:
    print("not a pallindrome")    