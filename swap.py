file = open("label.txt", "r")

for line in file.readlines():
    x = line.split()
    f = x[0]
    s = x[1]
    t = x[2]
    swapped = open("swap.txt", "a")
    swapped.write(t + " " + s + " " + f + "\n")
    swapped.close()
file.close()
