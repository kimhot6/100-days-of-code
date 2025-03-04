import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict={row.letter:row.code for (index,row) in data.iterrows()}

word_input = input("Enter a word: ").upper()
word_list = [alphabet_dict[letter] for letter in word_input]
print(word_list)
