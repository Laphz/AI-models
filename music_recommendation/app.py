import streamlit as st
import pickle
from PIL import Image


# Load models
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommendation(song_df):
    idx = df[df['song'] == song_df].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

    songs = []
    for m_id in distances[1:21]:
        songs.append(df.iloc[m_id[0]].song)

    return songs

# Streamlit app
st.title('Song Recommendation System')
img = Image.open('img.jpeg')
img = img.resize((600,400))
st.image(img)
# Dropdown for song selection
selected_song = st.selectbox("Select a song you like:", df['song'].values)

# Button to generate recommendations
if st.button("Recommend"):
    recommended_songs = recommendation(selected_song)
    st.subheader("Recommended Songs:")

    # Display recommendations in a grid with the headphone logo
    music_logo = 'Music_logo.png'  # Local path to the music logo image

    cols_per_row = 3  # Number of columns per row

    for i in range(0, len(recommended_songs), cols_per_row):
        cols = st.columns(cols_per_row)
        for col, song in zip(cols, recommended_songs[i:i + cols_per_row]):
            with col:
                st.image(music_logo, width=100)
                st.write(f"**{song}**")

