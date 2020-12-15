#!/usr/bin/python3
directory = input("Enter text file directory:")

f = open(directory, encoding="utf8")
text = f.read()

removed = {"się", "i", "oraz", "nigdy", "dlaczego"}

split_text = text.split(" ")

#Remove words
for string in removed:
    for index, word in enumerate(split_text):
        if string.lower() == word.lower():
            del split_text[index]
        
        #Consider words with dots at the end, same functionality could be implemented for comas, colons etc.
        if word.lower().endswith("."):
                if string.lower() + "." == word.lower():
                    split_text = [i.replace(string + ".", ".") for i in split_text] 

#Cleanup
for index, word in enumerate(split_text):
    if word == ".":
        split_text[index-1] = split_text[index-1] + "."
        split_text.remove(split_text[index])

#Convert list to string
full_string = ' '.join([str(word) for word in split_text]) 

print(full_string)