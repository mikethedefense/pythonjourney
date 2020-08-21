# Python Dictionary Exercise 4
# Write a code that will print out the anagrams from a paragraph of text. 

# Variables
paragraph = "A green hunting cap squeezed the top of the fleshy balloon of a head deah"
paragraph = paragraph.lower()
words = paragraph.split(" ")
anagrams = {}

# For loop checking for the anagram

for word in words:
    _sorted = "".join(sorted(word))
    anagrams.setdefault(_sorted, []).append(word)

# Print out the anagrams

print(list(anagrams.values()))
