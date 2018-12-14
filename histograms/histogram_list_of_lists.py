def histogram():
    histogram = []
    words = []
    with open("/Users/ruhsane/dev/courses/cs1.2/tweet-generator/histograms/source.txt") as f:
        for line in f:
            for word in line.split():
                words.append(word)

    for word in words: #run this for each word in file
        word_found = False
        if len(histogram): #if histogram has value in it:
            for sublist in histogram: #for each [word: value] list in histogram
                if sublist[0] == word: #if we find that word alredy saved in histogram
                    word_found = True
                    sublist[1] += 1 #add fequency by 1
                    break #break because we already found the word, no need to go to rest of the lists for efficiency
            if not word_found: #if word is not found in list
                histogram.append([word, 1]) #add the word with frequency of 1
        else: # if we have not added anything to histogram
            histogram.append([word, 1]) # just add the first word to historgram
    return histogram

def unique_words(histogram):
    print("there are {} unique words.".format(len(histogram)))

def frequency(word, histogram):
    for sublist in histogram: #for each [word: value] list in histogram
        if sublist[0] == word: #if word in the list== word that we take in
            time = sublist[1] #save its value to time (number of times the word appeared)
        else:
            continue
    print("{} appears {} times".format(word, time))

if __name__ == "__main__":
    print(histogram())
    unique_words(histogram())
    frequency("fish", histogram())
