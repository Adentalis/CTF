hits = 0

with open("./data.dat") as f:
    for line in f:
        val0 = line.count('0')
        val1 = line.count('1')
        print( val0 , val1)
        if (val0 % 3 == 0) | (val1 % 2 == 0):
            hits = hits +1

print("flag?: ", hits)