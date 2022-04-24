def readmappingtable():
    with open("config.txt", "r") as f:
        mapdata = f.read()
    mapdata = mapdata.split("\n")
    mapdata = [i.split("=") for i in mapdata if i != ""]
    print(mapdata)
    return mapdata


def convertdata():  # convert input.txt to output.txt
    inputdata = open("input.txt", "r")
    outputdata = open("output.txt", "w")
    mapdata = readmappingtable()
    for line in inputdata:
        for i in range(len(mapdata)):
            a = mapdata[i][0]
            b = mapdata[i][1]
            line = extractline(line, a, b)

        outputdata.write(line)
    inputdata.close()
    outputdata.close()


def reverseconvertdata():  # reverse the conversion process of convertdata()
    inputdata = open("output.txt", "r")
    outputdata = open("input.txt", "w")
    mapdata = readmappingtable()
    for line in inputdata:
        for i in range(len(mapdata)):
            a = mapdata[i][1]
            b = mapdata[i][0]
            line = extractline(line, a, b)

        outputdata.write(line)
    inputdata.close()
    outputdata.close()


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
