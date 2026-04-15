file = open("P-04-integers-input.data", "r")
output = open("P-04-JosephNezol-integers-output.data", "w")
for line in file:
    linesplit = line.split(",")
    length = len(linesplit)
    total = 0
    for item in linesplit:
        number = float(item)
        total += number
    print("The sum is: " + str(total) + ". The Number of items: " + str(length) + ". The Average is: " + str(total / length), file = output)
output.close()
