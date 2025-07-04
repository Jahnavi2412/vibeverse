import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image
import webbrowser
import pyttsx3
import requests
import re
import urllib
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# from sklearn.metrics.pairwise import cosine_similarity
st.set_page_config(page_title='VibeVista')
st.title(":red[VibeVista:microphone:]")
# df1 = pd.read_csv('movieorig.csv',encoding='ISO-8859-1')
df=pd.read_csv('music1.csv',encoding='ISO-8859-1')
df3=pd.read_csv('punjabimusic.csv',encoding='ISO-8859-1')
l=st.selectbox(label='Enter Language',options=['Hindi','English','Punjabi'])
if l=='Punjabi':
    dmp=df3[df3['language']=='Punjabi']
import random
dmp=df3[df3['language']=='Punjabi']
if 'songs_pselected' not in st.session_state:
 st.session_state.songs_pselected = random.sample(dmp.to_dict('records'), 9)  # Pick 2 random songs
st.session_state.current_song_left = st.session_state.songs_pselected[0]
st.session_state.current_song_middle = st.session_state.songs_pselected[1]
st.session_state.current_song_right = st.session_state.songs_pselected[2]
st.session_state.current_song_le = st.session_state.songs_pselected[3]
st.session_state.current_song_mi = st.session_state.songs_pselected[4]
st.session_state.current_song_ri = st.session_state.songs_pselected[5]
st.session_state.current_song_lee = st.session_state.songs_pselected[6]
st.session_state.current_song_mii = st.session_state.songs_pselected[7]
st.session_state.current_song_rii = st.session_state.songs_pselected[8]
# Layout columns
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

s_l=song1['song_name']
s_m=song2['song_name']
s_r=song3['song_name']
s_le=song4['song_name']
s_mi=song5['song_name']
s_ri=song6['song_name']
s_lee=song7['song_name']
s_mii=song8['song_name']
s_rii=song9['song_name']

def talk_r(s_r):
         engine = pyttsx3.init()
         engine.say(s_r)
         engine.runAndWait()
         def play_songs(s_r):
             if (s_r):
              st.write(f"Playing the song: {s_r}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_r + " official audio")
              url=f"https://www.youtube.com/results?search_query={s_r}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}") 
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
              if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
              else:
               return None
              
             else:
                st.write("Please provide a song name.")
                talk_r("Please provide a song name.")
        #  play_songs(s_l)
         def play(s_r):
              url = play_songs(s_r)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(s_r)



  

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=10000, stop_words='english')
df3['combined_features']=df3['Genre']+df3['language']
c3=cv.fit_transform(df3['combined_features'].values.astype('U')).toarray()
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(c3)
# similarity
ds3  = df3.drop(columns=['Genre','language','poster'])
# idx=ds[ds['song_name']==s_l].index[0]
# idxrandom
import random
# l, m, r = st.columns(3) 
def recommandp(song_name):
    index=df3[df3['song_name']==song_name].index[0]
    distance3 = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    # selected_songs = set()
    # s = []
    # for i in distance2[1:]:  # Skip the first one (itself)
    #  song_series = df2.iloc[i[0]]  # Get the song details (as Series)
    #  song_tuple = tuple(song_series)  # Convert Series to a hashable tuple
    
    #  if song_tuple not in selected_songs:
    #     s.append(song_series)  # Append original Series (not tuple)
    #     selected_songs.add(song_tuple)  # Track song in the set
        
    #  if len(s) == 6:  # Stop when we have 6 unique recommendations
    #     break

    # for i in distance2[1:]:  # Skip the first one (itself)
    #   song = df2.iloc[i[0]]
    #   if song not in s:
    #     s.append(song)
  #       selected_songs.add(song)
  #   if len(top_6_similar) == 6:  # Stop when we have 6 unique recommendations
  #       break
    s3=[df3.iloc[i[0]] for i in distance3[1:7]]
#  random.shuffle(s1)
  
    rec = random.sample(s3, min(len(s3), 7))
    for song in rec: 
#  st.write(s1)
     songs = song['song_name']
     poster_url = song['poster']    # ✅ Access poster directly
     st.image(poster_url, width=150)
     st.write(songs)
    
  #sl=s1.sample(n=5)
#  st.write(s1)
def talk_l(s_l):
        engine = pyttsx3.init()
        engine.say(s_l)
        engine.runAndWait()
        def play_songs(s_l):
            if (s_l):
             st.write(f"Playing the song: {s_l}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_l + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_l}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            else:
              return None
            
           
      #  play_songs(s_l)
        def play(s_l):
            url = play_songs(s_l)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_l)

