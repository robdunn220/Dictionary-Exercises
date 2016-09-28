from sys import argv

script, filename = argv

file_lines = open(filename)

counts = {}

for char in file_lines:
    text = char.replace('.', '').replace('(', '').replace(')', '')
    for word in char.split():
        counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
        print "%s: %d" % (word, counts[word])
        
