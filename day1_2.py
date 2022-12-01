f = open("day1input.txt","r")

thisCals = 0
top3 = [0,0,0]
for line in f:
    top3.sort()
    if line == "\n":
        if thisCals > top3[0]:
            top3.pop(0)
            top3.insert(0,thisCals)
        thisCals = 0
    else:
        thisCals = thisCals + int(line)
    
print(top3[0] + top3[1] + top3[2])
f.close()