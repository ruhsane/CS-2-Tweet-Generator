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
        print("in range of words")
        word_found = False
        if words_list[i] in words_dict:
            print("word found")
            word_found = True
            for follow_up_words in words_dict[words_list[i]]:
                print("iterate follow ups")
                follow_found = False
                if len(words_list) == i+1:
                    print("last iteration")
                    if len(words_dict[words_list[i]]):
                        break
                    else:
                        words_dict[words_list[i]]={}
                        break
                else:
                    print("not last iteration")
                    if follow_up_words == words_list[i+1]:
                        print("already existed follow up word. add 1 to the count of follow up")
                        follow_found = True
                        words_dict[words_list[i]][follow_up_words] +=1
                        break
                if follow_found == False:
                    print("new follow up word. count 1")
                    words_dict[words_list[i]][words_list[i+1]] = 1
                    break
        if word_found == False:
            print("word not found. a:{i+1 : 1}")
            if len(words_list) == i+1:
                print("last iteration")
                if len(words_dict[words_list[i]]):
                    break
                else:
                    words_dict[words_list[i]]={}
                    break

            else:
                inner_dict = words_dict[words_list[i]]={}
                inner_dict[words_list[i+1]] = 1

    return words_dict

def result_sentence(words_dict):
    pass

if __name__ == "__main__":
    content = read_file("/Users/ruhsane/dev/courses/cs1.2/CS-2-Tweet-Generator/source/story.txt")
    data_structure = data_structure(content)
    print(data_structure)
