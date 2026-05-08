#WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one. use subject name as key & marks as value
marks={}

x= int(input("enter chem marks:"))
marks.update({"chem":x})

x=int(input("enter math marks:"))
marks.update({"math":x})

x=int(input("enter phy marks:"))
marks.update({"phy":x})


print(marks)