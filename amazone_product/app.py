# importing imp lib
import pandas as pd
import numpy as np
import nltk 
import streamlit as st
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
from PIL import Image


# loading data and removing not req col
df = pd.read_csv('amazon_product.csv')
df = df.drop('id', axis=1)

# tokenization and stemming
sbs = SnowballStemmer('english')
def tokenization(txt):
  tokens = nltk.word_tokenize(txt.lower())
  txt = [sbs.stem(token) for token in tokens]
  return " ".join(txt)

df['Stemmed_row'] = df.apply(lambda row: tokenization(row['Title'] + ' ' + row['Description']), axis=1)

# cosine similarity and search function
tfifd = TfidfVectorizer(tokenizer = tokenization)
def consine_similarity(vector1, vector2):
  matrix = tfifd.fit_transform([vector1, vector2])
  return cosine_similarity(matrix)[0][1]

def search_product(search):
  stemmed_search = tokenization(search)
  df['Similarity'] = df['Stemmed_row'].apply(lambda x: consine_similarity(stemmed_search, x))
  return df.sort_values(by='Similarity', ascending=False).head(10)[['Title','Description','Category']]

# web app
st.set_page_config(page_title = "Amazon Search Engine")
img = Image.open('img.jpeg')
st.image(img,width = 600)
st.title('Search Engine and Product Recommendation System on Amazon Data')
search = st.text_input('Enter Product Name')
sumbitbtn = st.button('Search')
if sumbitbtn:
    res = search_product(search)
    st.write(res)
