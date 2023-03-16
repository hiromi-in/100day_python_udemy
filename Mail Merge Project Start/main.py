#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


###with open('./Input/Names/invited_names.txt') as name:
###    name_list = name.readlines()
###    i = 0
###
###    with open("./Input/Letters/starting_letter.txt") as letter:
###        bday_letter = letter.read()
###
###    for name in name_list:
###        name_list[i] = name.replace("\n", '')
###        i += 1
###
###    for i in range(len(name_list)):
###        with open(f"./Output/ReadyToSend/letter_for_{name_list[i-1]}.txt", mode="w") as sent_letter:
###            sent_letter.write(bday_letter.replace("[name]", f"{name_list[i-1]}"))
###
###

PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

    with open("./Input/Letters/starting_letter.txt") as letter:
        draft = letter.read()

        for name in name_list:
            name = name.strip()
            new_letter = draft.replace(PLACE_HOLDER, name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as send_letter:
                send_letter.write(new_letter)
