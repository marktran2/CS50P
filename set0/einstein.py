def main():
    m = int(input("m: "))
    c = 300000000
    print("E:", calculateE(m, c))

def calculateE(m, c):
    return m * (c ** 2)


main()