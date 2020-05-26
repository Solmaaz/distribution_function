import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
data= np.loadtxt('correlation.txt')
list_1 = np.array(data[:,1])
#print (list_1)
max = list_1.max()
min = list_1.min()
print( max, min)
N = int(input("Enter N : "))
Nx = int(input("Enter number of datas: "))
delta = (max- min)/ N
pdf = np.zeros(Nx)
h_list = list()
for i in list_1:
    print(i)
    h= int((i-min)/delta)
    h_list.append(h)
    print(h)
    pdf[h-1]= pdf[h-1] + 1

print(pdf) 
#plt.plot(list_1[0],pdf[0])
#np.savetxt('distribution_output.txt, data, h_list, pdf')
whole = [[data],[h_list],[pdf]]
print(whole)
np.savetxt('distribution_output.txt', whole)
