import re


# extract data.txt from the config.txt.txt file
def extractdata():
    with open("config.txt", "r") as f:
        config = f.read()
    config = config.split("\n")
    config = [i.split("=") for i in config if i != ""]
    return config


def convertdata():  # convert data.txt to converted.txt
    data = open("data.txt", "r")
    converted = open("converted.txt", "w")
    config = extractdata()
    for line in data:
        for i in range(len(config)):
            line = line.replace(config[i][0], config[i][1])
        converted.write(line)
    data.close()
    converted.close()


# merge the two functions above into one
def convert():
    convertdata()
    return extractdata()


def rconvert():  # reverse the conversion process
    data = open("converted.txt", "r")
    converted = open("data.txt", "w")
    config = extractdata()
    for line in data:
        for i in range(len(config)):
            line = line.replace(config[i][1], config[i][0])
        converted.write(line)
    data.close()
    converted.close()


# main function
if __name__ == '__main__':
    convert()
