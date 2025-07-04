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

dfk=pd.read_csv('kdrama1 final.csv',encoding='ISO-8859-1')

def show():
   
  search_query = st.text_input("Search for a kdrama")
  if search_query:
     if len(search_query) >= 3:
      fil_df=dfk[dfk.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
      if not fil_df.empty:
       st.subheader("Search Results:")
       if len(fil_df)==1:
    #  st.write(fil_df)
        img=fil_df['Poster Path'].iloc[0]
    #  img1=fil_df['poster'].iloc[1]
# st.columns
      # with left:
        st.image(img,width=200)
    #  st.image(img1,width=200)
        s=fil_df['Name'].iloc[0]
        import urllib
        import requests
        def talk_l(s):
         engine = pyttsx3.init()
         engine.say(s)
         engine.runAndWait()
        def play_songs(s):
             if (s):
              st.write(f"Playing the kdrama: {s}")
              
              query = urllib.parse.quote(s + "kdrama")
              url=f"https://www.youtube.com/results?search_query={s}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}")
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
              if video_ids:
                 return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              # else:


              #    return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
                 return None
              
             else:
                st.write("Please provide a K-Drama name.")
                talk_l("Please provide a K-Drama name.")
        #  play_songs(s_l)
        def play(s):
              url = play_songs(s)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this K-Drama 😢")
      
        if st.button("▶ Play"):
         talk_l(s)
         play_songs(s)
         play(s)
    
         st.write(s)
    
        else: 
          lef, mid = st.columns(2)
          img1=fil_df['Poster Path'].iloc[0]
          img2=fil_df['Poster Path'].iloc[1]
          
          
          s1=fil_df['Poster Path'].iloc[0]
          s2=fil_df['Poster Path'].iloc[1]
          
        def talk_l(s1):
         engine = pyttsx3.init()
         engine.say(s1)
         engine.runAndWait()
        def play_songs(s1):
             if (s1):
              st.write(f"Playing the kdrama: {s1}")
              
              query = urllib.parse.quote(s1 + "kdrama")
              url=f"https://www.youtube.com/results?search_query={s1}"
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
              if video_ids:
                 return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              # else:
              #    return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
                 return None
              
             else:
                st.write("Please provide a K-Drama name.")
                talk_l("Please provide a K-Drama name.")
        def play(s1):
              url = play_songs(s1)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this K-Drama 😢")
        def talk_m(s2):
         engine = pyttsx3.init()
         engine.say(s2)
         engine.runAndWait()
         def play_songs(s2):
             if (s2):
              st.write(f"Playing the kdrama: {s2}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s2 + "kdrama")
              url=f"https://www.youtube.com/results?search_query={s2}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}")
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
              if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
               return None
              
             else:
                st.write("Please provide a K-Drama name.")
                talk_m("Please provide a K-Drama name.")
        #  play_songs(s_l)
             def play(s2):
              url = play_songs(s2)
              if url:
                st.markdown(
                   f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this K-Drama 😢")
             play(s2)
        lef.image(img1,width=200)
        with lef:
         st.write(s1)
         if st.button("▶ Play",key="re_lef"):
          talk_l(s1)
          play_songs(s1)
          play(s1)
      
        mid.image(img2,width=200)
        with mid:
         st.write(s2)
         if st.button("▶ Play",key="re_mid"):
          talk_m(s2)
          play_songs(s2)
          play(s2)
         else:
          st.write("K-Drama does not exist")
  else:
      st.write("")
  import random
  if 'songs_eselected' not in st.session_state:
    st.session_state.songs_kselected = random.sample(dfk.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_leftk = st.session_state.songs_kselected[0]
    st.session_state.current_song_middlek = st.session_state.songs_kselected[1]
    st.session_state.current_song_rightk = st.session_state.songs_kselected[2]
    st.session_state.current_song_lek = st.session_state.songs_kselected[3]
    st.session_state.current_song_mik = st.session_state.songs_kselected[4]
    st.session_state.current_song_rik = st.session_state.songs_kselected[5]
    st.session_state.current_song_leek = st.session_state.songs_kselected[6]
    st.session_state.current_song_miik = st.session_state.songs_kselected[7]
    st.session_state.current_song_riik = st.session_state.songs_kselected[8]
# Layout columns
    left, middle, right = st.columns(3)
    song1k = st.session_state.current_song_leftk
    song2k=st.session_state.current_song_middlek
    song3k=st.session_state.current_song_rightk
    song4k= st.session_state.current_song_lek 
    song5k= st.session_state.current_song_mik
    song6k= st.session_state.current_song_rik
    song7k=st.session_state.current_song_leek
    song8k=st.session_state.current_song_miik
    song9k=st.session_state.current_song_riik

    s_lk=song1k['Name']
    s_mk=song2k['Name']
    s_rk=song3k['Name']
    s_lek=song4k['Name']
    s_mik=song5k['Name']
    s_rik=song6k['Name']
    s_leek=song7k['Name']
    s_miik=song8k['Name']
    s_riik=song9k['Name']

  def talk_r(s_rk):
         engine = pyttsx3.init()
         engine.say(s_rk)
         engine.runAndWait()
         def play_songs(s_rk):
             if (s_rk):
              st.write(f"Playing the kdrama: {s_rk}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_rk + "kdrama")
              url=f"https://www.youtube.com/results?search_query={s_rk}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}") 
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
              if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
               return None
              
             else:
                st.write("Please provide a K-Drama name.")
                talk_r("Please provide a K-Drama name.")
        #  play_songs(s_l)
         def play(s_rk):
              url = play_songs(s_rk)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this K-Drama 😢")
         play(s_rk)



  

  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  dfk['combined_features']=dfk['Genre']
  c=cv.fit_transform(dfk['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c)
  import random
# l, m, r = st.columns(3) 
  def recommand(song_name):
    index=dfk[dfk['Name']==song_name].index[0]
    distance1 = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    
    s=[dfk.iloc[i[0]] for i in distance1[1:7]]
#  random.shuffle(s1)
  
    rec = random.sample(s, min(len(s), 7))
    for song in rec: 
#  st.write(s1)
     songs = song['Name']
     poster_url = song['Poster Path']    # ✅ Access poster directly
     st.image(poster_url, width=150)
     st.write(songs)
    
  #sl=s1.sample(n=5)
#  st.write(s1)
  import urllib
  import requests
  def talk_l(s_lk):
        engine = pyttsx3.init()
        engine.say(s_lk)
        engine.runAndWait()
        def play_songs(s_lk):
            if (s_lk):
             st.write(f"Playing the kdrama: {s_lk}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_lk + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_lk}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            else:
              return None
            
           
      #  play_songs(s_l)
        def play(s_lk):
            url = play_songs(s_lk)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this K-Drama 😢")
        play(s_lk)

  def talk_m(s_mk):
        engine = pyttsx3.init()
        engine.say(s_mk)
        engine.runAndWait()
        def play_songs(s_mk):
            if (s_mk):
              st.write(f"Playing the kdrama: {s_mk}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mk + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_mk}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            
            else:
              st.write("Please provide a K-Drama name.")
              talk_m("Please provide a K-Drama name.")
      #  play_songs(s_l)
        def play(s_mk):
            url = play_songs(s_mk)
            if url:
              st.markdown(
                  f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this K-Drama 😢")
        play(s_mk)
  def talk_r(s_rk):
         engine = pyttsx3.init()
         engine.say(s_rk)
         engine.runAndWait()
         def play_songs(s_rk):
             if (s_rk):
              st.write(f"Playing the kdrama: {s_rk}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_rk + "kdrama")
              url=f"https://www.youtube.com/results?search_query={s_rk}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}") 
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
              if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
               return None
              
             else:
                st.write("Please provide a K-Drama name.")
                talk_r("Please provide a K-Drama name.")
        #  play_songs(s_l)
         def play(s_rk):
              url = play_songs(s_rk)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this K-Drama 😢")
         play(s_rk)

# recommand(s_l)      

# 1st column
import random
if 'songs_selected' not in st.session_state:
  st.session_state.songs_selected = random.sample(dfk.to_dict('records'), 9)
  song1k = st.session_state.current_song_leftk
  song2k=st.session_state.current_song_middlek
  song3k=st.session_state.current_song_rightk
  song4k= st.session_state.current_song_lek
  song5k= st.session_state.current_song_mik
  song6k= st.session_state.current_song_rik
  song7k=st.session_state.current_song_leek
  song8k=st.session_state.current_song_miik
  song9k=st.session_state.current_song_riik
  s_lk=song1k['Name']
  s_mk=song2k['Name']
  s_rk=song3k['Name']
  s_lek=song4k['Name']
  s_mik=song5k['Name']
  s_rik=song6k['Name']
  s_leek=song7k['Name']
  s_miik=song8k['Name']
  s_riik=song9k['Name']
  def talk_l(s_lk):
        engine = pyttsx3.init()
        engine.say(s_lk)
        engine.runAndWait()
        def play_songs(s_lk):
            if (s_lk):
             st.write(f"Playing the kdrama: {s_lk}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_lk + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_lk}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            else:
              return None
            
           
      #  play_songs(s_l)
        def play(s_lk):
            url = play_songs(s_lk)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this K-Drama 😢")
        play(s_lk)

  def talk_m(s_mk):
        engine = pyttsx3.init()
        engine.say(s_mk)
        engine.runAndWait()
        def play_songs(s_mk):
            if (s_mk):
              st.write(f"Playing the kdrama: {s_mk}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mk + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_mk}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            
            else:
              st.write("Please provide a K-Drama name.")
              talk_m("Please provide a K-Drama name.")
      #  play_songs(s_l)
        def play(s_mk):
            url = play_songs(s_mk)
            if url:
              st.markdown(
                  f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this K-Drama 😢")
        play(s_mk)
  def talk_r(s_rk):
         engine = pyttsx3.init()
         engine.say(s_rk)
         engine.runAndWait()
         def play_songs(s_rk):
             if (s_rk):
              st.write(f"Playing the kdrama: {s_rk}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_rk + "kdrama")
              url=f"https://www.youtube.com/results?search_query={s_rk}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}") 
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
              if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
               return None
              
             else:
                st.write("Please provide a K-Drama name.")
                talk_r("Please provide a K-Drama name.")
        #  play_songs(s_l)
         def play(s_rk):
              url = play_songs(s_rk)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this K-Drama 😢")
         play(s_rk)
  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  dfk['combined_features']=dfk['Genre']
  c=cv.fit_transform(dfk['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c)
  import random
  def recommand(song_name):
    index=dfk[dfk['Name']==song_name].index[0]
    distance1 = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    
    s=[dfk.iloc[i[0]] for i in distance1[1:7]]
#  random.shuffle(s1)
  
    rec = random.sample(s, min(len(s), 7))
    for song in rec: 
#  st.write(s1)
     songs = song['Name']
     poster_url = song['Poster Path']    # ✅ Access poster directly
     st.image(poster_url, width=150)
     st.write(songs)
  left, middle, right = st.columns(3)              
  left.image(song1k['Poster Path'], width=150)
  with left:
    st.write(s_lk)
    if st.button("▶ Play", key="play_eleft"):
  # v=s_l
      talk_l(s_lk)
#  if st.button("Recommend", key="rec_left"):
      st.subheader("Made For You:")
      recommand(s_lk)   #recommnded songs for left
    
  middle.image(song2k['Poster Path'], width=150)
  with middle:
    st.write(s_mk)
    if st.button("▶ Play", key="play_emiddle"):
  # v=s_l
      talk_m(s_mk)     
      recommand(s_mk)
# if st.button("Recommend", key="rec_middle")  
  right.image(song3k['Poster Path'], width=150)
  with right:
    st.write(s_rk)
    if st.button("▶ Play", key="play_eright"):
  # v=s_l
     talk_r(s_rk)
     recommand(s_rk)
  
# 2 layout columns 
  import requests
  def talk_le(s_lek):
        engine = pyttsx3.init()
        engine.say(s_lek)
        engine.runAndWait()
        def play_songs(s_lek):
            if (s_lek):
             st.write(f"Playing the kdrama: {s_lek}")
            query = urllib.parse.quote(s_lek + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_lek}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a K-Drama name.")
              talk_le("Please provide a K-Drama name.")
      #  play_songs(s_l)
        def play(s_lek):
            url = play_songs(s_lek)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this K-Drama 😢")
        play(s_lek)


  def talk_mi(s_mik):
        engine = pyttsx3.init()
        engine.say(s_mik)
        engine.runAndWait()
        def play_songs(s_mik):
            if (s_mik):
             st.write(f"Playing the kdrama: {s_mik}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mik + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_mik}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a K-Drama name.")
              talk_mi("Please provide a K-Drama name.")
      #  play_songs(s_l)
        def play(s_mik):
            url = play_songs(s_mik)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this K-Drama 😢")
        play(s_mik)
  import urllib
  def talk_ri(s_rik):
        engine = pyttsx3.init()
        engine.say(s_rik)
        engine.runAndWait()
        def play_songs(s_rik):
            if (s_rik):
             st.write(f"Playing the kdrama: {s_rik}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_rik + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_rik}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a K-Drama name.")
              talk_r("Please provide a K-Drama name.")
      #  play_songs(s_l)
        def play(s_rik):
            url = play_songs(s_rik)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this K-Drama 😢")
        play(s_rik)

# Left Column - Fixed Song. 2nd column
  le, mi, ri = st.columns(3)
  with le:
   song4= st.session_state.current_song_lek
   st.image(song4['Poster Path'], width=150)
   st.write(song4['Name'])
   if st.button("▶ Play", key="play_ele"):
      talk_le(s_lek)
      recommand(s_lek)
  
# Middle Column - Fixed Song 2
  with mi:
    song5 = st.session_state.current_song_mik
    st.image(song5['Poster Path'], width=150)
    st.write(song5['Name'])
    if st.button("▶ Play", key="play_emi"):
      talk_mi(s_mik)
      recommand(s_mik)
      

# Right Column - "Now Playing" Section
  with ri:
    song6 = st.session_state.current_song_rik
    st.image(song6['Poster Path'], width=150)
    st.write(song6['Name'])
    if st.button("▶ Play", key="play_eri"):
      talk_ri(s_rik)
      recommand(s_rik)
      
      # 3rd row
  lee, mii, rii = st.columns(3)
  def talk_lee(s_leek):
        engine = pyttsx3.init()
        engine.say(s_leek)
        engine.runAndWait()
        def play_songs(s_leek):
            if (s_leek):
             st.write(f"Playing the kdrama: {s_leek}")
            query = urllib.parse.quote(s_mik + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_leek}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a K-Drama name.")
              talk_lee("Please provide a K-Drama name.")
      #  play_songs_l)
        def play(s_leek):
            url = play_songs(s_leek)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this kdrama 😢")
        play(s_leek)
  def talk_mii(s_miik):
        engine = pyttsx3.init()
        engine.say(s_miik)
        engine.runAndWait()
        def play_songs(s_miik):
            if (s_miik):
             st.write(f"Playing the kdrama: {s_miik}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_miik + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_miik}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a K-Drama name.")
              talk_mii("Please provide a K-Drama name.")
      #  play_songs(s_l)
        def play(s_miik):
            url = play_songs(s_miik)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this K-Drama 😢")
        play(s_miik)
  def talk_rii(s_riik):
        engine = pyttsx3.init()
        engine.say(s_riik)
        engine.runAndWait()
        def play_songs(s_riik):
            if (s_riik):
             st.write(f"Playing the kdrama: {s_riik}")
            
            
            query = urllib.parse.quote(s_riik + "kdrama")
            url=f"https://www.youtube.com/results?search_query={s_riik}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a K-Drama name.")
              talk_rii("Please provide a K-Drama name.")
      #  play_songs(s_l)
        def play(s_riik):
            url = play_songs(s_riik)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this K-Drama 😢")
        play(s_riik)
# Left Column - Fixed Song 1
  with lee:
    song7= st.session_state.current_song_leek
    st.image(song7['Poster Path'], width=150)
    st.write(song7['Name'])
    if st.button("▶ Play", key="play_elee"):
      talk_lee(s_leek)
      recommand(s_leek)
# Middle Column - Fixed Song 2
  with mii:
    song8 = st.session_state.current_song_miik
    st.image(song8['Poster Path'], width=150)
    st.write(song8['Name'])
    if st.button("▶ Play", key="play_emii"):
      talk_mii(s_miik)
      recommand(s_miik)

# Right Column - "Now Playing" Section
  with rii:
    song9 = st.session_state.current_song_riik
    st.image(song9['Poster Path'], width=150)
    st.write(song9['Name'])
    if st.button("▶ Play", key="play_erii"):
      talk_rii(s_riik)
      recommand(s_riik)
show()                                     