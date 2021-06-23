# Solution to http://rosalind.info/problems/ba1d/
import time
start_time = time.time()
f = open("BA1D/input", "r")
f2 = open("BA1D/output", "w")
data = f.read().splitlines()

patt = data[0]
data = data[1:]
str1 = ''.join(data)
ans = []
for x in range(0, len(str1) - len(patt) + 1):
    nomatch = False
    for y in range(0, len(patt) - 1):
        if not str1[x + y] == patt[y]:
            nomatch = True
    if not nomatch:
        ans.append(str(x))
print("--- %s seconds ---" % (time.time() - start_time))
f2.write(' '.join(ans))
f.close()
f2.close()