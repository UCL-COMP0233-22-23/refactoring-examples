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
    weight = []
    for n in linew.split(','):
        weight.append(float(n.strip()))

results = []
for i in range(len(data1)):
    dis_with_weight = 0
    for j in range(len(w)):
        distance = data1[i][j] - data2[i][j]
        dis_with_weight += weight[j] * abs(distance)
    results.append(dis_with_weight)


# Show results with weight*distance greater than 5
critical = 0
for i in range(len(results)):  # for all i
    if results[i] > 5:
        critical = critical + 1  # increase by 1

print("criticality:", critical, "results above 5")
