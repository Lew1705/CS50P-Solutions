import inflect

names=[]
p = inflect.engine()

while True:
    try:
        name = str(input("Enter: "))
        names.append(name)
    except EOFError:
        print()
        break

adieu_list = p.join(names)

print(f"Adieu, adieu, to {adieu_list}")
