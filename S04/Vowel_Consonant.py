# this code reads a letter (either lower- or uppercase) and says if it is Vowel or Consonant

alph_raw = input("enter a letter of the alphabet: ")
alph = alph_raw.lower()
vowel = ["a", "e", "i", "o", "u"]

if alph in vowel:
    print("this letter is a vowel")
elif alph == "y":
    print("this letter can be either a vowel or a consonant")
else:
    print("this letter is a consonant")




