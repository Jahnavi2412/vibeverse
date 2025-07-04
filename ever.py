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
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
# import teen
import ever
df3=pd.read_csv('gamesff.csv',encoding='ISO-8859-1')
dfet=pd.read_csv('Everyone10+.csv',encoding='ISO-8859-1')
dfet['combined_features']=dfet['Genre']+dfet['Rating']
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=10000, stop_words='english')
c=cv.fit_transform(dfet['combined_features'].values.astype('U')).toarray()
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(dfet['combined_features'])
from sklearn.metrics.pairwise import cosine_similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
knn = NearestNeighbors(n_neighbors=10, metric='cosine')  # n_neighbors=10 means top-10 similar games
knn.fit(cosine_sim)

def recommend_games(name):
 game_index = dfet[dfet['Name'].str.lower() == name.lower()].index[0]
 distance, indices = knn.kneighbors(cosine_sim[game_index].reshape(1, -1), n_neighbors=6)
 recommended_game_indices = indices.flatten()[1:]
 recommended_games = dfet.iloc[recommended_game_indices]

def show():
 leftt, middlet, rightt = st.columns(3, vertical_alignment='center')
 g1e=dfet.sample(n=1)
 gamee=g1e["Name"].iloc[0]
 postere=g1e['Poster'].iloc[0]
 leftt.image(postere,width=150)
 with leftt:
    st.write(gamee)
    recommend_games(gamee)
    # 2nd song
    g2e=dfet.sample(n=1)
    game1e=g2e["Name"].iloc[0]  
    poster1e=g2e['Poster'].iloc[0]
    middlet.image(poster1e,width=150)
    with middlet:
     st.write(game1e)
    recommend_games(game1e)

    g3e=dfet.sample(n=1)
    game2e=g3e["Name"].iloc[0]
    poster2e=g3e['Poster'].iloc[0]
    rightt.image(poster2e,width=150)
    with rightt:
     st.write(game2e)
    if st.button("show"):
     a=recommend_games(game2e)
    st.write(a)  
    lefttt, middlett, righttt = st.columns(3, vertical_alignment='center')
    g4e=dfet.sample(n=1)
    game3e=g4e["Name"].iloc[0]
    poster3e=g4e['Poster'].iloc[0]
    lefttt.image(poster3e,width=150)
    with lefttt:
     st.write(game3e)
    # 2nd song
    g5e=dfet.sample(n=1)
    game4e=g5e["Name"].iloc[0]   
    poster4e=g5e['Poster'].iloc[0]
    middlett.image(poster4e,width=150)
    with middlett:
     st.write(game4e)
    recommend_games(game4e)
    g6e=dfet.sample(n=1)
    game5e=g6e["Name"].iloc[0]
    poster5e=g6e['Poster'].iloc[0]
    righttt.image(poster5e,width=150)
    with righttt:
     st.write(game5e)
    lefty, middlej, rightk = st.columns(3, vertical_alignment='center')
    g7e=dfet.sample(n=1)
    game6e=g7e["Name"].iloc[0]
    poster6e=g7e['Poster'].iloc[0]
    lefty.image(poster6e,width=150)
    with lefty:
     st.write(game6e)
    # 2nd song
    g8e=dfet.sample(n=1)
    game7e=g8e["Name"].iloc[0]  
    poster7e=g8e['Poster'].iloc[0]
    middlej.image(poster7e,width=150)
    with middlej:
     st.write(game7e)
    # 3rd song
    g9e=dfet.sample(n=1)
    game8e=g9e["Name"].iloc[0]
    poster8e=g9e['Poster'].iloc[0]
    rightk.image(poster8e,width=150)
    with rightk:
     st.write(game8e)


    rating=st.selectbox("Select Rating:",['Everyone','Above 10 years','Teens','Mature'],key='rating')

    #   # if rating=="Everyone":
    #   #  everyone.show()
    if rating=="Above 10 years":
     ever.show()
    #   # # elif rating=="Teens":
    #   # #  teen.show()
    #   # elif rating=="Mature":
    #   #  mature.show()
    