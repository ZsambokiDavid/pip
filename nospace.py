file = open("label.txt", "r").read().splitlines()

for line in file:
    x = line.split("-")
    f = x[0]
    s = x[1]
    swapped = open("swap.txt", "a")
    swapped.writelines(s + "-" + f + "\n") # t + " " + 
    swapped.close()
