import re

#hand1 = open('regex_sum_177865.txt')
#hand2 = open('regex_sum_42.txt')
#hand = 'Why should you learn to write programs? 7746 12 1929 8827 Writing programs (or programming) is a very creative 7 and rewarding activity.  You can write programs for many reasons, ranging from making your living to solving 8837 a difficult data analysis problem to having fun to helping 128 someone else solve a problem.  This book assumes that everyone needs to know how to program'


text = open('regex_sum_177865.txt')
final = []
for line in text:
    line = line.strip()
    y = re.findall('([0-9]+)',line)

    if len(y) > 0:
         for num in y:
             num = int(num)
             final.append(num)
print(sum(final))
