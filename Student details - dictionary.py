student ={"name":"John","age":25,"courses":["Math","Science"]}
print(student["name"])
student["age"]=26
student["grade"]="A"
del student["age"]
print(student["grade"])
student["age"]=20
print(student["age"])
for key,value in student.items():
    print(key,value)
