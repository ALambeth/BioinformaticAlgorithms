f = open("BA5F/input", "r")
f3 = open("BA5F/PAM250.txt", "r")
f2 = open("BA5F/output", "w")
pam = []
def maxThree(a,b,c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c
alphabet = {
    "A" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5,
    "G" : 6,
    "H" : 7,
    "I" : 8,
    "K" : 9,
    "L" : 10,
    "M" : 11,
    "N" : 12,
    "P" : 13,
    "Q" : 14,
    "R" : 15,
    "S" : 16,
    "T" : 17,
    "V" : 18,
    "W" : 19,
    "Y" : 20}

data = f.read().splitlines()
alignment = []
direction = []
for line in f3.read().splitlines():
    pam.append(line.split())
str1 = data[0]
str2 = data[1]
for x in range(0, len(str1) + 1):
    temp = []
    for x in range(0, len(str2) + 1):
        temp.append(0)
    alignment.append(temp)
    direction.append(temp)

best = 0
bestx = 0
besty = 0
for x in range(1, len(str1) + 1):
    for y in range(1, len(str2) + 1):
        cost = [alignment[x - 1][y] - 5,
        alignment[x][y-1] - 5, alignment[x-1][y-1] + int(pam[alphabet[str1[x - 1]]][alphabet[str2[y - 1]]]), 0]
        #print("max cost is: " + str(max(cost)))
        alignment[x][y] = max(cost)
        #print("alignment is: " + str(alignment[x][y]))
        #direction[x][y] = cost.index(alignment[x][y])

        if alignment[x][y] > best:
            print("x: " + str(x) + " y: " + str(y) + " best: " + str(best))
            best = alignment[x][y]
            bestx = x
            besty = y


ans1 = ""
ans2 = ""
i = bestx
print(x)
print(len(str1))
j = besty

while((not i < 0 or not j < 0) and not alignment[i][j] == 0):
    if(abs(alignment[i][j] - (alignment[i-1][j]-5)) <= 0):
        ans1 += str1[i - 1]
        ans2 += "-"
        i -= 1   
    elif(abs(alignment[i][j] - (alignment[i][j-1]-5)) <= 0):
        ans1 += "-"
        ans2 += str2[j - 1]
        j -= 1
    else:
        ans1 += str1[i-1]
        ans2 += str2[j-1]
        j-=1
        i-=1
ans1 = ans1[::-1]
ans2 = ans2[::-1]
f2.write(str(best) + "\n" + ans1 + "\n" + ans2)

