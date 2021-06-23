# Solution to http://rosalind.info/problems/ba2e/
temp = []
f1 = open("BA2E/input", "r")
for line in f1.read().splitlines():
    temp.append(line)

alphabet_num = {
    "A" : 0,
    "C" : 1,
    "G" : 2,
    "T" : 3
}
num_alphabet = {
    0 : "A",
    1 : "C",
    2 : "G",
    3 : "T"
}

def probableKmer(text, k, profile):
	maxp = 0
	kmer = text[0:k]
	for x in range(0,len(text) - k +1):
		z = 1
		patt = text[x:x+k]
		for y in range(0, k):
			l = alphabet_num[patt[y]]
			z = z * profile[l][y]
		if z > maxp:
			maxp = z
			kmer = patt
	return kmer

def score(motifs):
	profile = profileForm(motifs)
	cons = ""
	for i in range(0, len(profile[0])):
		maxScore = 0
		z = 0
		for j in range(0, 4):
			if profile[j][i] > maxScore:
				z = j
				maxScore = profile[j][i]
		cons += num_alphabet[z]
	score = 0
	for x in motifs:
		for y in range(0, len(x)):
			if cons[y] != x[y]:
				score += 1
	return score

def profileForm(motifs):
	k = len(motifs[0])
	profile = [[1 for i in range(0, k)] for j in range(0, 4)]
	for x in motifs:
		for i in range(0, len(x)):
			j = alphabet_num[x[i]]
			profile[j][i] += 1
	for x in profile:
		for y in x:
			y = y/len(motifs)
	#print(profile)
	return profile



def greedyMotifSearch(dna, k, t):
	best = []
	for x in dna:
		best.append(x[0:k])
	for i in range(0, len(dna[0]) - k + 1):
		motifs = []
		motifs.append(dna[0][i:i+k])
		for j in range(1,t):
			profile = profileForm(motifs)
			motifs.append(probableKmer(dna[j], k, profile))



		if score(motifs) < score(best):
			best = motifs
	return best

valu = temp[0].split(" ")
print(valu)
k = int(valu[0])

t = int(valu[1])

temp = temp[1::]
dna = []
for x in temp:
	dna.append(x)


a = greedyMotifSearch(dna, k, t)
f2 = open("BA2E/output", "w")

for x in a:
	f2.write(x + "\n")




    
    