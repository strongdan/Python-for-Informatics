file_name = input("Enter a file name: ")
lines = [line.strip('\n') for line in open(file_name, 'r')
         if line.startswith("From ")]
emails = {}

## splits each line into words and counts each occurence
for line in lines:
    words = line.split()
    emails[words[1]] = emails.get(words[1], 0) + 1

## blank variables for 1. most occurrences and 2. the value associated with that key
most_inst = 0
address = None
for email in emails:
    if emails[email] > most_inst:
        most_inst = emails[email]
        address = email

print address, emails[address]
