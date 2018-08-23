# q-1 Get Keys Corresponding to a Value in User Defined Dictionary
dict={}
for i in range(1,5):
    key = input("Enter key: ")
    value = input("Enter  value: ")
    dict[key] = value
print(dict)
# q-2 Nested Dictionary
dict1={}
dict2={}
for i in range(1,4):
    dict2={}
    name = input("Enter name ")
    for j in range(1,4):
              sub=input("enter subject")
              marks=int(input("enter marks"))
              dict2[sub]=marks
    dict1[name]=dict2
print(dict1)
student=input("Enter the student's name")
print(dict1[student])
