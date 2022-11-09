fname = input("Enter file name: ")
fh = open(fname)
count = float(0)
avalue = float(0)
finalvalue = float(0)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    fixvalue = line.strip()
    value = float(fixvalue[20:])
    avalue = avalue + value

finalvalue = avalue/count
print("Average spam confidence:", finalvalue)
