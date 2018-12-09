import random

def read_file(content):
    words = []
    with open(content) as file:
        for line in file: #for each line of the file
            for word in line.split(): #split the words
                words.append(word)
    return words

def data_structure(words_list):
    words_dict = {}
    for i in range(len(words_list)):
        # loop through every words
        word_found = False
        if words_list[i] in words_dict:
            #word found
            word_found = True
            for follow_up_words in words_dict[words_list[i]]:
                # print("iterate follow ups")
                follow_found = False
                if len(words_list) == i+1:
                    # print("last iteration")
                    if len(words_dict[words_list[i]]):
                        break
                    else:
                        words_dict[words_list[i]]={}
                        break
                else:
                    # print("not last iteration")
                    if follow_up_words == words_list[i+1]:
                        # print("already existed follow up word. add 1 to the count of follow up")
                        follow_found = True
                        words_dict[words_list[i]][follow_up_words] +=1
                        break
                if follow_found == False:
                    # print("new follow up word. count 1")
                    words_dict[words_list[i]][words_list[i+1]] = 1
                    break
        if word_found == False:
            # print("word not found. a:{i+1 : 1}")
            if len(words_list) == i+1:
                # print("last iteration")
                if words_list[i] in words_dict:
                    break
                else:
                    words_dict[words_list[i]]={}
                    break

            else:
                inner_dict = words_dict[words_list[i]]={}
                inner_dict[words_list[i+1]] = 1

    return words_dict

def sample_weighted(words_dict, word):
    words=[]
    inner_dict = words_dict.get(word)
    for word in inner_dict: #go into each value,key of dictionary
        for i in range(inner_dict[word]): #take in the value of the word which is the frequency.
            words.append(word) #add the word to the list based on number of its frequency. ex: if fish:4 , add fish to list four times
    return random.choice(words) #randomly choose word from the new list


def result_sentence(words_dict):
    #pick a random word to start
    # final_words_list = []
    word_is_last = True

    while word_is_last == True:
        start = random.choice(list(words_dict))
        # print(start)
        if len(words_dict[start]):
            word_is_last = False
            # next_word = sample_weighted(words_dict, start)
            final_words_list = [start]
            for i in range(15):
            #     next = sample_weighted(words_dict, next_word)
            # final = " ".join([sentece, next])
                next_is_last=False
                next_word = sample_weighted(words_dict, start)
                start = next_word

                if len(words_dict[next_word]) == 0:
                    next_is_last = True
                    final_words_list.append(next_word)
                    break


                final_words_list.append(next_word)

                # else:
                #     # next_word = sample_weighted(words_dict, start)
                #     final_words_list.append(next_word)

    final_sentence = " ".join(final_words_list)
    return final_sentence

if __name__ == "__main__":
    content = read_file("/Users/ruhsane/dev/courses/cs1.2/CS-2-Tweet-Generator/source/story.txt")
    data_structure = data_structure(content)
    print(data_structure)

    # start = random.choice(list(data_structure))
    # print(start)
    # print(sample_weighted(data_structure, start))
    print(result_sentence(data_structure))
    # sentence = result_sentence(data_structure)
    # print(sentence)
