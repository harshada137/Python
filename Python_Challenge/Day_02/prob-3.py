# Reverse Words in a String
# Input: "Cloud DevOps Engineer"
# Output: "Engineer DevOps Cloud"

text = input("Enter a sentence: ")

words = text.split()        # split the sentence into words
reversed_words = words[::-1]  # reverse the words

result = " ".join(reversed_words)  # join words back into a sentence

print("Reversed sentence:", result)
