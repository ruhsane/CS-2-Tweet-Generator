import sys
import random

def read_file(content):
    f = open(content, 'r') # open file at URL
    content = f.read().splitlines() # split file up lines and add each linne to an array named 'content'
    f.close()
    return content

def generate_random(content):
    random_index = random.randrange(0,len(content)) #choose a random index out of the length of the file
    print(content[random_index], end=" ") #print each randomized word, separate with space " "

if __name__ == "__main__":
    content = read_file("/usr/share/dict/words")
    number = int(sys.argv[1]) #take a number argument 
    for x in range(number): #randomly pick a word NUMBER of times
        generate_random(content)
