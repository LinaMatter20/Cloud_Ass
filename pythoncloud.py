
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

with open(r'cloud\random_paragraphs.txt.txt','r') as file:
    content = file.read()

    # Tokenize the text
    tokens = word_tokenize(content)

    # Remove punctuation and convert to lower case
    tokens = [word.lower() for word in tokens if word.isalpha()]

    # Get English stop words
    stop_words = set(stopwords.words('english'))

    # Remove stop words
    filtered_tokens = [word for word in tokens if not word in stop_words]

    # Count the frequency of each word
    word_freq = Counter(filtered_tokens)

    # Display the word frequency count
    for word, count in word_freq.items():
        print(word, ':', count)
