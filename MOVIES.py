import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image
import webbrowser
import pyttsx3
import requests
import re
import urllib.parse
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# from sklearn.metrics.pairwise import cosine_similarity
st.set_page_config(page_title='VibeVista')
# st.markdown('<p style="color:blue;">VibeVista</p>', unsafe_allow_html=True)
st.title(":blue[VibeVista:microphone:]")
df1 = pd.read_csv('movieorig.csv',encoding='ISO-8859-1')
st.markdown("""
    <style>
    .big-font { font-size:24px !important; font-weight: bold; color: #FF4B4B; }
    .song-box { background-color: #222; padding: 15px; border-radius: 10px; color: green; }
    </style>
    """, unsafe_allow_html=True)


# App Header music
# st.markdown('<p class="title">🎶 Music Recomendation System</p>',unsafe_allow_html=True)
# --- HEADER --- music
st.markdown('<p class="big-font">🎶 Discover Your Next Favorite Song 🎶</p>', unsafe_allow_html=True)
# df=pd.read_csv('music1.csv',encoding='ISO-8859-1')
# songs=df

option=st.sidebar.selectbox("Select options",options=['Home','Music','Movies','K-Drama'])
if option=='Movies':
  search_query = st.text_input("Search for a movie")
  if search_query:
#    if len(search_mquery) >= 3:
   fil_df1=df1[df1.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
   if not fil_df1.empty:
    st.subheader("Search Results:")
    #  if len(fil_df)==1:
     
    m=fil_df1['Title'].iloc[0]
    st.write(m)
    img=fil_df1['poster_path'].iloc[0]
    st.image(img,width=200)
    def talk_lm(m):
         engine = pyttsx3.init()
         engine.say(m)
         engine.runAndWait()
    def play_movie(m):
            if (m):
              st.write(f"Playing the trailer: {m}")
              
              query = urllib.parse.quote(m + "official trailer")
              url=f"https://www.youtube.com/results?search_query={m}"
              response = requests.get(url)
              st.write(response)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
              st.write(video_ids)
              if video_ids:
                 return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
                 return None
              
            else:
                st.write("Please provide a movie name.")
                talk_lm("Please provide a movie name.")
        #  play_songs(s_l)
    def playm(m):
              url = play_movie(m)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
               st.error("No video found for this movie 😢")
      
    if st.button("▶ Play"):
      talk_lm(m)
      # play_movie(m)
      playm(m)
    st.write(m)
    #  st.write(s1)
    