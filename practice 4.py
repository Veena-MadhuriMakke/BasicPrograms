# Count the Occurences of the word in teh given Sentence.
def word_count(str):
    count = dict()
    words = str.split() #converts string into list
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count
#str = input("Enter the Sentence : ")
print(word_count(input("Enter the Sentence : ")))

