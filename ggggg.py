Список = "mydata.txt"
fd = open(Список, "w")
for i in range(10):
    A = i*18
    fd.write("%i\t%.1f\n" % (i, A))
fd.close()
import csv
import sys
Список = "mydata.txt"
fd = open(Список, "r")
reader = csv.reader(fd, delimiter="\t")
for row in reader:
     print(row)
fd.close() 
     


 
