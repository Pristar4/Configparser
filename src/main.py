def readmappingtable():
    with open("config.txt", "r") as f:
        map = f.read()
    map = map.split("\n")
    map = [i.split("=") for i in map if i != ""]
    print(map)
    return map


def convertdata():  # convert input.txt to output.txt
    input = open("input.txt", "r")
    output = open("output.txt", "w")
    map = readmappingtable()
    for line in input:
        for i in range(len(map)):
            a = map[i][0]
            b = map[i][1]
            line = extractline(line, a, b)

        output.write(line)
    input.close()
    output.close()


def reverseconvertdata():  # reverse the conversion process of convertdata()
    input = open("output.txt", "r")
    output = open("input.txt", "w")
    map = readmappingtable()
    for line in input:
        for i in range(len(map)):
            a = map[i][1]
            b = map[i][0]
            line = extractline(line, a, b)

        output.write(line)
    input.close()
    output.close()


def extractline(line, a, b):
    # improvment: use regex to replace
    s = line.split("=")
    left = s[0]
    right = s[1]

    right = right.replace(a, b)
    result = left + "=" + right  # convert this line to a function
    return result


def main():
    convertdata()


# main
if __name__ == "__main__":
    main()
