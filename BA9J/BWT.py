
#Solution to http://rosalind.info/problems/ba9j/
with open('BA9J/input', 'r') as file:
    data = file.read().replace('\n', '')
print(data)

sort = sorted(data)
i = []
dicti = {}
j = []
dictj = {}

for x in range(len(data)):
    if sort[x] in dicti:
        dicti[sort[x]] += 1
    else:
        dicti[sort[x]] = 1
    i.append((sort[x], dicti[sort[x]]))
    if data[x] in dictj:
        dictj[data[x]] += 1
    else:
        dictj[data[x]] = 1
    j.append((data[x], dictj[data[x]]))

ans = [sort[0]]
isub = 0
for x in range(len(data) - 1):
    ans.append(data[isub])
    isub = i.index((ans[-1], j[isub][1]))
ans = "".join(ans)
print(ans[::-1])
f2 = open("BA9J/output", "w")
f2.write(ans[::-1])