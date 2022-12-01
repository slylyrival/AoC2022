f = open("day1input.txt","r")

mostCals = 0
thisCals = 0
for line in f:
    if line == "\n":
        if thisCals > mostCals:
            mostCals = thisCals
        thisCals = 0
    else:
        thisCals = thisCals + int(line)
    
print(mostCals)
f.close()