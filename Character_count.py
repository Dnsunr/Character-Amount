counts = dict()
with open('Randomtxtfile.txt') as f:
    for lines in f:
        characters = list(lines)
for letter in characters:
    counts[letter] = counts.get(letter, 0) + 1

bigcount = None
bigletter = None
for letter,count in counts.items():
    if bigcount is None or count > bigcount:
        bigletter = letter
        bigcount = count
print(bigletter, bigcount)
