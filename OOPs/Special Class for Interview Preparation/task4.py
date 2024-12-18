# homework - 1

# String Methods:
# a. Create a string variable sentence with any sentence of your choice.
# b. Convert the sentence to uppercase.
# c. Split the sentence into a list of words.
# d. Join the words in the list using a space as the separator.
# e. Print the modified sentence.

sentences = "Noman Ali Khan Ki Na Maloom Kahani! "

# print(sentences.upper())
# print(sentences.lower())
# print(sentences.split())
# Splitting by the word "Ki"
# if "Ki" in sentences:
#     parts = sentences.split("Ki", maxsplit=1)
#     print(parts)
# else:
#     print("Word not found!")


# d. Join the words in the list using a space as the separator.

words = sentences.split()
if len(words) > 3:
    part1 = " " . join(words[:3])
    part2 = " " . join(words[3:])
    print([part1 , part2])