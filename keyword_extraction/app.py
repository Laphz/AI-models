import streamlit as st
import pickle
import re
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from PIL import Image
import os

# Adjust file paths to reference the directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Update the file paths
with open(os.path.join(BASE_DIR, 'cv.pkl'), 'rb') as f:
    cv = pickle.load(f)

with open(os.path.join(BASE_DIR, 'tfidf.pkl'), 'rb') as f:
    tfidf_transformer = pickle.load(f)

with open(os.path.join(BASE_DIR, 'feature_names.pkl'), 'rb') as f:
    feature_names = pickle.load(f)

img = Image.open(os.path.join(BASE_DIR, 'img.jpeg'))

# Your remaining code...
nltk.download('stopwords')
nltk.download('wordnet')


# Cleaning data:
stop_words = set(stopwords.words('english'))
new_stop_words = ["fig","figure","image","sample","using",
                  "show", "result", "large",
                  "also", "one", "two", "three",
                  "four", "five", "seven","eight","nine"]
stop_words = list(stop_words.union(new_stop_words))

def preprocess_text(txt):
    txt = txt.lower()

    txt = re.sub(r"<.*?>", " ", txt) 
    txt = re.sub(r"[^a-zA-Z]", " ", txt)
    txt = nltk.word_tokenize(txt) 
    txt = [word for word in txt if word not in stop_words] 
    txt = [word for word in txt if len(word) > 3]
    return " ".join(txt)

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []
    for idx, score in sorted_items:
        fname = feature_names[idx]
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    results = {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]] = score_vals[idx]
    return results

# Streamlit UI
st.title('Keyword Extraction and Search App')
#img = Image.open('img.jpeg')
st.image(img,width = 350)
# Keyword Extraction Section
st.header("Extract Keywords from a Document")
uploaded_file = st.file_uploader("Upload a document", type=["txt",'pdf'])

if uploaded_file is not None:
    if st.button("Extract Keywords"):
        text = uploaded_file.read().decode('utf-8', errors='ignore')
        preprocessed_text = preprocess_text(text)
        tf_idf_vector = tfidf_transformer.transform(cv.transform([preprocessed_text]))
        sorted_items = sort_coo(tf_idf_vector.tocoo())
        keywords = extract_topn_from_vector(feature_names, sorted_items, 20)

        st.subheader("Extracted Keywords")
        st.table(list(keywords.items()))

# Keyword Search Section
st.header("Search Keywords")
search_query = st.text_input("Enter a keyword to search")

if search_query:
    keywords = [keyword for keyword in feature_names if search_query.lower() in keyword.lower()]
    st.subheader("Search Results")
    st.table(list(keywords[:20]))  # Show up to 20 keywords


