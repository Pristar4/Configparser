path_input = "C:/Users/felix/Documents/StarCraft II/Accounts/463101077/Hotkeys/Story.SC2Hotkeys"
path_output = "output.txt"

path_io = "io.txt"  # config file for Input -> Output
path_oi = "oi.txt"  # config file for Output -> Input


# map OI
def readmappingtableoi():
    with open(path_oi, "r") as f:
        mapdataoi = f.read()
    mapdataoi = mapdataoi.split("\n")
    mapdataoi = [i.split("=") for i in mapdataoi if i != ""]
    return mapdataoi


# map IO
def readmappingtableio():
    with open(path_io, "r") as f:
        mapdataio = f.read()
    mapdataio = mapdataio.split("\n")
    mapdataio = [i.split("=") for i in mapdataio if i != ""]
    return mapdataio


mapdataoi = readmappingtableoi()
mapdataio = readmappingtableio()


# Input -> Output IO // Load
def convertdata():
    # convert input.txt to output.txt
    inputdata = open(path_input, "r")
    outputdata = open(path_output, "w")

    for line in inputdata:
        for i in range(len(mapdataio)):
            a = mapdataio[i][0]
            b = mapdataio[i][1]

        line = extractline(line, a, b)
        outputdata.write(line)
    inputdata.close()
    outputdata.close()


# Output -> Input OI (reverse) // Save
def reverseconvertdata():  # reverse the conversion process of convertdata()
    # convert input.txt to output.txt
    inputdata = open(path_input, "r")
    outputdata = open(path_output, "w")

    for line in inputdata:
        for i in range(len(mapdataoi)):
            if mapdataoi[i][0] != "":
                a = mapdataoi[i][0]

            if mapdataoi[i][1] != "":  # if the mapping is empty, skip it
                b = mapdataoi[i][1]

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

    return line


# main
def load():
    convertdata()
    print("Loading complete!")


def save():
    reverseconvertdata()
    print("Conversion complete!")
