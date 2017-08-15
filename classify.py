from nltk.stem.snowball import SnowballStemmer
import string
import pickle

training_data = pickle.load(open("training_data.pkl", 'rb'))
stemmed_words = {}
word_classes = {}
stemmer = SnowballStemmer("english")
#print training_data
for c in training_data:
    word_classes[c['class']] = []

for data in training_data:
    data["sentence"] = data['sentence'].translate(string.maketrans("", ""), string.punctuation)
    words = data['sentence'].split(" ")
    for word in words:
        stemmed_word = stemmer.stem(word)
        if stemmed_word not in stemmed_words:
            stemmed_words[stemmed_word] = 1
        else:
            stemmed_words[stemmed_word] += 1
        word_classes[data['class']].extend([stemmed_word])

print stemmed_words
print word_classes

def classify(sentence, class_name, show_details = True):
    words = sentence.translate(string.maketrans("", ""), string.punctuation).split(" ")
    ctr = 0
    for word in words:
        if stemmer.stem(word.lower()) in word_classes[class_name]:
            ctr += (1/float(stemmed_words[stemmer.stem(word.lower())]))
            if show_details:
                print '\tword: ', word

    return ctr

sentence = raw_input("Write a sentence: ")
#sentence = "How are you?"
max = 0
name ="None"
for c in word_classes.keys():
    v = classify(sentence, c, show_details = False)
    if v > max:
        max = v
        name = c

print "Class: ", name
print "Score: ", max
