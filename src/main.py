path_input = "input.txt"
path_output = "output.txt"


def readmappingtable():
    with open("config.txt", "r") as f:
        mapdata = f.read()
    mapdata = mapdata.split("\n")
    mapdata = [i.split("=") for i in mapdata if i != ""]
    return mapdata


mapdata = readmappingtable()
print(mapdata)


def convertdata():
    # convert input.txt to output.txt
    inputdata = open(path_input, "r")
    outputdata = open(path_output, "w")

    for line in inputdata:
        for i in range(len(mapdata)):
            a = mapdata[i][1]
            b = mapdata[i][0]
            line = extractline(line, a, b)
        outputdata.write(line)
    inputdata.close()
    outputdata.close()


def reverseconvertdata():  # reverse the conversion process of convertdata()
    # convert input.txt to output.txt
    inputdata = open(path_input, "r")
    outputdata = open(path_output, "w")

    for line in inputdata:
        for i in range(len(mapdata)):
            a = mapdata[i][0]
            b = mapdata[i][1]
            line = extractline(line, a, b)
        outputdata.write(line)
    inputdata.close()
    outputdata.close()


def extractline(line, a, b):
    # Check for "=" in line
    if "=" in line:
        line = line.split("=", 1)  # split line into two strings
        line[1] = line[1].strip()  # remove whitespace from the right side of the string
        line[1] = line[1].replace(a, b)  # right string and replaced a with b
        line = "=".join(line)
        line = str(line + "\n")  # join the two strings

    # convert line to string

    return line


# main
if __name__ == "__main__":
    convertdata()
    print("done")
