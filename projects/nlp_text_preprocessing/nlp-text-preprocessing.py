#!/usr/bin/env python
# coding: utf-8

# # NLP Text Preprocessing (Udemy AI Engineer Course)
# This notebook demonstrates Data Clean up Steps and TEXT PREPROCESSING:
# - Lowercasing
# - Removing stopwords
# - Regex preprocessing
# - Tokenization
# - Lemmatization / stemming
# - N-grams
# Part of the AI & Robotics portfolio.
# 

# 1) **Using .lower() function to turn sentences to lower case** 
# Lower method is beneficial in npl because it simplifies the workflow and maintains consistency
# one benefit of lowercasing words like “Apple” and “apple” is that It allows the model to treat them as the same token, simplifying analysis

# In[ ]:


sentence = "Her cat's name is Luna"


# In[ ]:


lower_sentence = sentence.lower()


# In[ ]:


print(lower_sentence )


# In[ ]:


sentence_list = ["Could you pass me the TV remote?", "It is impossible to find this hotel", "Want to go for dinner on Tuesday"]


# In[ ]:


lower_sentence_list = [x.lower() for x in sentence_list]
lower_sentence_list


# 2) **Stop Words removal**
# we remove stop words e.g. and , of , a and to since they dont have much meaning and simplify the text for smaller and cleaner dataset easier to process
# for this purpose we use NLTK library, comes with predefined list of stopwords, tools for tokenizng text and datasets for experiments
# 

# In[ ]:


import nltk
nltk.download('stopwords')           # run once (or guard it)
from nltk.corpus import stopwords


# In[ ]:


en_stopwords = stopwords.words('english')
print(en_stopwords)


# In[ ]:


sentence = "it was too far to go to the shop and he did not want her to walk"


# In[ ]:


sentence_no_stopwords = ' '. join([word for word in sentence.split() if word not in en_stopwords])


# In[ ]:


print(sentence_no_stopwords)


# In[ ]:


en_stopwords.remove("did")
en_stopwords.remove("not")


# In[ ]:


en_stopwords.append("go")


# In[ ]:


sentence_no_stopwords_custom =' '.join([word for word in sentence.split() if word not in en_stopwords])


# In[ ]:


print(sentence_no_stopwords_custom)


# 3) **Regular Expressions** 
# Regular Expressions (regex): a special way of writing patterns to search through text 
# e.g. any thre numbers in a row. it can be used to find text, filter or check text

# In[ ]:


#Raw Strings e.g. we do \n which means new line but what if we want it to be \n in that case we use raw string as r"\n" 
import re


# In[ ]:


#my_folder = "C:\desktop\notes" if we do this we loose n after desktop and "otes" also shifted to next line
#instead we use raw string 
my_folder = r"C:\desktop\notes"
print(my_folder)


# In[ ]:


#regex search function
result_search  =  re.search("pattern", r"string to contain the pattern") #if matches returns matched object, else returns None
result_search


# In[ ]:


result_search_2 =  re.search("pattern", r"the phrase to find isn't in the string")
print(result_search_2)


# In[ ]:


#re.sub searches for a specific text withing a string and replaces it with new content, required 3 arguments
#re.sub("old text", "new text",  "the string"), 
string = r"sara was able to help me find the new items i needed quickly"
new_string =  re.sub("sara", "sarah", string)
new_string   


# In[ ]:


# import re


# In[ ]:


#here if we do "sarah?" it means "h" is optonal
customer_reviews = ["sam was a great help to me in the store", "the cashier was very rude to me, I think her name was elanor",
                    "amazing work from sadeen!", "sarah was able to help me find the items i needed quickly", "lucy is such a great addition to the team",
                    "great service from sara she found me what i wanted" ]


# In[ ]:


sarahs_reviews = []


# In[ ]:


pattern_to_find = r"sarah?"


# In[ ]:


for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        sarahs_reviews.append(string)


# In[ ]:


print(sarahs_reviews)


# In[ ]:


# ^pattern matches any string that begins with that pattern e.g. r"^a" matches any string that beings with 'a'
a_reviews = []
pattern_to_find = r"^a"
for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        a_reviews.append(string)
print(a_reviews)


# In[ ]:


