import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data)

nato_alpha_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(nato_alpha_dict)

user_input = input("Enter a word:")
# list of phonetic code from word user inputs
nato_user_code = [nato_alpha_dict[f'{char.upper()}'] for char in user_input]
print(nato_user_code)
