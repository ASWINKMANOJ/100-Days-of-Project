PLACE_HOLDER = "[Name]"

with open("Names_file/Names.txt") as names_file:
    names = names_file.readlines()


with open("./Letter_Body/Body.txt") as letter_text:
    letter_contents = letter_text.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACE_HOLDER, stripped_name)
        with open(f"./Letters_generated/Letter_for_{stripped_name}.txt", 'w') as completed:
            completed.write(new_letter)