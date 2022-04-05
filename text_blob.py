from textblob import TextBlob 

# analysis = TextBlob("Text looks like it has some interesting features!")

# #print(dir(analysis))
# #To use something from TextBlob, we first want to convert it to a TextBlob object, so we do that with our analysis var. From here, we can do quite a bit. You can read the docs, or just do:

# #we can immediately see quite a few useful ones. We can do things like detect_language, capture noun_pharse, lable parts of speech with tags, we can even translate to other languages,
# #tokenize, and more. 

# print(analysis.translate(to="es"))

# print(analysis.tags)

# #TextBlob is build on NLTK, the pos tags are the same. Hence the definations remain same. 

# print(analysis.sentiment)

#so the sentiment of the above sentence is fairly postive and highly subjective. Now, let's test this on a bit more data using the postive.txt and negative.txt datasets. 

pos_count = 0
pos_correct = 0

with open ("/home/varsha/created/codes/python_code/Untitled-2.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity > 0:
            pos_correct += 1 
        pos_count += 1 

print ("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))

#word embeddings are a type of word representations that allows words with similar meaning to have a similar representation
#they are a distributed representation for text that is prerhaps one of the key breakthroughs for the impressive performance of deep learning 
#methods on challenging natural language processing problems 
#pandas -> library for data analysis and data manipulation 
#matplotlib -> library used for data visualization 
#seaborn -> a library based on matplotlib and it provides a high-level interface for data visulalization 
#wordcloud -> library to visualize text data 
#re -provides functions to pre-process the strings as per the given regular expressions 
#nltk language toolkit is a collection of librariries for natural languag processing 
#stopwords - a collection of words that don't provide any meaning to a sentence 
#wordnetlemmatizer - used to convert different forms of words into a single item but still keeping context intact 