def talk_m(s_m):
        engine = pyttsx3.init()
        engine.say(s_m)
        engine.runAndWait()
        def play_songs(s_m):
            if (s_m):
              st.write(f"Playing the song: {s_m}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_m + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_m}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            
            else:
              st.write("Please provide a song name.")
              talk_m("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_m):
            url = play_songs(s_m)
            if url:
              st.markdown(
                  f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_m)
# recommand(s_l)      
# 1st column
song1 = st.session_state.current_song_left
song2=st.session_state.current_song_middle
song3=st.session_state.current_song_right
song4= st.session_state.current_song_le 
song5= st.session_state.current_song_mi
song6= st.session_state.current_song_ri
song7=st.session_state.current_song_lee
song8=st.session_state.current_song_mii
song9=st.session_state.current_song_rii
s_l=song1['song_name']
s_m=song2['song_name']
s_r=song3['song_name']
s_le=song4['song_name']
s_mi=song5['song_name']
s_ri=song6['song_name']
s_lee=song7['song_name']
s_mii=song8['song_name']
s_rii=song9['song_name']
left, middle, right = st.columns(3)              
left.image(song1['poster'], width=150)
with left:
  st.write(s_l)
  if st.button("▶ Play", key="play_pleft"):
  # v=s_l
   talk_l(s_l)
#  if st.button("Recommend", key="rec_left"):
   st.subheader("Made For You:")
   recommandp(s_l)   #recommnded songs for left
    
middle.image(song2['poster'], width=150)
with middle:
  st.write(s_m)
  if st.button("▶ Play", key="play_pmiddle"):
  # v=s_l
    talk_m(s_m)     
    recommandp(s_m)
# if st.button("Recommend", key="rec_middle")  
right.image(song3['poster'], width=150)
with right:
  st.write(s_r)
  if st.button("▶ Play", key="play_pright"):
  # v=s_l
    talk_r(s_r)
    recommandp(s_r)
  
# 2 layout columns 
import requests
def talk_le(s_le):
        engine = pyttsx3.init()
        engine.say(s_le)
        engine.runAndWait()
        def play_songs(s_le):
            if (s_le):
             st.write(f"Playing the song: {s_le}")
            query = urllib.parse.quote(s_le + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_le}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_le("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_le):
            url = play_songs(s_le)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_le)


def talk_mi(s_mi):
        engine = pyttsx3.init()
        engine.say(s_mi)
        engine.runAndWait()
        def play_songs(s_mi):
            if (s_mi):
             st.write(f"Playing the song: {s_mi}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mi + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_mi}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_mi("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_mi):
            url = play_songs(s_mi)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mi)
import urllib
def talk_ri(s_ri):
        engine = pyttsx3.init()
        engine.say(s_ri)
        engine.runAndWait()
        def play_songs(s_ri):
            if (s_ri):
             st.write(f"Playing the song: {s_ri}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_ri + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_ri}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_r("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_ri):
            url = play_songs(s_ri)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_ri)

# Left Column - Fixed Song. 2nd column
le, mi, ri = st.columns(3)
with le:
  song4= st.session_state.current_song_le
  st.image(song4['poster'], width=150)
  st.write(song4['song_name'])
  if st.button("▶ Play", key="play_ple"):
      talk_le(s_le)
      recommandp(s_le)
  
# Middle Column - Fixed Song 2
with mi:
  song5 = st.session_state.current_song_mi
  st.image(song5['poster'], width=150)
  st.write(song5['song_name'])
  if st.button("▶ Play", key="play_pmi"):
      talk_mi(s_mi)
      recommandp(s_mi)
      

# Right Column - "Now Playing" Section
with ri:
  song6 = st.session_state.current_song_ri
  st.image(song6['poster'], width=150)
  st.write(song6['song_name'])
  if st.button("▶ Play", key="play_pri"):
      talk_ri(s_ri)
      recommandp(s_ri)
      
      # 3rd row
lee, mii, rii = st.columns(3)
def talk_lee(s_lee):
        engine = pyttsx3.init()
        engine.say(s_lee)
        engine.runAndWait()
        def play_songs(s_lee):
            if (s_lee):
             st.write(f"Playing the song: {s_lee}")
            query = urllib.parse.quote(s_mi + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_lee}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_lee("Please provide a song name.")
      #  play_songs_l)
        def play(s_lee):
            url = play_songs(s_lee)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_lee)
def talk_mii(s_mii):
        engine = pyttsx3.init()
        engine.say(s_mii)
        engine.runAndWait()
        def play_songs(s_mii):
            if (s_mi):
             st.write(f"Playing the song: {s_mii}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mi + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_mii}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_mii("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_mii):
            url = play_songs(s_mii)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mii)
def talk_rii(s_rii):
        engine = pyttsx3.init()
        engine.say(s_rii)
        engine.runAndWait()
        def play_songs(s_rii):
            if (s_rii):
             st.write(f"Playing the song: {s_rii}")
            
            
            query = urllib.parse.quote(s_rii + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_rii}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_rii("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_rii):
            url = play_songs(s_rii)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_rii)
# Left Column - Fixed Song 1
with lee:
  song7= st.session_state.current_song_lee
  st.image(song7['poster'], width=150)
  st.write(song7['song_name'])
  if st.button("▶ Play", key="play_plee"):
      talk_lee(s_lee)
      recommandp(s_lee)
# Middle Column - Fixed Song 2
with mii:
  song8 = st.session_state.current_song_mii
  st.image(song8['poster'], width=150)
  st.write(song8['song_name'])
  if st.button("▶ Play", key="play_pmii"):
      talk_mii(s_mii)
      recommandp(s_mii)

# Right Column - "Now Playing" Section
with rii:
  song9 = st.session_state.current_song_rii
  st.image(song9['poster'], width=150)
  st.write(song9['song_name'])
  if st.button("▶ Play", key="play_prii"):
      talk_rii(s_rii)
      recommandp(s_rii)