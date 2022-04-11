from cProfile import label
from collections import Counter
from turtle import color
from matplotlib import pyplot as plt
import  numpy as np

datainput=[{'year' : 2022},{'year' : 2022},{'year' : 2028},{'year' : 2028},{'year' : 2029},{'year' : 2023},{'year' : 2021},{'year' : 2020},{'year' : 2021}, {'year' : 2018},{'year' : 2019},{'year' : 2021},{'year' : 2020},{'year' : 2022}]


llist=[]
cnt = Counter()
for dates in datainput:
    year = dates['year']
    cnt[year] += 1

yearses=[]
popu=[]
for item in cnt.most_common(15):
    yearses.append(item[0])
    popu.append(item[1])

#plt.plot(yearses, popu,color= '#444444', linewidth=3, label='degree')
plt.bar(yearses, popu,color= '#5a7d9a', linewidth=3, label='degree')



plt.title("KPI of publication work's")
plt.xlabel("Years")
plt.ylabel("Number of publication")
plt.tight_layout()
plt.legend()
plt.grid() 


plt.show()
#plt.savefig('plot.png')
