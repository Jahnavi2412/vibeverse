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
st.set_page_config(page_title='VibeVista')
st.title(":red[VibeVista:microphone:]")
df=pd.read_csv('music1.csv',encoding='ISO-8859-1')
df1=pd.read_csv('englishmusic.csv',encoding='ISO-8859-1')
df2=pd.read_csv('hindimusic.csv',encoding='ISO-8859-1')
df3=pd.read_csv('punjabimusic.csv',encoding='ISO-8859-1')


# st.set_page_config(page_title="Music Selector", layout="wide")


# st.title("🎵 Music Selection App")
option=st.sidebar.selectbox("Select options",options=['Home','Music','Movies','K-Drama'])
if option=='Home':
 st.header("Music for You",divider='rainbow')
 left, middle, right = st.columns(3, vertical_alignment='center')
# 1st song
# english music
 s1=df.sample(n=1)
 song=s1["song_name"].iloc[0]
 poster=s1['poster'].iloc[0]
 left.image(poster,width=150)
 with left:
  st.write(song)
# 2nd song
 s2=df.sample(n=1)
 song1=s2["song_name"].iloc[0]  
 poster1=s2['poster'].iloc[0]
 middle.image(poster1,width=150)
 with middle:
  st.write(song1)
  # 3rd song
 s3=df.sample(n=1)
 song2=s3["song_name"].iloc[0]
 poster2=s3['poster'].iloc[0]
 right.image(poster2,width=150)
 with right:
  st.write(song2)
 left, middle, right = st.columns(3, vertical_alignment='center')

#  movies
 df2=pd.read_csv("movieorig.csv",encoding='ISO-8859-1')
 st.header("Movies For You",divider='green')
 left, middle, right = st.columns(3, vertical_alignment='center')
# 1st movie
 m1=df2.sample(n=1)
 mo=m1["Title"].iloc[0]
 mposter=m1['poster_path'].iloc[0]
 left.image(mposter,width=150)
 with left:
  st.write(mo)
# 2nd song
 m2=df2.sample(n=1)
 mmo=m2["Title"].iloc[0]
 mmposter=m2['poster_path'].iloc[0]
 middle.image(mmposter,width=150)
 with middle:
  st.write(mmo)
  # 3rd song
 m3=df2.sample(n=1)
 mmmo2=m3["Title"].iloc[0]
 mmmposter2=m3['poster_path'].iloc[0]
 right.image(mmmposter2,width=150)
 with right:
  st.write(mmmo2)
# # kdrama
#  df3=pd.read_csv("kdrama1.csv",encoding='ISO-8859-1')
#  st.header("K-Drama for You",divider='blue')
#  left, middle, right = st.columns(3, vertical_alignment='center')
 
# 1st movie
 k1=df2.sample(n=1)
 kd=k1["Name"].iloc[0]
 kposter=k1['Poster Path'].iloc[0]
 left.image(kposter,width=150)
 with left:
  st.write(kd)
# 2nd song
 k2=df2.sample(n=1)
 kk=k2["Name"].iloc[0]
 kkposter=k2['Poster Path'].iloc[0]
 middle.image(kkposter,width=150)
 with middle:
  st.write(kk)
  # 3rd song
 k3=df2.sample(n=1)
 kk3=k3["Name"].iloc[0]
 kkposter2=k3['Poster Path'].iloc[0]
 right.image(kkposter2,width=150)
 with right:
  st.write(kk3)
  song1=st.session_state.current_song_left
  song2=st.session_state.current_song_middle
  song3=st.session_state.current_song_right
  s_l=song1['song_name']
  s_m=song2['song_name']
  s_r=song3['song_name']

  def talk_l(so):
         engine = pyttsx3.init()
         engine.say(so)
         engine.runAndWait()
         def play_songs(so):
             if (so):
              st.write(f"Playing the song: {so}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_l + " official audio")
              url=f"https://www.youtube.com/results?search_query={s_l}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}")
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
              if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
               return None
              
             else:
                st.write("Please provide a song name.")
                talk_l("Please provide a song name.")
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
               return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
               return None
              
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

# Select language
language = st.selectbox("Select a language:", ["English", "Hindi", "Punjabi"])

# Navigate based on selection
if language == "English":
    st.switch_page("pages/englishmusic.py")
# elif language == "Hindi":
#     st.switch_page("pages/hindi.py")
# elif language == "Punjabi":
#     st.switch_page("pages/punjabi.py")
elif language=='Punjabi':
    st.switch_page("pages/punjabimusic.py")
elif language=='Hindi':
    st.switch_page("pages/hindimusic.py")
else:
  st.write("")
