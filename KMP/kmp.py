f = open("KMP/input", "r")
f2 = open("KMP/output", "w")
data = f.read().splitlines()
data = data[1:]
ans = "".join(data)
sps = []
sps.append(0)
sp = 0
x = 1
print(ans)
while x < len(ans):
    if ans[sp] == ans[x]:
        sp += 1
        x += 1
        sps.append(sp)
    else:
        if(sp != 0):
            sp = sps[sp - 1]

        else:
            sps.append(sp)
            x += 1

sps_str = [str(x) for x in sps]
f2.write(' '.join(sps_str))
f.close()
f2.close()
