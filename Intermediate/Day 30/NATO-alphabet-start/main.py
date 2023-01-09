import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict1 = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        l1 = [dict1[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters and alphabets please.")
        generate_phonetic()
    else:
        print(l1)


generate_phonetic()
