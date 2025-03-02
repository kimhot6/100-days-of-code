#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from fileinput import close

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

for name in names:
    stripped_name = name.strip("\n")
    content = letter_contents.replace("[name]",stripped_name)
    with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="a") as letter:
        letter.write(content)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp