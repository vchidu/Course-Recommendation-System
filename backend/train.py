import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from nltk.util import ngrams
from nltk.corpus import stopwords
import spacy
import nltk
import re
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from recommend import get_recommendations_1
from metrics import *
import pickle

data = pd.read_csv("Coursera.csv")

# Selecting features

col = ['Course Name','Difficulty Level','Course Description','Skills','Course Rating','Course URL','University']
df = data[col]
df = df.drop_duplicates()

df = df[df['Course Rating'] != 'Not Calibrated']
df['Course Rating'] = df['Course Rating'].astype(float)

# Pre-processing features

df['Course Name']=df['Course Name'].apply(lambda x:x.replace(':',' '))
df['Course Name']=df['Course Name'].apply(lambda x:x.replace(',',' '))
df['Course Name']=df['Course Name'].apply(lambda x:x.replace('-',' '))

df['Course Description']=df['Course Description'].apply(lambda x:x.replace('-',' '))
df['Course Description']=df['Course Description'].apply(lambda x:x.replace('.',' '))
df['Course Description']=df['Course Description'].apply(lambda x:x.replace(':',' '))
df['Course Description']=df['Course Description'].apply(lambda x:x.replace(',',' '))

df['Skills']=df['Skills'].apply(lambda x:x.replace('-',' '))
df['Skills']=df['Skills'].apply(lambda x:x.replace('.',' '))
df['Skills']=df['Skills'].apply(lambda x:x.replace(':',' '))
df['Skills']=df['Skills'].apply(lambda x:x.replace(',',' '))
df['Skills']=df['Skills'].apply(lambda x:x.replace('(',' '))
df['Skills']=df['Skills'].apply(lambda x:x.replace(')',' '))

# Create target labels

outputs = []
for i in df['Skills']:
  tokens = [token for token in i.split(" ") if token != ""]
  
  outputs.append(list(ngrams(tokens, 2)))

lab = ['data science','arts humanities','business','computer science','health','information technology','language learning','math logic','personal development','physical science engineering','social sciences']
lab1=['data','arts','humanities','business','computer','health','information','technology','language','math','logic','personal','development','physical','engineering','social']

targ = []
f=0
c=0
for j in outputs:
  f=0
  for i in j:
    #print(i[0],i[1])
    if i[0].lower() +' '+i[1].lower() in lab:
      targ.append(i[0].lower() +' '+i[1].lower())
      f=1
      break
    elif i[0].lower() in lab1:
      targ.append(i[0].lower())
      f=1
      break
    elif i[1].lower() in lab1:
      targ.append(i[1].lower())
      f=1
      break
    
  if f==0:
    targ.append('default')

targ1= []
dic = {'default':'default','arts':'arts humanitites','computer':'computer science','data':'data science','development':'personal development','personal':'personal development','engineering':'physical science engineering','information':'information technology','technology':'information technology','language':'language learning','physical':'physical science engineering','social':'social sciences','math':'math logic','logic':'math logic'}
for i in targ:
  if i in lab:
    targ1.append(i)
  else:
    targ1.append(dic[i])

df['Target label'] = targ1
#To-do: Need to choose ideal cluster number still
#df['Target cluster'] = clusters

# Create final col for feeding data to encoding model

df['Final Col']=df['Course Name']+' '+df['Course Description']+' '+df['Skills']

df = df.drop_duplicates(subset=['Course Name'])

indices = pd.Series(df.index, index=df['Course Name']).drop_duplicates()

nlp=spacy.load("en_core_web_sm")

#### Removal of \characters #####

df['processed']=df['Final Col'].apply(lambda x: re.sub(r'[^\w+ ]',' ',x.lower()))
#df['processed'] = df['processed'].apply(lambda x: re.sub(r'[0-9]','',x))
df['processed'] = df['processed'].apply(lambda x: re.sub(r'[/(){}\[\]\|@,;]',' ',x))

#Remove stop word
df['processed'] = df['processed'].apply(lambda x: ' '.join([word for word in x.split() if nlp.vocab[word].is_stop==False ]))

######## Counting number of words ############

df['words'] = df['processed'].apply(lambda x: len(str(x).split(' ')))

# Save the processed dataframe
df.to_csv('Processed_Dataframe.csv')

# Use pre-trained bert model for creating an encoding matrix

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

#Sentences we want to encode. Example:
sentence = list(df['processed'])


#Sentences are encoded by calling model.encode()
embedding = model.encode(sentence)

# Create similarity matrix

similarity_1 = cosine_similarity(embedding)

# Save the similairty matrix
with open('cosine_sim.pkl', 'wb') as file:
      
    # A new file will be created
    pickle.dump(similarity_1, file)

# Get predicted array for evaluating the model
c=0
pred_array = []
for i in df['Course Name']:
  #if i!='Introduction to Cybersecurity Tools & Cyber Attacks':
    #print(i)
  name, pred_lab_id = get_recommendations_1(i,similarity_1,indices,df,5)
  if df['Target label'].iloc[c] == 'default':
    pred_array.append([1,1,1,1,1])
  else:
    pred_array.append([1 if j ==df['Target label'].iloc[c] else 0 for j in df['Target label'].iloc[pred_lab_id]])
  
  c+=1
  if c==500:
    break

#Evaluate the model 

# MAP@5
print(mean_average_precision(pred_array))

#NDCG@5
s=0
for i in pred_array:
  s+=ndcg_at_k(i,5)
print(s/len(pred_array))