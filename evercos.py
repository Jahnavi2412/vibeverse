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
dft=pd.read_csv('Everyone10+.csv',encoding='ISO-8859-1')
def show():
#  search_query = st.text_input("Search for a song")
#  if search_query:
#      if len(search_query) >= 3:
#       fil_df=dft[dft.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
#       if not fil_df.empty:
#        st.subheader("Search Results:")
#        if len(fil_df)==1:
#          img=fil_df['Poster'].iloc[0]
#          st.image(img,width=200)
#          s=fil_df['Name'].iloc[0]
#        else:
#         lef, mid = st.columns(2)
#         img1=fil_df['Poster'].iloc[0]
#         img2=fil_df['Poster'].iloc[1]
#         s1=fil_df['Name'].iloc[0]
#         s2=fil_df['Name'].iloc[1]
  import random
  if 'songs_eselected' not in st.session_state:
    st.session_state.songs_eselected = random.sample(dft.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_left = st.session_state.songs_eselected[0]
    st.session_state.current_song_middle = st.session_state.songs_eselected[1]
    st.session_state.current_song_right = st.session_state.songs_eselected[2]
    st.session_state.current_song_le = st.session_state.songs_eselected[3]
    st.session_state.current_song_mi = st.session_state.songs_eselected[4]
    st.session_state.current_song_ri = st.session_state.songs_eselected[5]
    st.session_state.current_song_lee = st.session_state.songs_eselected[6]
    st.session_state.current_song_mii = st.session_state.songs_eselected[7]
    st.session_state.current_song_rii = st.session_state.songs_eselected[8]
    
    left, middle, right = st.columns(3)
    song1 = st.session_state.current_song_left
    song2=st.session_state.current_song_middle
    song3=st.session_state.current_song_right
    song4= st.session_state.current_song_le 
    song5= st.session_state.current_song_mi
    song6= st.session_state.current_song_ri
    song7=st.session_state.current_song_lee
    song8=st.session_state.current_song_mii
    song9=st.session_state.current_song_rii

    s_l=song1['Name']
    s_m=song2['Name']
    s_r=song3['Name']
    s_le=song4['Name']
    s_mi=song5['Name']
    s_ri=song6['Name']
    s_lee=song7['Name']
    s_mii=song8['Name']
    s_rii=song9['Name']

  dft['combined_features']=dft['Genre']+dft['Rating']
  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  c=cv.fit_transform(dft['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c)
  import random
  def recommand(song_name):
      idx=dft[dft['Name']==song_name].index[0]
      distance = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda vector:vector[1])
# 
      s=[dft.iloc[i[0]] for i in distance[1:7]]
#  random.shuffle(s1)
  
      rec = random.sample(s, min(len(s), 7))
      for song in rec: 
#  st.write(s1)
       songs = song['Name']
       poster_url = song['Poster']    # ✅ Access poster directly
       st.image(poster_url, width=150)
       st.write(songs)
  import urllib
  import requests
  song1 = st.session_state.current_song_left
  song2=st.session_state.current_song_middle
  song3=st.session_state.current_song_right
  song4= st.session_state.current_song_le 
  song5= st.session_state.current_song_mi
  song6= st.session_state.current_song_ri
  song7=st.session_state.current_song_lee
  song8=st.session_state.current_song_mii
  song9=st.session_state.current_song_rii
  s_l=song1['Name']
  s_m=song2['Name']
  s_r=song3['Name']
  s_le=song4['Name']
  s_mi=song5['Name']
  s_ri=song6['Name']
  s_lee=song7['Name']
  s_mii=song8['Name']
  s_rii=song9['Name']
  left, middle, right = st.columns(3)              
  left.image(song1['Poster'], width=150)
  with left:
     st.write(s_l)
     if st.button("Recommendations:",key='leftg'):
      recommand(s_l)
  middle.image(song2['Poster'], width=150)
  with middle:
     st.write(s_m)
     if st.button("Recommendations:",key='middleg'):
      recommand(s_m)
  right.image(song3['Poster'], width=150)
  with right:
     st.write(s_r)
     if st.button("Recommendations:",key='rightg'):
      recommand(s_r)
  le, mi, ri = st.columns(3)
  with le:
   song4= st.session_state.current_song_le
   st.image(song4['Poster'], width=150)
   st.write(song4['Name'])
   if st.button("Recommendations:", key="leg"):
      recommand(s_le)
  with mi:
    song5 = st.session_state.current_song_mi
    st.image(song5['Poster'], width=150)
    st.write(song5['Name'])
    if st.button("Recommendations", key="mig"):
      recommand(s_mi)
  with ri:
    song6 = st.session_state.current_song_ri
    st.image(song6['Poster'], width=150)
    st.write(song6['Name'])
    if st.button("Recommendations", key="rig"):
      recommand(s_ri)
  lee, mii, rii = st.columns(3)
  with lee:
    song7= st.session_state.current_song_lee
    st.image(song7['Poster'], width=150)
    st.write(song7['Name'])
    if st.button("Recommendations", key="leeg"):
      recommand(s_lee)
  with rii:
    song8= st.session_state.current_song_rii
    st.image(song8['Poster'], width=150)
    st.write(song8['Name'])
    if st.button("Recommendations", key="riig"):
      recommand(s_lee)
  with mii:
    song9= st.session_state.current_song_mii
    st.image(song9['Poster'], width=150)
    st.write(song9['Name'])
    if st.button("Recommendations", key="miig"):
      recommand(s_lee)
show()