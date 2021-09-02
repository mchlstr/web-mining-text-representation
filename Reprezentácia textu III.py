#!/usr/bin/env python
# coding: utf-8

# #### Zadanie:
# Pokračujte s textami z predchádzajúceho cvičenia (Texty z webu.zip). Spracujte nasledujúce zadanie s pomocou knižnice nltk v Pythone:
# 
# Rozdeľte texty na vety a identifikujte v nich slová, pre ktoré si budete pamätať, ku ktorej vete patria.
# Odstráňte z matice tzv. stop slová a priraďte slovám poradie v danej vete.
# Pomocou morfologickej anotácie otagujte jednotlivé slová.
# Vytvorte dátový súbor, ktorý bude obsahovať všetky dané slová z identifikátorom vety, daným slovom, jeho slovným základom (lema), tagom a poradím vo vete.
# Odovzdajte výsledný súbor a zdrojový kód v jednom zip súbore.
# Importy v Pythone vhodné pre riešenie tohto zadania:
# 
# `import nltk
# from nltk.corpus import stopwords 
# from nltk.tokenize import word_tokenize, sent_tokenize 
# from nltk.stem import WordNetLemmatizer` 
# 
# `nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('wordnet')`
# 
# `stop_words = set(stopwords.words('english')) `
# 
# `tagged = nltk.pos_tag(wordsList)` 

# In[1]:


import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.stem import WordNetLemmatizer 
import re
import pandas as pd
stop_words = set(stopwords.words('english'))
lemmmatizer=WordNetLemmatizer()


# In[2]:


# this time we care about case, so we will not transform to lower
text1 = open('text1.txt','r').read()
text2 = open('text2.txt', 'r').read()
text3 = open('text3.txt', 'r').read()
text4 = open('text4.txt', 'r').read()
text5 = open('text5.txt', 'r').read()


# In[3]:


# for this excercise we can create 2 aproaches
# first all texts will be combined to one
# each text will be processed individually 
# and afterwards they will be in separate sheets

# first we will combine all texts together
text = text1 + text2 + text3 + text4 + text5


# In[4]:


# replace newline character for dot. Oterwise sent tokenizer will not
# recognize the title in the text and will make it as a part of first sentese
# not sure if correct solution but works
text = text.replace("\n",". ")
# If there were more newline characters, just leave one dot instead of 2
text = text.replace("..",".")


# In[5]:


# tokenize the text to the sentenses
sentences = nltk.sent_tokenize(text)


# In[6]:


# creating a list of lists where we will tokenize the words from the sentenses we created first
tokenized_text = [word_tokenize (sent)  for  sent  in  sentences]


# In[7]:


# create empty global lists
# those lists will be used as data source for the fataframe
sentense_id = []
word_id = []
words = []
lemmas = []
pos = []

for i in range(len(tokenized_text)):
    part_of_speech = nltk.pos_tag(tokenized_text[i])
    for x in part_of_speech:
        pos.append(x[1])
    for j in range(len(tokenized_text[i])):
        lematized_word = lemmmatizer.lemmatize(tokenized_text[i][j].lower())
        sentense_id.append(i+1)
        word_id.append(j+1)
        words.append(tokenized_text[i][j])
        lemmas.append(lematized_word)  


# In[8]:


# create a dataset for with the data we created for out combined text

data_from_combined_texts = {
    'Poradie vety': sentense_id,
    'Poradie slova vo vete': word_id,
    'Slovo / token': words,
    'Lema': lemmas,
    'POS': pos
}

combined_dataset= pd.DataFrame(data_from_combined_texts)


# In[9]:


combined_dataset


# In[10]:


# now we will do all steps for the 5 texts
# for text 1
text1 = text1.replace("\n",". ")
text1 = text1.replace("..",".")
# tokenize the text to the sentenses
sentences1 = nltk.sent_tokenize(text1)
# creating a list of lists where we will tokenize the words from the sentenses we created first
tokenized_text1 = [word_tokenize(sent)  for  sent  in  sentences1]

# we already have created the lists so we can reuse them for separate texts.
sentense_id.clear()
word_id.clear()
words.clear()
lemmas.clear()
pos.clear()

for i in range(len(tokenized_text)):
    part_of_speech = nltk.pos_tag(tokenized_text[i])
    for x in part_of_speech:
        pos.append(x[1])
    for j in range(len(tokenized_text[i])):
        lematized_word = lemmmatizer.lemmatize(tokenized_text[i][j].lower())
        sentense_id.append(i+1)
        word_id.append(j+1)
        words.append(tokenized_text[i][j])
        lemmas.append(lematized_word)

# create a dataset for with the data we created for text1

data_from_text1 = {
    'Poradie vety': sentense_id,
    'Poradie slova vo vete': word_id,
    'Slovo / token': words,
    'Lema': lemmas,
    'POS': pos
}

dataset1= pd.DataFrame(data_from_text1)


# In[11]:


# now we will do all steps for the 5 texts
# for text 2
text2 = text2.replace("\n",". ")
text2 = text2.replace("..",".")
# tokenize the text to the sentenses
sentences2 = nltk.sent_tokenize(text2)
# creating a list of lists where we will tokenize the words from the sentenses we created first
tokenized_text2 = [word_tokenize(sent)  for  sent  in  sentences2]

# we already have created the lists so we can reuse them for separate texts.
sentense_id.clear()
word_id.clear()
words.clear()
lemmas.clear()
pos.clear()

