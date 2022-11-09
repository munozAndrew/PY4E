counts = dict()
lst3 = []
lst5 = []
lst6 = []
lst7 = []
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for word in handle:
    if not word.startswith("From "):
        continue
    lst = word.strip()
    lst2 = lst.split()
    #print(lst2)
    lst3 = lst2[5]
    lst4 = lst3.split(":")
    #print("amogus", lst4)
    lst5.append(lst4[0])
    #print(lst5)
for word in lst5:
    counts[word] = counts.get(word, 0 ) + 1




for key, val in counts.items():
    newtup = (key, val)
    lst6.append(newtup)

lst6 = sorted(lst6, reverse=False)
#print(lst5)
for val, key in lst6:
    print(val, key)
        #print("amogus")
