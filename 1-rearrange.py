import random

words = ["how","now","brown","cow"]


def random_python_word():
    new_words = []

    #keep going with the loop until the new list word count is equal to the list given at the beginning. meaning done rearranging all the words
    while len(new_words) != len(words):
        rand_index = random.randrange(0, len(words)) #randomly pick an index of word in the list

        if words[rand_index] not in new_words: # check if the word has previously picked
            new_words.append(words[rand_index]) # append the randomly picked word to new list
        else:
            continue # if the word was already has picked before, choose randomly again
    return new_words 

if __name__ == '__main__':
    result = random_python_word()
    print(result)
