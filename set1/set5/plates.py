def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    count = 0
    number_used = False;
    for char in s:
        if char >= '0' and char <= '9':
            if count < 2:
                return False
            elif number_used == False:
                if char == '0':
                    return False
                number_used = True
        elif char.lower() >= 'a' and char.lower() <= 'z':
            if number_used == True:
                return False
        else:
            return False            
        count += 1
    return True;


if __name__ == "__main__":
    main()