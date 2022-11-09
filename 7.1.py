 Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
for character in fh:
    character = character.strip()
    print(character.upper())
