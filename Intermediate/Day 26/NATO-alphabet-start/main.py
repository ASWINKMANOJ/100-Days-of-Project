import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict1 = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

l1 = [dict1[letter] for letter in word]
print(l1)
