class Contacts:
    def __init__(self):
        with open('./Input/Names/invited_names.txt', mode='r') as f:
            self.names = f.read().splitlines()
      
class Letters:
    def __init__(self):
        self.o_path = './Output/ReadyToSend/'
        with open('./Input/Letters/starting_letter.txt', mode='r') as f:
            self.letter_text = f.read()
    
    def write_letters(self):
        contacts = Contacts()
        for name in contacts.names:
            with open(f'./Output/ReadyToSend/{name}', mode='w') as f:
                f.write(self.letter_text.replace('[Name]', name))
           

l = Letters()
l.write_letters()

