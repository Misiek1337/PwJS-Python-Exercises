#!/usr/bin/python3
directory = input("Enter text file directory:")

f = open(directory, encoding="utf8")
text = f.read()

replaced = {"i":"oraz", "oraz":"i", "nigdy":"prawie nigdy", "dlaczego":"czemu"}

split_text = text.split(" ")

for index, word in enumerate(split_text):
    for key in replaced:
        if key.lower() == word.lower():
            split_text[index] = replaced[key]
        if key.capitalize() == word:
            split_text[index] = replaced[key].capitalize()
        if key.lower() + "." == word.lower():
            split_text[index] = replaced[key] + "."

full_string = ' '.join([str(word) for word in split_text]) 

print (full_string)