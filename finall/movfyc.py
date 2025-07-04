import streamlit as st
import pandas as pd
import random
import urllib
import requests
import re
# Load datasets (Replace with actual CSV file paths)
music_df = pd.read_csv("music1.csv",encoding='ISO-8859-1')  # Columns: ['Title', 'Artist', 'Genre', 'Year', 'Link', 'Poster']
movie_df = pd.read_csv("movieorig.csv",encoding='ISO-8859-1')  # Columns: ['Title', 'Director', 'Genre', 'Year', 'Trailer', 'Poster']

st.title("🎵🎬 Music & Movie Recommendation System")

# --- DISPLAY 9 RANDOM POSTERS ON HOMEPAGE ---
st.header("🔥 Trending Now")

# Combine posters from both datasets
all_posters = list(music_df['poster'].dropna()) + list(movie_df['poster_path'].dropna())

# Select 9 random posters
random_posters = random.sample(all_posters, min(9, len(all_posters)))

# Show posters in a grid
cols = st.columns(3)  # Create 3 columns per row
for i, poster in enumerate(random_posters):
    with cols[i % 3]:  # Distribute posters across columns
        st.image(poster, use_column_width=True)

# --- USER SELECTION FOR RECOMMENDATIONS ---

st.sidebar.header("🎶 Choose Your Music Preferences")
selected_music_genres = st.sidebar.multiselect("Select Music Genre(s):", music_df['Genre'].unique())

st.sidebar.header("🎥 Choose Your Movie Preferences")
selected_movie_genres = st.sidebar.multiselect("Select Movie Genre(s):", movie_df['genres'].unique())

# Filter recommendations
filtered_music = music_df[music_df['Genre'].isin(selected_music_genres)]
filtered_movies = movie_df[movie_df['genres'].isin(selected_movie_genres)]

# --- DISPLAY MUSIC RECOMMENDATIONS ---
if not filtered_music.empty:
    st.subheader("🎼 Recommended Songs:")
    for _, row in filtered_music.iterrows():
        st.write(f"🎵 **{row['song_name']}** by {row['singer']} ({row['Year']})")
        url=f"https://www.youtube.com/results?search_query"

        response = requests.get(url)

        video_ids = re.findall(r"watch\?v=(\S{11})", response.text)

        Link= f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
        st.markdown(f"[▶ Play](['Link'])", unsafe_allow_html=True)

# --- DISPLAY MOVIE RECOMMENDATIONS ---
if not filtered_movies.empty:
    st.subheader("🎬 Recommended Movies:")
    for _, row in filtered_movies.iterrows():
        st.write(f"🎬 **{row['Title']}** directed by {row['Director']} ({row['overview']})")
        url=f"https://www.youtube.com/results?search_query"

        response = requests.get(url)

        video_ids = re.findall(r"watch\?v=(\S{11})", response.text)

        Trailer= f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
        st.markdown(f"[▶ Watch Trailer]({row['Trailer']})", unsafe_allow_html=True)
        query = urllib.parse.quote('Title' + " official trailer")
        url=f"https://www.youtube.com/results?search_query"
    #   webbrowser.open(url)
    #   print(f"Playing song: {s_l}")
        response = requests.get(url)
        video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
        if video_ids:
           Trailer= f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"