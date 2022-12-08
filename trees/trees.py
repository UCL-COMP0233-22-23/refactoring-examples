"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt

branch_length = 1 # Length of the first branch
start_branch = [[0,1,0]] # List of initial root branches
branches_number = 5 
plt.plot([0,0],[0,1]) # Plots root
for branch in range(branches_number): # Iterates over the number of branches
    end_branch = [] 
    for j in range(len(start_branch)): 
        end_branch.append([start_branch[j][0]+branch_length*sin(start_branch[j][2]-0.1), start_branch[j][1]+branch_length*cos(start_branch[j][2]-0.1), start_branch[j][2]-0.1])
        end_branch.append([start_branch[j][0]+branch_length*sin(start_branch[j][2]+0.1), start_branch[j][1]+branch_length*cos(start_branch[j][2]+0.1), start_branch[j][2]+0.1]) 
        plt.plot([start_branch[j][0], end_branch[-2][0]],[start_branch[j][1], end_branch[-2][1]]) # Plots branches
        plt.plot([start_branch[j][0], end_branch[-1][0]],[start_branch[j][1], end_branch[-1][1]]) # Plots branches
    start_branch = end_branch # Updating the list of branches
    branch_length *= 0.6 # Making each progressive branch level shorter by given factor.
plt.savefig('tree.png') # Saving the plot
