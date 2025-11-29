def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    words = str(input("Enter: "))
    print(convert(words))

main()
