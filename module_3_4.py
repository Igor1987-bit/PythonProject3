# Declaration of function single_root_words
def single_root_words(root_word, *other_words):
    same_words = []
    list_words = list(other_words) # Simply enumerate words into a word list
    # Cross-checking of the occurrence of a word in a part of a word from the list or vice versa
    for i in range(len(list_words)): # Iterate over each element of a list_words using its index
        # Using the count() method and the in operator
        if (list_words[i].lower()).count(root_word.lower()) or list_words[
            i].lower() in root_word.lower():
            same_words.append(list_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
# Consol
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']

