# open inputfile.txt for reading
inputFile = open("assets/inputFile.txt", "r")

# open passfile.txt for writing pass records
passFile = open("assets/passfile.txt", "w")

# open failfile.txt for writing fail records
failFile = open("assets/failfile.txt", "w")

# loop through each records in inputFile.txt
for line in inputFile:
    # split the line on the basis of spaces
    split_file = line.split()
    if split_file[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)   



# close inputFile.txt
inputFile.close()

# close passfile.txt
passFile.close()

# close failfile.txt
failFile.close()