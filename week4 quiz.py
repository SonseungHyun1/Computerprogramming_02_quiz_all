students=[90,45,64,9,17,29]
result=[]
for i in students:
    if i >= 71:
        result.append("A")
    elif i >= 41:
        result.append("B")
    elif i >= 11:
         result.append("C")
    elif i <= 10:
        result.append("D")
print(result)

