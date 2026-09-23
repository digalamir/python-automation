inputFile = open("assets/inputFile.txt", "r")
for line in inputFile:
    split_line = line.split() # Split the line on the basis of space
    if split_line[2] == "P": # filter only the records which are P
        print(line)
inputFile.close()