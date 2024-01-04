file = "books/frankenstein.txt"

def getNumberOfCharacters(text):
    chars = []
    dict = {}

    for t in text:
        chars.append(t.lower().split())

    chars.sort()

    for c in chars:
        if len(c) != 0 and c[0].isalpha():
            if c[0] not in dict:
                dict[c[0]] = 1
            else:
                dict[c[0]] += 1

    return dict

def printBookReport(dct):
    # want to sort by value, use the following, otherwise is alphabetical
    dct = dict(sorted(dct.items(), key=lambda x:x[1], reverse=True))

    print(f"--- Begin report of {file} ---")
    words = sum(dct.values())
    print(f"{words} words found in the document")

    for char in dct:
        print(f"The '{char}' character was found {dct[char]} times")

    print("--- End report ---")

with open(file) as f:
    file_contents = f.read()
    words = file_contents.split()
    dct = getNumberOfCharacters(file_contents)
    printBookReport(dct)
