import random


def main():
    range = get_level()
    question_count = 0
    correct_count = 0
    while (question_count < 10):
        num1 = generate_integer(range)
        num2 = generate_integer(range)
        solution = num1 + num2

        count = 0
        solved = False
        while (count < 3 and solved == False):
            try:
                response = int(input(f"{num1} + {num2} = "))
            except ValueError:
                continue
            else:
                if response == solution:
                    correct_count += 1
                    solved = True
                else:
                    print("EEE")
                    if count == 2:
                        print(f"{num1} + {num2} = {solution}")
            count += 1
        
        question_count += 1
    
    print(f"Score: {correct_count}")


def get_level():
    while (True):
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level < 1 or level > 3:
                continue
            return level

def generate_integer(level):
    return random.randint(10 ** (level - 1), 10 ** level)


if __name__ == "__main__":
    main()