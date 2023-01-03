from matplotlib import pyplot as plt
import nltk, unidecode
from random import *



# Republicans like to talk about Democrats in their speeches and Democrats like to talk about Republicans in their speeches
# Below, we compiled a list of popular words used by Demograts and Republicans at within their political campaigns
# that made sense in context
# https://www.washingtonpost.com/politics/2020/08/28/words-used-dnc-rnc/
# popular words used by democrats and republicans

#Republican popular words

republican_indicators = ["Democrats", "Democrat", "Joe", "Biden", "Obama", "Barack",
                         "Sleepy", "Abortion","Destroy","Violence","Virus","Socialism",
                         "China","church","prosperity","American","Americans", "great"]

# Democrat popular words
democrat_indicators = ["Republican", "Republicans", "Trump", "Donald", "Mitt", "Romney",
                       "democracy","care","man","life","world"]


#list of speech document names
speeches = ["Obama2004.txt","Biden.txt","Trump.txt","Romney.txt"]


# this function is a dictionary that counts the evidence for whether the politician's speech
# leans more towards Republican or Democrat
# get_indicators gets the counts of number of indicators for Democrat or Republican words, and stores the numerical data
# in a counter using the dictionary indicators the key is the political party "democrat" or "republican" while the value 
# is the number or count of evidence for that party

def get_indicators(text):
    indicators = {}
    indicators["republican"] = 0
    indicators["democrat"] = 0
    for word in text:
        if word in republican_indicators:
            indicators["republican"] += 1
        elif word in democrat_indicators:
            indicators["democrat"] += 1
        else:
            continue
    return indicators


### the compare function functions checks if there are more republican indicators than democrats and stores
# it in a boolean is_republican which we use in later parts of the project
        
def compare(indicators):
    is_republican = False
    
    if indicators["republican"] > indicators["democrat"]:
        is_republican = True
    return is_republican

def read_words_from_file(filename):
    # Opens the given file using the UTF-8 encoding
    with open(filename, encoding = "ISO-8859-1") as file:
        #utf-8 did not work, had to look online for an encoding format: "ISO-8859-1"
        
        # Reads the file into a string
        text_utf8 = file.read()
        
        # Replaces all special characters (like É and slanted quotes) with
        # standard (ASCII) equivalents, which will make them easier for NLTK
        # to handle.
        text = unidecode.unidecode(text_utf8)
    # tokenize function which turns words read in, into a list of strings
    words = nltk.word_tokenize(text)
    return words


def namelocation_drop_counter():
    ## find name_drop data
    
    # find proper nouns from words_list from nltk pos_tag function, name/location drop function, which politician
    # name/location drops the most
    
    # load all txt files of speeches
    
    obama_words = read_words_from_file('Obama2004.txt')
    Obama = nltk.pos_tag(obama_words)
    
    trump_words = read_words_from_file('Trump.txt')
    Trump = nltk.pos_tag(trump_words)
    
    romney_words = read_words_from_file('Romney.txt')
    Romney = nltk.pos_tag(romney_words)
    
    biden_words = read_words_from_file('Biden.txt')
    Biden = nltk.pos_tag(biden_words)
    
    # function which finds proper nouns and puts them in a list 
    def proper_noun(words_list):
        propnoun_list = []
        for word in words_list:
    # go through the list and search for NNP, proper nouns.
    # if the proper noun tag is found, add the word to the list of proper nouns
            if word[1] == 'NNP':
                propnoun_list.append(word[0])
        return propnoun_list

    obama_counts = len(proper_noun(Obama))
    trump_counts = len(proper_noun(Trump))
    romney_counts = len(proper_noun(Romney))
    biden_counts = len(proper_noun(Biden))
    
    candidates = ['Obama','Trump','Romney','Biden']
    prop_noun_counts = [obama_counts,trump_counts,romney_counts, biden_counts]
    
    # graph the data using matplot lib to see who name/location drops the most
    plt.bar(range(len(candidates)), prop_noun_counts, tick_label = candidates)
    plt.suptitle('Name & Location Dropper Distribution (Who Says The Most Proper Nouns)')
    plt.title('by Ben Zhao and Leo Li')
    plt.show()




def main():
    print('Welcome to the Political Speech Analyzer! We will feed in a random speech from Trump, Obama, Romney, or Biden and our machine will let you know if the politican who gave this speech is a Democrat or Republican!')
    # randomly select 1 of 4 speeches
    speech = speeches[randint(0, 3)]
    
    print("We have selected",speech)
    
    # make list, words and words_list for further analysis
    
    words = read_words_from_file(speech)
    words_list = nltk.pos_tag(words)
    
    # print the first 100 or so words of the speech
    print(f'Here is a brief glimpse of the beginning of the chosen speech: {words[:100]}')
    
    # use the get_indicators function on our speech words to count evidence
    indicators = get_indicators(words)
    
    print(indicators)
    
    # boolean, conditional for if is_republican == False (if the person is not Republican, then the person is a democrat)
    # Else, if is_republican == True, if the person is a Republican, then the person is a Republican
    is_republican = compare(indicators)
    if is_republican == False:
        print('The person who gave this speech is a Democrat!')
    else:
        print('The person who gave this speech is a Republican!')
    
    # Bar plots, turn indicators dictionary keys into a list and scores into a list for graphing
    parties = list(indicators.keys())
    counts = list(indicators.values())
    
    # Matplotlib bar plot for 'Evidence for Democrat or Republican Candidate by Leo and Ben'

    plt.bar(range(len(indicators)), counts, tick_label=parties)
    plt.title('Evidence for Democrat or Republican Candidate by Leo and Ben')
    plt.show()
    
    # Matplotlib pie chart for counts, red for Republican, blue for Democrats
    plt.pie(counts,colors = ['red','blue'], labels = parties)
    plt.title('Evidence for Democrat or Republican Candidate by Leo and Ben')
    plt.show()
    
    # use the name/location drop function to count who used the most proper nouns in their speeches, function defined earlier
    namelocation_drop_counter()
    
    
main()



# Have fun!

### Ideas for the project in the beginning

### matplotlib make charts for evidence for Rebpulican or Democrat

### find "republicans" for democrats key words: the initial idea

# focus on 3 main functions/programs
# one function finds democrats or republicans,
# key words "great" trump indicator
## republcians will say democrats more than republicans