import re

text = ""

# task 1

with open("faust.txt", "r", encoding="utf-8") as file:
    for line in file:
        text += line

# task 2

print("case sensitive:")
print(text.count("er"))
print("ignore case: ")
print(sum((1 for _ in re.finditer(r'er', text, re.IGNORECASE))))

# task 3
text_split = text.splitlines()
print(text_split[104-1]) # array starts by 0 --> line 104 is index 103

# task 4
def has_three_sequential_vowels(word):
    vowels = "aeiou"
    vowel_count = 0

    if not word:
        return False

    for char in word[0]:
        if char.lower() in vowels:
            vowel_count += 1
            if vowel_count >= 3:
                return True
        else:
            vowel_count = 0

    return False

result = [word for word in [word.split(" ") for word in text.splitlines()] if has_three_sequential_vowels(word)]
print(result)
print(len(result))