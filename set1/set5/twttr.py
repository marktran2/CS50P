def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    new = ""
    for letter in word:
        if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
            continue
        else:
            new += letter
    return new

if __name__ == "__main__":
    main()