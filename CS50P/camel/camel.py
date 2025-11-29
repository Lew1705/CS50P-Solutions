camelCase = str(input("Enter a string in camel case: "))
underscore = "_"
result = ""
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        result += underscore + camelCase[(i)].lower()
    else:
        result += camelCase[i]
print(result)
