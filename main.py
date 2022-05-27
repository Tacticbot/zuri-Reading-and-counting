# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string


def read_file_content(filename):
   file = open(filename,'r')
   while True:
    next_line = file.readlines()

    if not next_line:
        break;
    
    file.close()
    return next_line


def count_words():

    text = read_file_content("story.txt")
    # [assignment] Add your code here
    #new dictionary
    dict_count = dict()
    # loop through each line
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()
        # convert to lower case
        line = line.lower()
        # removing punctuations
        line = line.translate(line.maketrans("", "", string.punctuation))
        # splitting each line to words
        words = line.split(" ")
        # looping each word
        for word in words:
            # if word in dictionary add count
            if word in dict_count:
                dict_count[word] = dict_count[word] + 1
            # if not add count by 1
            else:
                dict_count[word] = 1
    return dict_count

print(count_words())


