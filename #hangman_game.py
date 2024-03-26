#hangman_game
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words=['cake','chocolate','snacks']
choose=random.choice(words)
fina=[]
length=len(choose)
lives=6
for letter in range(length):
    fina +='_'
print(fina)
end_of_game=False
while not end_of_game:
    guess=input("guess a letter:").lower()
    for i in range(length):
        letter=choose[i]
        if letter==guess:
            fina[i]=letter
    if guess not in choose:
        lives-=1
        if lives==0:
            end=True
    print(fina)
    if "_" not in fina:
        end_of_game=True
        print("you win")
    print(stages[lives])


