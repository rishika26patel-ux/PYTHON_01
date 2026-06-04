# ASCII full form==> american standard code for information interchange

import random
import string

pass_len=12
charValues=string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is:",password)    




# AGAIN WE GENERATE PASSWORD USING "LIST COMPREHENTION"

import random
import string

pass_len=12
charValues=string.ascii_letters + string.digits + string.punctuation

res=[random.choice(charValues) for i in range(pass_len)]
print(res)


res="%".join([random.choice(charValues) for i in range(pass_len)])
print(res) #.join is used to concatinate the string
