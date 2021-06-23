# Solution to http://rosalind.info/problems/ba5e/
def maxThree(a,b,c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c
f = open("BA5E/input", "r")
f3 = open("BA5E/BLOSUM62.txt", "r")
f2 = open("BA5E/output", "w")
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
blosum = []
alignment = []
direction = []
for line in f3.read().splitlines():
    blosum.append(line.split())
str1 = data[0]
str2 = data[1]
for x in range(0, len(str2) + 1):
    temp = []
    for x in range(0, len(str1) + 1):
        temp.append(0)
    alignment.append(temp)

for x in range(1, len(str2) + 1):
    alignment[x][0] = alignment[x-1][0] - 5
for x in range(1, len(str1) + 1):
    alignment[0][x] = alignment[0][x - 1] - 5


for x in range(1, len(str2) + 1):
    for y in range(1, len(str1) + 1):
        alignment[x][y] = maxThree(alignment[x - 1][y] - 5,
        alignment[x][y-1] - 5, alignment[x-1][y-1] +int(blosum[alphabet[str2[x - 1]]][alphabet[str1[y - 1]]]) )


ans1 = ""
ans2 = ""
i = len(str2)
j = len(str1)

while(not i == 0 or not j == 0):
    if(abs(alignment[i][j] - (alignment[i-1][j]-5)) <= 0):
        ans1 += str2[i - 1]
        ans2 += "-"
        i -= 1

        
    elif(abs(alignment[i][j] - (alignment[i][j-1]-5)) <= 0):
        ans1 += "-"
        ans2 += str1[j - 1]
        j -= 1
    else:
        ans1 += str2[i-1]
        ans2 += str1[j-1]
        j-=1
        i-=1
ans1 = ans1[::-1]
ans2 = ans2[::-1]
f2.write(str(alignment[len(str2)][len(str1)]) + "\n" + ans2 + "\n" + ans1)






    