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
    

data1 = read_csv('data1.csv')
data2 = read_csv('data2.csv')



with open('weights.csv') as filew:
    linew = filew.read()
    w = []
    for n in linew.split(','):
        w.append(float(n.strip()))

results = []
for i in range(len(data1)):
    s = 0
    for j in range(len(w)):
        d = data1[i][j] - data2[i][j]
        s += w[j] * abs(d)
    results.append(s)

critical = 0
for i in range(len(results)):  # for all i
    if results[i] > 5:
        critical = critical + 1  # increase by 1
if critical == 1:
    print("criticality: 1 result above 5")
else:
    print("criticality:", critical, "results above 5")
