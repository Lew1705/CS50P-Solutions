string = str(input("Enter string: "))
result = ""
def shorten(result):
    for i in range(len(string)):
        if string[i] not in ["a" ,"e", "i", "o", "u", "A" ,"E", "I", "O", "U"]:
            result += string[i] #this rebuilds the string as result and skips vowels
    print(result)


shorten(result)



