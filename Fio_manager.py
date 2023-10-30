import random
import pyttsx3
import time
import importlib


speaker = pyttsx3.init()



greetings = ['hey',"hi","hello"]


def organize_files():
    comm = print('Opening file organizer sub program')
    time.sleep(3)
    FileOrganizer = importlib.machinery.SourceFileLoader('fileOrganizerGUI.py', r'C:\Users\judew\Documents\code projects\python\files organizer\fileOrganizerGUI.py').load_module()



def tell_jokes():
    print('Opening jokes sub program')
    time.sleep(3)
    jokesTeller = importlib.machinery.SourceFileLoader('jokesAPI.py', r'C:\Users\judew\Documents\code projects\python\other\jokesAPI.py').load_module()    


def play_youtube():
    print('Opening youtube player  sub program')
    time.sleep(2)
    youtubePlayer = importlib.machinery.SourceFileLoader('youtube.py', r'C:\Users\judew\Documents\code projects\python\sel\youtube.py').load_module()     

def take_notes():
    print('Opening take notes sub program')
    time.sleep(2)
    noteTaker = importlib.machinery.SourceFileLoader('writeNotes.py', r'C:\Users\judew\Documents\code projects\python\other\writeNotes.py').load_module()  


def search_google():
    print('Opening google sub program')
    time.sleep(2)
    noteTaker = importlib.machinery.SourceFileLoader('googleSearch.py', r'C:\Users\judew\Documents\code projects\python\FewInOne\googleSearch.py').load_module() 


def get_recipe():
    print('Opening recipe sub program')
    time.sleep(2)
    noteTaker = importlib.machinery.SourceFileLoader('recipe.py', r'C:\Users\judew\Documents\code projects\python\FewInOne\recipe.py').load_module()    

def shop_online():
    print('Opening shop online sub program')
    time.sleep(2)
    noteTaker = importlib.machinery.SourceFileLoader('jumia.py', r'C:\Users\judew\Documents\code projects\python\sel\jumia.py').load_module() 

count = 0   
global greet
print('''-type 'help-long' to see my commands with explanation
-type 'exit' to exit
-type 'help' to get commands without explanation''')
count += 1
stop = False
while not stop:
    def start():
        greet = input(f'{random.choice(greetings)},how can i help you\n >>: ').lower()
        match greet:
            case 'exit':
                print('OK,,bye hope i\'ll see you soon sir')
                time.sleep(3)
                stop = True
            case "help-long":
                print("""My name is Chad,an AI model created by Jude for assistance (type 'quit' to exit) \n
                -organize files - organizes files by moving them to their respective folders \n
                -play favourite song - plays your set favourite song or playlist from youtube\n
                -play this video - plays the inserted video from youtube\n
                -tell me a joke - tells you a joke\n
                -google this - searches the web for the inserted text\n
                -get recipe - get the recipe of the inserted meal\n
                -shop jumia 'item' - opens jumia and searches for the inserted item\n
                -take notes ' ' - writes the inserted text into a text file \n
                >>: """)
                start()
            case "help":
                print('''
                -organize files,
                -play song,
                -play video,
                -tell me a joke,
                -google this,
                -open app,
                -get recipe,
                -shop online, 
                -take notes \n>>: ''')
                start()
            case "hi":
                start()
            case "files organizer":
                organize_files()
            case "tell me a joke":
                tell_jokes()
            case 'play video':
                play_youtube()
            case 'play song':
                play_youtube()
            case 'take notes':
                take_notes()
            case 'google this':
                search_google()
            case 'get recipe':
                get_recipe()
            case 'shop online':
                shop_online()       
    break      
start()





