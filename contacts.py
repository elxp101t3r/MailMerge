class Contacts:
    def __init__(self):
        with open('./Input/Names/invited_names.txt', mode='r') as f:
            self.names = f.read().splitlines()
      