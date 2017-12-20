# read file
fh = open ('a.txt')
ls = list()
timeList= list()
hourList = list()
tup = tuple()
dic = dict()
finalList = list()

# loop into the file line by line
for line in fh :
    # searching for lines start with 'From ' and must contain mor than 30 charcter to make sure that line containe time information
    if line.startswith('From ') and len(line) > 30:
        # spliting line into words and make list of thos words
        ls = line.split()
        # get the time from the splited line 06:12:50
        timeList = (ls[len(ls)-2])
        # get the hours from time list 05:XX:xx , 12:xx:xx
        hourList.append(timeList[:2])
# make dict and count how many each element appeared in the hourlist
for d in hourList :
    dic[d] = dic.get(d,0)+1
# make a final list of tuples each tuple contain the hour and how many it appeared in the file
for k,v in dic.items():
    finalList.append((k,v))
# sort the final list smallest to largest
finalList.sort()
# print the hour 'key' and the count 'value' because the finallist is a list of tuple and each tuple have two element key and value (05 . 2)
for x , y in finalList:
    # print the hour and the count of the hour
    print(x,y)
