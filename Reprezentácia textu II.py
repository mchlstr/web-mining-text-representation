#!/usr/bin/env python
# coding: utf-8

# #### Zadanie:
# Pomocou knižnice nltk v Pythone extrahujte lemy slov (základy slov) z anglických textov získaných z webu (Texty z webu.zip).
# 
# Následne vytvorte dátovú maticu, ktorá bude obsahovať frekvenciu lém v jednotlivých dokumentoch, z ktorej odvodíte binárnu, logaritmickú a inverznú frekvenciu.
# 
# Odovzdajte výsledný súbor a zdrojový kód v jednom zip súbore.
# 
# Importy v Pythone vhodné pre riešenie tohto zadania: 
# 
# `import nltk
# from nltk.corpus import stopwords 
# from nltk.tokenize import word_tokenize, sent_tokenize 
# from nltk.stem import WordNetLemmatizer 
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('wordnet')
# stop_words = set(stopwords.words('english'))`
# 
# Postup dosiahnutia výsledkov:
# 
# načítajte texty do Pythonu;
# rozdeľte vety na slová pomocou príkazu: wordsList = nltk.word_tokenize(word)
# inicializovať lematizátor: lemmatizer = WordNetLemmatizer();
# získajte základ slova (lemmu) pre dané slová: lemmatizer.lemmatize(word);

# In[1]:


import nltk
import pandas as pd
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.stem import WordNetLemmatizer 

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('wordnet')

stop_words = set(stopwords.words('english')) 


# In[2]:


# open the text files and load the content from them 
text1 = open("text1.txt", "r").read()
text2 = open("text2.txt", "r").read()
text3 = open("text3.txt", "r").read()
text4 = open("text4.txt", "r").read()
text5 = open("text5.txt", "r").read()


# In[5]:


# 1. Since we analyze just the existance of the words, 
#    we need to put them to lower case first
text1 = text1.lower()
text2 = text2.lower()
text3 = text3.lower()
text4 = text4.lower()
text5 = text5.lower()


# In[6]:


# 2. tokenize the text
tokenized_text1=word_tokenize(text1)
tokenized_text2=word_tokenize(text2)
tokenized_text3=word_tokenize(text3)
tokenized_text4=word_tokenize(text4)
tokenized_text5=word_tokenize(text5)


# In[7]:


# 3. get rid of the stop words
no_stopwords_text1 = [w for w in tokenized_text1 if not w in stop_words]
no_stopwords_text2 = [q for q in tokenized_text2 if not q in stop_words]
no_stopwords_text3 = [z for z in tokenized_text3 if not z in stop_words]
no_stopwords_text4 = [a for a in tokenized_text4 if not a in stop_words]
no_stopwords_text5 = [b for b in tokenized_text5 if not b in stop_words]


# In[8]:


# initialize the word lematizer
lemmatizer = WordNetLemmatizer()


# In[9]:


# 4. lematize the text wich does not contain the stop words anymore
lematized_text1=[lemmatizer.lemmatize(w) for w in no_stopwords_text1]
lematized_text2=[lemmatizer.lemmatize(q) for q in no_stopwords_text2]
lematized_text3=[lemmatizer.lemmatize(a) for a in no_stopwords_text3]
lematized_text4=[lemmatizer.lemmatize(z) for z in no_stopwords_text4]
lematized_text5=[lemmatizer.lemmatize(x) for x in no_stopwords_text5]


# In[10]:


# create a list containing all the lematized words
all_words = []
all_words.extend(lematized_text1)
all_words.extend(lematized_text2)
all_words.extend(lematized_text3)
all_words.extend(lematized_text4)
all_words.extend(lematized_text5)


# In[13]:


# since some words are bound to be repeated in multiple texts
# we want to get rid of it, theretore, we create a set of all unique words
all_words = set(all_words)


# In[15]:


# this step is done so the list can be alphabeticaly sorted
# set by default does not allows this possibility
# this step is pure cosmetics
all_words = list(all_words)

all_words.sort()


# In[18]:


# creating the empty lists to store frequency of the occurance of the word
text1_word_freq  = []
text2_word_freq  = []
text3_word_freq  = []
text4_word_freq  = []
text5_word_freq  = []

for word in all_words:
    text1_word_freq.append(lematized_text1.count(word))
    text2_word_freq.append(lematized_text2.count(word))
    text3_word_freq.append(lematized_text3.count(word))
    text4_word_freq.append(lematized_text4.count(word))
    text5_word_freq.append(lematized_text5.count(word))


# In[20]:


# creating the list of thelist to be fed to the dataframe as a input data
# this way each list will be a row in the dataframe
# if we used the dictionary, we would need be creating columns
words_data = [
    text1_word_freq,
    text2_word_freq,
    text3_word_freq,
    text4_word_freq,
    text5_word_freq
]
frekvencia_slov = pd.DataFrame(words_data, columns = all_words, index = ['text1','text2','text3','text4','text5'])


