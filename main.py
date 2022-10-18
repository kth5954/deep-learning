import gate

def main():
    x1 = [0, 1, 1, 0]
    x2 = [1, 0, 1, 0]
    for i in range(4):
        print("AND(%d, %d): %d" % (x1[i], x2[i], gate.AND(x1[i], x2[i])))
    for i in range(4):
        print("NAND(%d, %d): %d" % (x1[i], x2[i], gate.NAND(x1[i], x2[i])))


if __name__ == "__main__":
    main()

