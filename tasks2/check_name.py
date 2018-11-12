'''
    write function that ask about name, eye color, last name,
    also ask if somebody has an animal, if yes ask about the name
    if no then skip question. 

    Create function that returns all the values in dictionary, 
    so you can use it in different file
'''
def check_name():
    print('What is your name?')
    name = input()

    print('What is your last name?')
    last_name = input()

    print('How is your eye color?')
    color = input()

    print('Do you have animal?')
    animals = input()

    if animals == 'Yes':
        print('What is name your animal?')
        name_animal = input()

    personal_data = {
        "name": name,
        "last_name": last_name,
        "color": color,
        "animals": animals,
        "name_animal": name_animal
    }

    return personal_data

pd = check_name()
print(pd)

