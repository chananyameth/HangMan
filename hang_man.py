from random import randint
import os


#╔════════════╗
#║    init    ║
#╚════════════╝
def get_randon_word():
    num = randint(1, 295828)
    file = open("words.txt", 'r')
    for i in range(num):
        w = file.readline()
    file.close()
    return str.lower(w[:-1])

def setMessage(s):
    global message
    message = s
    
guesses = 0
message = "Hello! Wellcome to Hanging-Tree game!"
word = get_randon_word()
wordToShow = list(" _ " for i in range(len(word)))
alphaBet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
hang = '{3}{3}{3}{3}{3}{3}{3}{3}{3}{3}\n{1} {2}     {4}\n{1}{2}      {5}\n{1}      {7}{6}{8}\n{1}       {6}\n{1}      {9} {10}\n{1}         \n{1}{0}{0}{0}     \n'
hangList = ['_','|','/','_','|','O','|','/','\\','/','\\']
hangListToShow = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
command = "Enter a letter: "


#╔═════════════╗
#║    print    ║
#╚═════════════╝
def print_all(optional=''):
    print(message)
    setMessage("")
    print()
    print_center(" ".join(wordToShow))
    print()
    print_center(alphaBet)
    print()
    print_center(hang.format(*hangListToShow))
    print()
    print(optional)
    return input(command).lower()

def print_center(s):
    print ('\n'.join('{0:^80}'.format(x, 'centered') for x in s.split('\n')))


#╔═══════════════╗
#║    running    ║
#╚═══════════════╝
def good_input(c):  #returns true if the game finished
    global guesses
    global alphaBet
    global wordToShow
    if alphaBet.find(c)!=-1:    # unused letter
        alphaBet = alphaBet.replace(c, "_")
        setMessage(c + ": No letter has discovered... :-(")  #will be changed if new letter has found
        count = 0
        for i in range(len(word)):
            if word[i]==c:
                wordToShow[i] = " "+word[i]+" "
                count += 1
        if count > 0:
            setMessage("Good! You've find " + str(count) + " new letters!")
        else:   #bad guessing
            hangListToShow[guesses] = hangList[guesses]
            guesses += 1
    else:    # used letter
        setMessage("You already used the letter " + c + ". Try another one.")
        
    for item in wordToShow:
        if item == " _ ":
            return False
    return True


#╔═══════════╗
#║    end    ║
#╚═══════════╝
def to_exit():
    q = input("Are you sure? (y/n)  ")
    if q=="y":
        print("Goodbye!")
        return True
    else:
        return False

def done():
    global command
    command = 'Do you want another game? (y/n)  '
    os.system("cls" if os.name=="nt" else "clear")
    optional = ''
    optional += 'DDDD    OOO   N   N  EEEEE  !!\n'
    optional += 'D   D  O   O  NN  N  E      !!\n'
    optional += 'D   D  O   O  N N N  EEEEE  !!\n'
    optional += 'D   D  O   O  N  NN  E        \n'
    optional += 'DDDD    OOO   N   N  EEEEE  !!\n'
    optional += "\n\nTotal guesses: " + str(guesses)

    q = print_all(optional)
    if q=="y":
        return True
    else:
        print("Goodbye!")
        return False

def fail():
    global command
    command = 'Do you want another game? (y/n)  '
    os.system("cls" if os.name=="nt" else "clear")
    optional = ''
    optional += 'FFFFF    A     II  L      !!\n'
    optional += 'F       A A        L      !!\n'
    optional += 'FFF    A   A   II  L      !!\n'
    optional += 'F     AAAAAAA  II  L        \n'
    optional += 'F    A       A II  LLLLL  !!\n'
    optional += "\n\nTotal guesses: " + str(guesses)
    optional += "\n\nThe original word was: " + word

    q = print_all(optional)
    if q=="y":
        return True
    else:
        print("Goodbye!")
        return False
    
def reset():
    global guesses
    global word
    global wordToShow
    global alphaBet
    global hang
    global hangListToShow
    global command
    guesses = 0
    setMessage("Hello! Wellcome to Hanging-Tree game!")
    word = get_randon_word()
    wordToShow = list(" _ " for i in range(len(word)))
    alphaBet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    hang = '{3}{3}{3}{3}{3}{3}{3}{3}{3}{3}\n{1} {2}     {4}\n{1}{2}      {5}\n{1}      {7}{6}{8}\n{1}       {6}\n{1}      {9} {10}\n{1}         \n{1}{0}{0}{0}     \n'
    hangList = ['_','|','/','_','|','O','|','/','\\','/','\\']
    hangListToShow = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    command = "Enter a letter: "


def main():
    reset()
    global guesses
    while True:
        if guesses == 11:                
            if not fail():
                break
            else:
                reset()
        os.system("cls" if os.name=="nt" else "clear")
        c = print_all()
        if c.lower()=="exit":
            if to_exit():
                break
        elif len(c) != 1:
            setMessage("Enter only one letter.")
        elif c.isalpha():
            if good_input(c):                
                if not done():
                    break
                else:
                    reset()
        else:
            setMessage(c + " is not a letter.")
            
if __name__=="__main__":
    main()

# ╣ ║ ╗ ╝ ╜ ╚ ╔ ╩ ╦ ╠ ═ ╬






#__________
#| /     |
#|/      O
#|      /|\
#|       |
#|      / \
#|
#|___

#['_','|','/','_','|','O','|','/','\\','/','\\']
#[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#{3}{3}{3}{3}{3}{3}{3}{3}{3}{3}
#{1} {2}     {4}
#{1}{2}      {5}
#{1}      {7}{6}{8}
#{1}       {6}
#{1}      {9} {10}
#{1}
#{1}{0}{0}{0}

#'__________\n| /     |\n|/      O\n|      /|\\\n|       |\n|      / \\\n|\n|___'

#'{3}{3}{3}{3}{3}{3}{3}{3}{3}{3}\n{1} {2}     {4}\n{1}{2}      {5}\n{1}      {7}{6}{8}\n{1}       {6}\n{1}      {9} {10}\n{1}         \n{1}{0}{0}{0}     \n'
