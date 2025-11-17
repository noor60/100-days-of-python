HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
r''' 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= ''',

r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',

r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


player_1=input("Player1: Enter your word: ")
gobal_scope=1
def game():
    '''Function to run the hangman game'''
    local_scope=3
    print(gobal_scope)
    def internal():
            loc_local_scope=10
            print(local_scope)
            print(gobal_scope)
            print(loc_local_scope)
    # print(loc_local_scope) error
    internal() 
    

game()

# anything you name is called namespace and scope is the area where that namespace is accessible.

