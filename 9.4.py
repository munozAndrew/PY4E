name = input("Enter file:")
counts = dict()
bigword = None
bigcount = None
lst3 = []

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith("From "):
        continue
    lst2 = line.strip()
    lst = lst2.split()
    lst3.append(lst[1])
    for word in lst3:
        counts[word] = counts.get(word, 0) + 1
        lst3.clear()
for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword, bigcount)