# In[22]:


# importing the math for the logartimic calculations
# we can do two counts at the same time, both binary and logaritmical 
# in one iteration
import math

# creating empty lists to hold valued for the binary values for lemas in text
binary_text1 = []
binary_text2 = []
binary_text3 = []
binary_text4 = []
binary_text5 = []

# creating empty lists to hold valued for the log values for lemas in text
log_text1 = []
log_text2 = []
log_text3 = []
log_text4 = []
log_text5 = []


# for binary if the word occurs in text value is one, if not value is zero
# The logarithm function ensures the "attenuation" 
# of the frequency of occurrence of words, i. scattering stabilization

for freq in text1_word_freq:
    if freq > 0 : 
        binary_text1.append(1)
        log_text1.append(math.log10(freq))
    else :
        binary_text1.append(0)
        log_text1.append(0)
        
for freq in text2_word_freq:
    if freq > 0 : 
        binary_text2.append(1)
        log_text2.append(math.log10(freq))
    else :
        binary_text2.append(0)
        log_text2.append(0)
        
for freq in text3_word_freq:
    if freq > 0  : 
        binary_text3.append(1)
        log_text3.append(math.log10(freq))
    else :
        binary_text3.append(0)
        log_text3.append(0)
        
for freq in text4_word_freq:
    if freq > 0 : 
        binary_text4.append(1)
        log_text4.append(math.log10(freq))
    else :
        binary_text4.append(0)
        log_text4.append(0)
        
for freq in text5_word_freq:
    if freq > 0 : 
        binary_text5.append(1)
        log_text5.append(math.log10(freq))
    else :
        binary_text5.append(0)
        log_text5.append(0)
        
sum_binary = []
for i in range(len(all_words)):
    sum_binary.append(binary_text1[i]+binary_text2[i]+binary_text3[i]+binary_text4[i]+binary_text5[i])


# In[26]:


binary_data = [
    binary_text1,
    binary_text2,
    binary_text3,
    binary_text4,
    binary_text5,
    sum_binary
    ]
binarna_frekvencia = pd.DataFrame(binary_data , columns = all_words, index = ['text1','text2','text3','text4','text5', 'sum'])

log_data =[
        log_text1,
        log_text2,
        log_text3,
        log_text4,
        log_text5,
]

log_frekvencia = pd.DataFrame(log_data, columns = all_words, index = ['text1','text2','text3','text4','text5'])


# In[27]:


# creating empty lists to hold valued for the IDF (inverse document freq)
# values for lemas in text
binary_text1 = []
inverse_text1 = []
inverse_text2 = []
inverse_text3 = []
inverse_text4 = []
inverse_text5 = []

index = 0
for i in text1_word_freq:
    if i > 0 : 
        inverse_text1.append(log_text1[index] * math.log10(5/sum_binary[index]))
    else :        
        inverse_text1.append(0)
    index += 1
    
index = 0
for i in text2_word_freq:
    if i > 0 : 
        inverse_text2.append(log_text2[index] * math.log10(5/sum_binary[index]))
    else :        
        inverse_text2.append(0)
    index +=1
    
index = 0
for i in text3_word_freq:
    if i > 0 : 
        inverse_text3.append(log_text3[index] * math.log10(5/sum_binary[index]))
    else :        
        inverse_text3.append(0)
    index +=1

index = 0
for i in text4_word_freq:
    if i > 0 : 
        inverse_text4.append(log_text4[index] * math.log10(5/sum_binary[index]))
    else :        
        inverse_text4.append(0)
    index += 1

index = 0
for i in text5_word_freq:
    if i > 0 : 
        inverse_text5.append(log_text5[index] * math.log10(5/sum_binary[index]))
    else :        
        inverse_text5.append(0)
    index += 1


# In[28]:


inverse_data =[
        inverse_text1,
        inverse_text2,
        inverse_text3,
        inverse_text4,
        inverse_text5,
]

inverse_frekvencia = pd.DataFrame(inverse_data, columns = all_words, index = ['text1','text2','text3','text4','text5'])


# In[29]:


# writting to excel with multiple sheets
with pd.ExcelWriter('Reprezentacia_textu_II.xlsx') as writer:
    frekvencia_slov.to_excel(writer, sheet_name='frekvencia_slov')
    binarna_frekvencia.to_excel(writer, sheet_name='binarna_frekvencia')
    log_frekvencia.to_excel(writer, sheet_name='logartimicka_frekvencia')
    inverse_frekvencia.to_excel(writer, sheet_name='inversna_frekvencia')

