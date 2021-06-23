#Solution to http://rosalind.info/problems/ba8c/
def kmeans(k,n,data):
    clusters = []

    for i in range(k):
        clusters.append(data[i])
    step_size = 10000.0

    while step_size > 0:
        new_clusters = step(k, n, data, clusters)
        step_size = 0
        for i in range(0,k):
            step_size  += dist(new_clusters[i], clusters[i],n)

        clusters = new_clusters[:]

    return clusters


def dist(point1, point2, n):
    ans = 0
    for i in range(n):
        ans += (point1[i] - point2[i])**2
    return ans

def near(k, n, data, centres, p):
        index = -1
        best = 10000.0

        for i in range(k):
            dist1 = dist(p,centres[i],n)
            if dist1 < best:
                index = i
                best = dist1

        return index

def cluster(k, n, data, centres, i, indices):
    count = 0
    point = [0 for j in range(n)]
    for j in range(len(data)):
        if indices[j] == i:
            count += 1
            for l in range(n):
                point[l] += data[j][l]
    ans = []
    for p in point:
        ans.append(p / max(count,1))
    return ans

def step(k, n, data, centres):  
    indices = []
    for p in data:
        indices.append(near(k, n, data, centres, p))

    ans = []
    for i in range(0,k):
        ans.append(cluster(k, n, data, centres, i, indices))

    return ans

n = 0
k = 0
points=[]

with open ("BA8C/input") as f:   
    for line in f:
        if k == 0:
            values=line.strip().split()
            k = int(values[0])
            n = int(values[1])
        else:
            points.append([float(v) for v in line.strip().split()])

ans = kmeans(k, n, points)
fin = ""
outp = open("BA8C/output", "w")
count = 1
for p in ans:
    for i in p:
        if(count % n == 0):
            outp.write(str(i) + "\n")
            count += 1
        else:
            outp.write(str(i) + " ")
            count += 1
           




    