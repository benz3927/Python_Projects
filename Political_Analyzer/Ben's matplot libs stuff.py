### Matplotlib graph pos_tag how manny proper nouns in each speech
### Americans, American, pos, verbs, adj ## nltk.count()
### name drop

# republican vs democrat indicator evidence

import matplotlib.pyplot as plt

### example

def proper_noun(words_list):
    pnoun_list = []
    for word in words_list:
        if word[1] == 'NNP':
            pnoun_list.append(word[0])
    return pnoun_list

proper_noun(words_list)

indicators
parties = list(indicators.keys())
counts = list(indicators.values())

plt.bar(range(len(indicators)), counts, tick_label=parties)
plt.show()


plt.xticks(rotation=90)
plt.bar(parties,counts)
plt.tight_layout()
plt.show()
plt.pie(counts, labels = parties)
plt.show()



#name drop graph by speech
# make counts for each president and put it in a list
# pnoun_counts = c(