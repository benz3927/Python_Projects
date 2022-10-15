def read_words_from_file(filename):
    # Opens the given file using the UTF-8 encoding
    with open(filename, encoding = "utf-8") as file:
        
        # Reads the file into a string
        text_utf8 = file.read()
        
        # Replaces all special characters (like É and slanted quotes) with
        # standard (ASCII) equivalents, which will make them easier for NLTK
        # to handle.
        text = unidecode.unidecode(text_utf8)
        
    # What does this do?
    words = nltk.word_tokenize(text)
    
words = nltk.tokenize.word_tokenize(text)
allWordDist = nltk.FreqDist(w.lower() for w in allWords)

stopwords = nltk.corpus.stopwords.words('english')
allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)

## find pattern for obama