for i in range(len(tokenized_text)):
    part_of_speech = nltk.pos_tag(tokenized_text[i])
    for x in part_of_speech:
        pos.append(x[1])
    for j in range(len(tokenized_text[i])):
        lematized_word = lemmmatizer.lemmatize(tokenized_text[i][j].lower())
        sentense_id.append(i+1)
        word_id.append(j+1)
        words.append(tokenized_text[i][j])
        lemmas.append(lematized_word)

# create a dataset for with the data we created for text1

data_from_text2 = {
    'Poradie vety': sentense_id,
    'Poradie slova vo vete': word_id,
    'Slovo / token': words,
    'Lema': lemmas,
    'POS': pos
}

dataset2= pd.DataFrame(data_from_text2)


# In[12]:


# now we will do all steps for the 5 texts
# for text 3
text3 = text3.replace("\n",". ")
text3 = text3.replace("..",".")
# tokenize the text to the sentenses
sentences3 = nltk.sent_tokenize(text3)
# creating a list of lists where we will tokenize the words from the sentenses we created first
tokenized_text3 = [word_tokenize(sent)  for  sent  in  sentences3]

# we already have created the lists so we can reuse them for separate texts.
sentense_id.clear()
word_id.clear()
words.clear()
lemmas.clear()
pos.clear()

for i in range(len(tokenized_text)):
    part_of_speech = nltk.pos_tag(tokenized_text[i])
    for x in part_of_speech:
        pos.append(x[1])
    for j in range(len(tokenized_text[i])):
        lematized_word = lemmmatizer.lemmatize(tokenized_text[i][j].lower())
        sentense_id.append(i+1)
        word_id.append(j+1)
        words.append(tokenized_text[i][j])
        lemmas.append(lematized_word)

# create a dataset for with the data we created for text1

data_from_text3 = {
    'Poradie vety': sentense_id,
    'Poradie slova vo vete': word_id,
    'Slovo / token': words,
    'Lema': lemmas,
    'POS': pos
}

dataset3= pd.DataFrame(data_from_text3)


# In[13]:


# now we will do all steps for the 5 texts
# for text 4
text4 = text4.replace("\n",". ")
text4 = text4.replace("..",".")
# tokenize the text to the sentenses
sentences4 = nltk.sent_tokenize(text4)
# creating a list of lists where we will tokenize the words from the sentenses we created first
tokenized_text4 = [word_tokenize(sent)  for  sent  in  sentences4]

# we already have created the lists so we can reuse them for separate texts.
sentense_id.clear()
word_id.clear()
words.clear()
lemmas.clear()
pos.clear()

for i in range(len(tokenized_text)):
    part_of_speech = nltk.pos_tag(tokenized_text[i])
    for x in part_of_speech:
        pos.append(x[1])
    for j in range(len(tokenized_text[i])):
        lematized_word = lemmmatizer.lemmatize(tokenized_text[i][j].lower())
        sentense_id.append(i+1)
        word_id.append(j+1)
        words.append(tokenized_text[i][j])
        lemmas.append(lematized_word)

# create a dataset for with the data we created for text1

data_from_text4 = {
    'Poradie vety': sentense_id,
    'Poradie slova vo vete': word_id,
    'Slovo / token': words,
    'Lema': lemmas,
    'POS': pos
}

dataset4= pd.DataFrame(data_from_text4)


# In[14]:


# now we will do all steps for the 5 texts
# for text 5
text5 = text5.replace("\n",". ")
text5 = text5.replace("..",".")
# tokenize the text to the sentenses
sentences5 = nltk.sent_tokenize(text5)
# creating a list of lists where we will tokenize the words from the sentenses we created first
tokenized_text5 = [word_tokenize(sent)  for  sent  in  sentences5]

# we already have created the lists so we can reuse them for separate texts.
sentense_id.clear()
word_id.clear()
words.clear()
lemmas.clear()
pos.clear()

for i in range(len(tokenized_text)):
    part_of_speech = nltk.pos_tag(tokenized_text[i])
    for x in part_of_speech:
        pos.append(x[1])
    for j in range(len(tokenized_text[i])):
        lematized_word = lemmmatizer.lemmatize(tokenized_text[i][j].lower())
        sentense_id.append(i+1)
        word_id.append(j+1)
        words.append(tokenized_text[i][j])
        lemmas.append(lematized_word)

# create a dataset for with the data we created for text1

data_from_text5 = {
    'Poradie vety': sentense_id,
    'Poradie slova vo vete': word_id,
    'Slovo / token': words,
    'Lema': lemmas,
    'POS': pos
}

dataset5= pd.DataFrame(data_from_text5)


# In[16]:


# writting to excel with multiple sheets
with pd.ExcelWriter('Reprezentacia_textu_III.xlsx') as writer:
    combined_dataset.to_excel(writer, sheet_name='Analyza textov',index=False)
    dataset1.to_excel(writer, sheet_name='Analyza textu 1',index=False)
    dataset2.to_excel(writer, sheet_name='Analyza textu 2',index=False)
    dataset3.to_excel(writer, sheet_name='Analyza textu 3',index=False)
    dataset4.to_excel(writer, sheet_name='Analyza textu 4',index=False)
    dataset5.to_excel(writer, sheet_name='Analyza textu 5',index=False)
    writer.save()


# In[ ]:




