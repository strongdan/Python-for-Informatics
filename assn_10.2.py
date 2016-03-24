name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = {}
tuples = []
counts = dict()
lst = list()

for line in handle:
    line = line.strip()
    #only get lines with 'From' at the beginning
    if line.startswith("From "):
        #get the 6th word in words
        time = line.split()[5]
        hour = time.split(":")[0]
        hours[hour] = hours.get(hour, 0) + 1

for key, val in hours.items():
    lst.append( (key, val) )

lst.sort()

for val, key in lst:
    print(val, key)
