from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import pickle
import string

training_data = pickle.load(open("training_data.pkl", 'rb'))

classes = []
for data in training_data:
    if data['class'] not in classes:
        classes.append(data['class'])

stemmer = SnowballStemmer('english')
tfidf_vectorizer = TfidfVectorizer(min_df = 1)
tfidf_data = []
for cl in classes:
    sentences = []
    for data in training_data:
        if data['class'] == cl:
            data["sentence"] = data['sentence'].translate(string.maketrans("", ""), string.punctuation)
            words = data['sentence'].split()
            w = []
            for word in words:
                w.append(stemmer.stem(word))
            sentence = ' '.join(w)
            sentences.append(data['sentence'])
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    dictionary = tfidf_vectorizer.vocabulary_
    tfidf_data.append({'class':cl, 'matrix':tfidf_matrix, 'word_dict':dictionary})

def clean_and_tokenize(sentence):
    sentence = sentence.translate(string.maketrans("", ""), string.punctuation)
    words = sentence.split()
    stop_words = stopwords.words('english')
    w = []
    for word in words:
        if word not in stop_words:
            word = stemmer.stem(word)
            w.append(word.lower())
    return w

sentence = raw_input('Enter a sentence: ')
words = clean_and_tokenize(sentence)
final_score = 0
cl = ''
for data in tfidf_data:
    score = 0
    tf_words = data['word_dict'].keys()
    for word in words:
        if word in tf_words:
            score = score + data['word_dict'][word]
    if final_score < score:
        final_score = score
        cl = data['class']

print 'Class: ',cl
print 'Score: ',final_score
