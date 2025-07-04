import pickle
import numpy as np
from PIL import Image
import webbrowser
import pyttsx3
import requests
import re
import streamlit as st
import urllib
import pandas as pd
import teen
# import everyone

st.title(":red[Games]")
df3=pd.read_csv('gamesff.csv',encoding='ISO-8859-1')
dft=pd.read_csv("Teens.csv")
dt=dft

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity

tfidf_vectorizer = TfidfVectorizer(stop_words='english')
dt['combined_features']=dt['Genre']+dt['Rating']
tfidf_matrix = tfidf_vectorizer.fit_transform(dt['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
knn = NearestNeighbors(n_neighbors=10, metric='cosine') # Make sure cosine_sim is fitted properly
knn.fit(cosine_sim)
knn.fit(cosine_sim)

def recommend_games(name):
    name = str(name).lower()
    matches = dt[dt['Name'].str.lower() == name]

    if matches.empty:
        st.warning(f"No match found for '{name}'")
        return []

    game_index = matches.index[0]
    distance, indices = knn.kneighbors(cosine_sim[game_index].reshape(1, -1), n_neighbors=6)
    recommended_game_indices = indices.flatten()[1:]

    return dt.iloc[recommended_game_indices][['Name', 'Poster']]

# Streamlit UI
st.title("🎮 Game Recommender")

game_name = st.text_input("Enter a game name:")

if game_name:
    recs = recommend_games(game_name)

    if recs:
        st.subheader("Recommended Games")
        for rec in recs:
            st.markdown(f"**{rec['Name']}**")
            try:
                st.image(rec['Poster'], width=200)
            except Exception as e:
                st.error(f"Couldn't load image for {rec['Name']}")
# def recommend_games(name):
#     name = str(name).lower()
#     matches = dt[dt['Name'].str.lower() == name]
    
#     if matches.empty:
#         print(f"No match found for '{name}'")
#         return []

#     game_index = matches.index[0]
#     distance, indices = knn.kneighbors(cosine_sim[game_index].reshape(1, -1), n_neighbors=6)
#     recommended_game_indices = indices.flatten()[1:]
#     return dt.iloc[recommended_game_indices][['Name', 'Poster']]
# sample_game = dt['Name'].iloc[0]  # You can replace this with any known game name
# recommendations = recommend_games(sample_game)

# # Print results with poster URLs
# for _, row in recommendations.iterrows():
#     st.write(f"🎮 {row['Name']}")
#     st.image(f"🖼️  Poster: {row['Poster']}")
#     st.write()
# Example usage with the first game's name
# first_game_name = dt['Name'].iloc[0]
# g = recommend_games(first_game_name)

# # Print recommended games
# for m in g:
#     print(m)

def show():

 leftt, middlet, rightt = st.columns(3, vertical_alignment='center')
 g1t=dft.sample(n=1)
 gamet=g1t["Name"].iloc[0]
 postert=g1t['Poster'].iloc[0]
 leftt.image(postert,width=150)
 with leftt:
  st.write(gamet)
  if st.button("Recommend", key="play_ple"):
   recommend_games(gamet)
   
# 2nd song
 g2t=dft.sample(n=1)
 game1t=g2t["Name"].iloc[0]  
 poster1t=g2t['Poster'].iloc[0]
 middlet.image(poster1t,width=150)
 with middlet:
  st.write(game1t)
  if st.button("Recommend", key="play_ple1"):
   recommend_games(game1t)
   
  # 3rd song
 g3t=dft.sample(n=1)
 game2t=g3t["Name"].iloc[0]
 poster2t=g3t['Poster'].iloc[0]
 rightt.image(poster2t,width=150)
 with rightt:
  st.write(game2t)
  if st.button("Recommend", key="play_ple2"):
   recommend_games(game2t)
    
         
 lefttt, middlett, righttt = st.columns(3, vertical_alignment='center')
 g4t=dft.sample(n=1)
 game3t=g4t["Name"].iloc[0]
 poster3t=g4t['Poster'].iloc[0]
 lefttt.image(poster3t,width=150)
 with lefttt:
  st.write(game3t)
  if st.button("Recommend", key="play_ple3"):
   recommend_games(game3t)
   
# 2nd song
 g5t=dft.sample(n=1)
 game4t=g5t["Name"].iloc[0]   
 poster4t=g5t['Poster'].iloc[0]
 middlett.image(poster4t,width=150)
 with middlett:
  st.write(game4t)
  if st.button("Recommend", key="play_ple4"):
   recommend_games(game4t)
   
  # 3rd song
 g6t=dft.sample(n=1)
 game5t=g6t["Name"].iloc[0]
 poster5t=g6t['Poster'].iloc[0]
 righttt.image(poster5t,width=150)
 with righttt:
  st.write(game5t)
  if st.button("Recommend", key="play_ple5"):
   recommend_games(game5t)
   
 lefty, middlej, rightk = st.columns(3, vertical_alignment='center')
 g7t=dft.sample(n=1)
 game6t=g7t["Name"].iloc[0]
 poster6t=g7t['Poster'].iloc[0]
 lefty.image(poster6t,width=150)
 with lefty:
  st.write(game6t)
  if st.button("Recommend", key="play_ple6"):
   recommend_games(game6t)
   
# 2nd song
 g8t=dft.sample(n=1)
 game7t=g8t["Name"].iloc[0]  
 poster7t=g8t['Poster'].iloc[0]
 middlej.image(poster7t,width=150)
 with middlej:
  st.write(game7t)
  if st.button("Recommend", key="play_ple7"):
   recommend_games(game7t)
   
  # 3rd song
 g9t=dft.sample(n=1)
 game8t=g9t["Name"].iloc[0]
 poster8t=g9t['Poster'].iloc[0]
 rightk.image(poster8t,width=150)
 with rightk:
  st.write(game8t)
  if st.button("Recommend", key="play_ple8"):
   recommend_games(game8t)
   