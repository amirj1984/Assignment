# this code reads a string and returns the words in that string starting with a vowel
str_raw = input("write a string: ")
str_spl = str_raw.split()
print(str_spl)

i = 0
vowel = ["a", "e", "i", "o", "u"]

while i < len(str_spl):
    word = str_spl[i]
    if word[0].lower() in vowel:
        print(str_spl[i], "is a word starting with a vowel")
    i += 1

