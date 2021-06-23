# Solution to http://rosalind.info/problems/ba1f/
f = open("BA1F/input", "r")
f2 = open("BA1F/output", "w")
data = f.read().splitlines()
ans = "".join(data)
skews = []
skew = 0

for x in range(0, len(ans)):
    if(ans[x] == 'G'):
        skew += 1
    elif(ans[x] == 'C'):
        skew -= 1
    skews.append(skew)
mini = min(skews)
finalAnswer = ""
for x in range(0, len(skews)):
    if skews[x] == mini:
        finalAnswer += str(x + 1) + " "
finalAnswer = finalAnswer[:-1]

f2.write(finalAnswer)
f.close()
f2.close()