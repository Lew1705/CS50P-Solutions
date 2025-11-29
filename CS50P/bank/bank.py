greeting = input("Greeting: ").strip().lower()  # lowercase for case-insensitive comparison

def value (greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

value(greeting)
