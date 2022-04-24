path_input = "C:/Users/felix/Documents/StarCraft II/Accounts/463101077/Hotkeys/Story.SC2Hotkeys"
path_output = "output.txt"


def readmappingtable():
    with open("config.txt", "r") as f:
        mapdata = f.read()
    mapdata = mapdata.split("\n")
    mapdata = [i.split("=") for i in mapdata if i != ""]
    return mapdata


def convertdata():  # convert input.txt to output.txt
    inputdata = open(path_input, "r")
    outputdata = open(path_output, "w")
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
    inputdata = open(path_output, "r")
    outputdata = open(path_input, "w")
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



# main
if __name__ == "__main__":
    convertdata()
