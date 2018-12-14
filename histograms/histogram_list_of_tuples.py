def histogram():
    histogram = []
    words = []
    with open("/Users/ruhsane/dev/courses/cs1.2/tweet-generator/histograms/source.txt") as f:
        for line in f:
            for word in line.split():
                words.append(word)

    for word in words: #for each word in file
        word_found = False
        if len(histogram):
        # if histogram is NOT emoty
            for i in range(len(histogram)):
                current_tup = histogram[i] #save the current tuple
                if current_tup[0] == word:
                    # found the word:
                    word_found = True
                    freq_count = current_tup[1] #save the previous count
                    histogram[i] = (word, freq_count + 1) #replace the whole tuple with (word, adding 1 to previous count)
                    break #break because we already found the word, no need to go to rest of the lists for efficienc
            if not word_found:
                # word not found:
                histogram.append((word, 1))
        else:
            # if histogram is empty:
            histogram.append((word, 1))

    return histogram

def unique_words(histogram):
    print("there are {} unique words".format(len(histogram)))

def frequency(word, histogram):
    for i in range(len(histogram)):
        current_tup = histogram[i]
        if current_tup[0] == word:
            print("{} appears {} times.".format(word, current_tup[1]))

if __name__ == "__main__":
    print(histogram())
    unique_words(histogram())
    frequency("fish", histogram())
