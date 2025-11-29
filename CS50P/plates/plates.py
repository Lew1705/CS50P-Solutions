def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    elif not (s[0:1]).isalpha():
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] =="0":
                return False
            if not s[i:].isdigit():
                return False
            break

    if not s.isalnum():
        return False

    else:
        return True




if __name__ == "__main__":
    main()


    # 1. Check length /
    # 2. Check first two are letters /
    # 3. Check where numbers start /
    # 4. Check digits and letters order /
    # 5. Return True or False /
