fh = open('a.txt')
dic = dict()
ls = list()
count = 0
bigValue = 0
bigKey =''
# looping in the file line by line
for line in fh :
    # searching for lines start with From
    if line.startswith('From'):
        # if we found the line start with from thin split it and stor it into list
        ls = line.split()
        # stor the second element in the list as a key to use it later
        key = ls[1]
        # use the list of keys as a key of the dictionary and count how many time each key apperce
        dic[key] = dic.get(key,0)+1
# looping into the dict with two refrence one for the value and the other for the key
for k,v in dic.items():
    # if the value in the dict is none or bigger than the bigValue variable then stor the v refrence into the bigValue
    # each time the v stor the value into bigValue to get the largest value
    if v is None or v>bigValue:
        bigValue = v
        # each time 
        bigKey = k
print(bigKey,bigValue)