# $pattern matches any string that ends with that pattern e.g. r"y$" matches any string that ends with 'y'
y_reviews = []
pattern_to_find = r"y$"
for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        y_reviews.append(string)
print(y_reviews)


# In[ ]:


# | pipe symbol works like an "or" , e.g. checking multiple patterns, here parenthesis are neccassary as they group the words together
needwant_reviews = []
pattern_to_find = r"(need|want)ed"
for string in customer_reviews:
    if (re.search(pattern_to_find, string)):
        needwant_reviews.append(string)
print(needwant_reviews)


# In[ ]:


# removing punctations from text using regex, crucial in NLP , bcoz punctuation(:,?";) gets in the way when we want to analyze words
no_punct_reviews = []
pattern_to_find = r"[^\w\s]"   #here square brackets define set of characters we want to match  #inside square brackets ^ means not/negate
# \w stands for word characters 
 #\s stands for white spaces, 
#in other words pattern means find anything that is not 
                                # a word character and not a space


# In[ ]:


for string in customer_reviews:
    no_punct_string = re.sub(pattern_to_find, "", string)  #re.sub(old text, new text, string)
    no_punct_reviews.append(no_punct_string)
print(no_punct_reviews)


# 4) **Tokenization**
# # Critical Step in text preprocessing, which is breaking text into smaller units
# # common type is word tokenization where is word in a sentence becomes a token
# # depending upon use cases they can be words, sentences, subwords or characters
# # smaller text makes it easier to analyze and understand in other words easier for analysis
# # for example looking at individual words can reveal patterns e.g. which word is most common, how often specific words appear together
# # we use nltk package here and download punkt_tab a table to figure out where sentences beging and end 

# In[ ]:


import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize


# In[ ]:


sentences = "Her cat's name is Luna. Her dog's name is Max"


# In[ ]:


#doing sentence tokenization here 
sent_tokenize(sentences) #splits into individual sentences


# In[ ]:


#doing word tokenization here
sentence = "Her cat's name is Luna."  
word_tokenize(sentence)  #breaks into individual tokens, each word becomes its own token


# In[ ]:


#doing word tokenization on longer text
sentence = "Her cat's name is Luna and her dog's name is Max"
word_tokenize(sentence)  #breaks into individual tokens, each word becomes its own token
#if we had turned to lower case/preprocessed before tokenization, the tokens would not have treated word "her" as seperate tokens
#by lowering case we could have ensured consistency 


# 5) **Stemming**
# # Standardization of text, means makng the text more uniform so that different forms of the same words do not confuse the analysis
# # common way of standardization is stemming,where words are reduced to base form e.g connecting or connected will be reduced to base form connnect
# # stemming works by chopping off endings or suffixes
# # downsize is result isn't a proper word or doesn't look meaningfull e.g. studies might be stemmed to something like stud
# # we standardize because it reduces the number of unique words 
# # reduces noise in the data set making data cleaner and simpler an essential step in Machine Learning
# # we use PorterStemmer from the nltk.stem module which reduces english words to simpler bases

# In[ ]:


from nltk.stem import PorterStemmer


# In[ ]:


ps = PorterStemmer() #we create a PorterStemmer Object


# In[ ]:


#example 1
connect_tokens = ['connecting', 'connected', 'connectivity','connect', 'connects']


# In[ ]:


for t in connect_tokens:
    print(t, ": " , ps.stem(t))   #using .stem() method to stem tokens


# In[ ]:


#example 2
learn_tokens = ['learned', 'learning', 'learn' , 'learner', 'learners']


# In[ ]:


for t in learn_tokens:
    print(t, ": " , ps.stem(t)) 


# In[ ]:


#example 3
like_tokens = ['likes', 'better', 'worse']


# In[ ]:


for t in like_tokens:
    print(t, ": " , ps.stem(t)) 


# 6) **lemmatization**
# # lemmatization reduces a word to a meaning base form while preserving its intended meaning
# # More sophiscated as it references a predefined dictionary to find correct base, it uses that predefined dictionary to keep the context of the word
# # We usually end up with real, meaningfull words
# # Trade off is that we may still have more unique words compared to stemming
# # we are going to use NLTK library and we are going to download wordnet as its an extensive database of English, A dictionary Lemmatizer uses to make    sure the base forms it produces are real words
# # then we import the lemmatizer

# In[ ]:


nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer


# In[ ]:


lemmatizer = WordNetLemmatizer() #(lemmatizer Object)


# In[ ]:


for t in connect_tokens:
    print(t, ':', lemmatizer.lemmatize(t))


# In[ ]:


for t in learn_tokens:
    print(t, ':', lemmatizer.lemmatize(t))


# In[ ]:


for t in like_tokens:
    print(t, ':', lemmatizer.lemmatize(t))


# 7) **N-grams**
# #  Help us analyze the relationship between neighboring words
# #  N-grams basically means a seqeunce of N tokens, value of N tells us how many words are grouped 
# #  when n equals one, we have single words called unigrams N = 1: unigrams e.g. 'I', 'love', 'nlp', examining unigrams helps us understand the basic      building blocks of our text , often the first step in exploring data
# #  when n equals two, we have pairs of consecuting words called bigrams N = 2: bigrams e.g.  'I love' 'love nlp' 
# #  when n equals three, we have sequences of words called trigrams N = 3: trigrams e.g. 'I love nlp' 
# #  IF N > 3 , We use the word N-grams to describe them
# #  we are going to use nltk, pandas and matplotlib    
# #  pandas is the python library for working with structured data fast and intuitive
# #  core feature in pandas is the data frame which works like a spreadsheet, data frame stores data in rows and columns , making it easier to sort,        filter and group, Perfect for preparing text for analysis, keeping it organized and connecting with other steps in ML workflows
# #  matplotlib is the python library for creating charts and visualizations
# #  it can take results of our text analysis and turn them into graphs, easier to spot trends and patterns in data

# In[ ]:


import nltk
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


tokens = [
    'the', 'rise', 'of', 'artificial', 'intelligence', 'has', 'led', 'to',
    'significant', 'advancements', 'in', 'natural', 'language', 'processing',
    'computer', 'vision', 'and', 'other', 'fields', 'machine', 'learning',
    'algorithms', 'are', 'becoming', 'more', 'sophisticated', 'enabling',
    'computers', 'to', 'perform', 'complex', 'tasks', 'that', 'were', 'once',
    'thought', 'to', 'be', 'the', 'exclusive', 'domain', 'of', 'humans',
    'with', 'the', 'advent', 'of', 'deep', 'learning', 'neural', 'networks',
    'have', 'become', 'even', 'more', 'powerful', 'capable', 'of',
    'processing', 'vast', 'amounts', 'of', 'data', 'and', 'learning', 'from',
    'it', 'in', 'ways', 'that', 'were', 'not', 'possible', 'before', 'as',
    'a', 'result', 'ai', 'is', 'increasingly', 'being', 'used', 'in', 'a',
    'wide', 'range', 'of', 'industries', 'from', 'healthcare', 'to',
    'finance', 'to', 'transportation', 'and', 'its', 'impact', 'is', 'only',
    'set', 'to', 'grow', 'in', 'the', 'years', 'to', 'come'
]
print(tokens)


# In[ ]:


unigrams =  (pd.Series(nltk.ngrams(tokens, 1)).value_counts())   #pd.Series is a single column od data in a spreadsheet
print('All Unigrams','\n' , unigrams  )
print('Top 10 Unigrams','\n', unigrams[:10])


# In[ ]:


#taking top 10 unigrams , sorting them so they are in order then .plot.barh with an h in the end which creates a horizontal bar chat, followed 
#by customization e.g. color="lightsalmon"  width adjustment e.g.  width = 0.9 and define figure size e.g. figsize = (12,8)
unigrams[:10].sort_values().plot.barh(color="lightsalmon", width = 0.9, figsize=(12,8))
#finally we add tile
plt.title("10 Most frequently Occuring Unigrams")


# In[ ]:


bigrams =  (pd.Series(nltk.ngrams(tokens, 2)).value_counts())   #pd.Series is a single column od data in a spreadsheet
print('All Bigrams','\n' , bigrams  )
print('Top 10 Bigrams','\n', bigrams[:10])


# In[ ]:


trigrams =  (pd.Series(nltk.ngrams(tokens, 3)).value_counts())   #pd.Series is a single column od data in a spreadsheet
print('All trigrams','\n' , trigrams  )
print('Top 10 trigrams','\n', trigrams[:10])


# In[ ]:




