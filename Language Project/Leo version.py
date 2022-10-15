from matplotlib import *
import nltk, unidecode
from random import *


republican_indicators = ["Democrats", "Democrat", "Joe", "Biden", "Obama", "Barack", "Sleepy"]
democrat_indicators = ["Republican", "Republicans", "Trump", "Donald", "Mitt", "Romney"]

# conver lowercase somehow? also keep version which has the uppercase, also trump likes words such as "great"

speeches = ["Obama2004.txt","Biden.txt","Trump.txt","Romney.txt"]
#list of speech document names

### 

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

### 
        
def compare(indicators):
    is_republican = False
    
    if indicators["republican"] > indicators["democrat"]:
        is_republican = True
    return is_republican

def read_words_from_file(filename):
    # Opens the given file using the UTF-8 encoding
    with open(filename, encoding = "ISO-8859-1") as file:
        #utf-8 did not work, had to look online for the right encoding format
        
        # Reads the file into a string
        text_utf8 = file.read()
        
        # Replaces all special characters (like É and slanted quotes) with
        # standard (ASCII) equivalents, which will make them easier for NLTK
        # to handle.
        text = unidecode.unidecode(text_utf8)
    words = nltk.word_tokenize(text)
    return words



# randomly select 1 of 4 speechesprint(words)


def main():
    print('Welcome to the Political Speech Analyzer! We will feed in a random speech from Trump, Obama, Romney, or Biden and our machine will let you know if the politican who gave this speech is a Democrat or Republican!')
    
    speech = speeches[randint(0, 3)]
    
    print("The computer has selected", speech, ".")
    
    words = read_words_from_file(speech)
    words_list = nltk.pos_tag(words)
    indicators = get_indicators(words)
    
    print(indicators)
    
    
    is_republican = compare(indicators)
    
    if is_republican == False:
        print('The person who gave this speech is a Democrat!')
    else:
        print('The person who gave this speech is a Republican!')
    
main()

# print something out as introduction and when giving final results



### matplotlib make charts for evidence for Rebpulican or Democrat

### find "repbulicans" for democrats key words

# focus on 3 main functions/programs
# one function finds democrats or republicans,
# key words "great" trump indicator
## republcians will say democrats more than republicans
# great, 

#biden, Obama, Trump, Romney
