import csv
from matplotlib import pyplot as plt

f = open('data01.csv', 'r', encoding='UTF-8')
rdr = csv.reader(f)
temp = []
day = []

for line in rdr:
    temp.append(line[3])
    day.append(line[2])

# print(day)
# print(temp)

xaxis = day
yaxis = temp

plt.plot(xaxis, yaxis)
plt.show()

f.close()
