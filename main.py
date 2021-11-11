import re

#Get the list of words
f = open("words.txt","r")
lines = f.readlines()

#Iterate over the list of words and build the regex
for idx,line in enumerate(lines, start=1):
    if idx == 1:
        regex = "(\w*"+str.strip(line)+"\w*)|"
    else:
        regex = regex + "(\w*"+str.strip(line)+"\w*)"

#Get a list of sentences
print("Type sentences: ")
sentence = input()
sentenceList = [sentence]
while sentence != '':
    sentence = input()
    sentenceList.append(sentence)
#Removing break line
sentenceList.pop()

#Iterate over the list of sentences and give a result
for idx,sentence in enumerate(sentenceList, start=1):
    x = re.search(regex, sentence, re.IGNORECASE)
    print("Sentence " + str(idx) + ", response should be ", end="")
    if x:
        print("True")
    else:
        print("False")
