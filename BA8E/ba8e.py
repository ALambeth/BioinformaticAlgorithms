#Solution to http://rosalind.info/problems/ba8e/
def dist_func(a, b):
    total = 0
    for i in a:
        for j in b:
            total += dis[i][j]
    return total / len(a) / len(b)

f = open("BA8E/input", "r")
temp = []
dis = []
clusters = []
n = 0
p = 0
for line in f.read().splitlines():
    if p == 0:
        n = line.split()
    else:
        temp.append(line.split())
    p += 1
n = int(n[0])

for x in temp:
    temp1 = []
    for y in x:
        temp1.append(float(y))
    dis.append(temp1)

for i in range(n):
    clusters.append([i])

ans = ""
for z in range(0, n - 1):
    d = float('inf')
    a = None
    b = None
    for x in range(0, len(clusters)):
        for y in range(x + 1, len(clusters)):
            newd = dist_func(clusters[x], clusters[y])
            if newd < d:
                d = newd
                a = x
                b = y
    clusters[a] += clusters[b]
    del clusters[b]
    ans += (" ".join([str(x + 1) for x in clusters[a]])) + "\n"
f2 =  open("BA8E/output", "w")
ans = ans[0:len(ans) - 1]

f2.write(ans)

