from math import *

# read sample files
def read_csv(csv_file):
    with open(csv_file) as file:
        lines = file.readlines()
        data = []
        for line in lines:
            row = []
            for n in line.split(','):
                row.append(float(n.strip()))
        data.append(row)
    return data    
    

data1 = read_csv('samples1.csv')
data2 = read_csv('samples2.csv')


with open('weights.csv') as filew:
    linew = filew.read()
    w = []
    for n in linew.split(','):
        w.append(float(n.strip()))

results = []
for i in range(len(data1)):
    dis_with_weight = 0
    for j in range(len(w)):
        distance = data1[i][j] - data2[i][j]
        dis_with_weight += weight[j] * abs(distance)
    results.append(dis_with_weight)


dsum =  0
for i in range(len(results)):
    dsum = dsum + results[i]
print("d-index:", dsum/len(results))
