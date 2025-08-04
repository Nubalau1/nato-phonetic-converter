import pandas

# Load the CSV file into a DataFrame
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary: {letter: code}
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Ask the user to input a word and convert it to NATO alphabet
while True:
    try:
        word = input("Enter a word: ").upper()
        list_of_letters = [letter for letter in word]
        list_of_words = [nato_dict[letter] for letter in list_of_letters]
        print(list_of_words)
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please.")