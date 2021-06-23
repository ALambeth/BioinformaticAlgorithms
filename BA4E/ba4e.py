# Solution to http://rosalind.info/problems/ba4e/
mass = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def linear(p):
    prefix = [0]
    length = len(p)
    for x in range(length):
        temp = prefix[x] + p[x]
        prefix.append(temp)
    lin = [0]
    for x in range(length):
        for y in range(x + 1, length + 1):
            lin.append(prefix[y] - prefix[x])
    lin.sort()
    return lin


def consistent(pep, spectrum):
    if sum(pep) > int(spectrum[len(spectrum) - 1]) - mass[0]:
        return False
    x = linear(pep)
    for i in x:
        if i not in spectrum:
            return False
    return True
    

def cyclospectrum(p):
    spectrum = [0, sum(p)]
    x = p + p
    for i in range(1, len(p)):
        for j in range(len(p)):
            sub = x[j: i + j]
            spectrum.append(sum(sub))
    spectrum.sort()
    return spectrum

def CyclopeptideSequencing(spectrum):
    candidate = [[]]
    final = []
    while candidate:
        temp = []

        for x in candidate:
            for y in mass:
                temp.append(x + [y])

        candidate = temp
        for x in candidate:
            if sum(x) == int(spectrum[len(spectrum) - 1]):
                if cyclospectrum(x) == spectrum:
                    final.append("-".join(map(str, x)))
                temp = []
                for peptide in candidate:
                    if peptide != x:
                        temp.append(peptide)
                candidate = temp
            elif not consistent(x, spectrum):
                temp = []
                for peptide in candidate:
                    if peptide != x:
                        temp.append(peptide)
                candidate = temp
    return final


f = open("BA4E/input", "r")

data = f.read().splitlines()
data = data[0].split(" ")
int_data = []
for x in data:
    int_data.append(int(x))
ans = CyclopeptideSequencing(int_data)
print(ans)
f2 = open("BA4E/output", "w")
answer_string = ""
for x in range(len(ans)):
    if x == len(ans) - 1:
        answer_string += ans[x]
    else:
        answer_string += ans[x] + " "
f2.write(answer_string)