import streamlit as st
import artff
import newsai
import game
import home1
# st.set_page_config(page_title="VibeVerse", layout="centered")
if 'art_button_clicked' not in st.session_state:
    st.session_state.art_button_clicked=False
    st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPGbkh6S2HheJSRJ3NQVzd971XyRPdOWfpow&s');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100vh;
    }

    
    </style>
    """, unsafe_allow_html=True)
 

st.markdown("""
    <style>
    /* Custom button styling */
    .custom-button {
        background-color: #ffcc70;
        color: white;
        font-weight: bold;
        border: 2px solid #ffa500;
        border-radius: 12px;
        padding: 1em 2em; /* Larger padding for bigger button */
        margin: 10px 5px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 100px; /* Set font size to 50px */
    }
    .custom-button:hover {
        background-color: #ff9900;
        color: white;
        box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
    }
    /* Streamlit button styling */
    div.stButton > button:first-child {
        background-color: #66a5ed;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 60px 80px; /* Larger padding for bigger button */
        margin: 5px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        font-size: 100px; /* Increase font size for larger text */
        width: 300px;
        height: 200px;
    }
    div.stButton > button:first-child:hover {
        background-color: #062447;
        color: white;
        box-shadow: 0 0 15px #86a0bf, 0 0 25px #86a0bf, 0 0 35px #86a0bf;
    }
    .st-emotion-cache-atejua egexzqm0>{
      font-size:100px;
            }
    </style>
""", unsafe_allow_html=True)

for key in ["art_button_clicked", "entertainment_button_clicked", "game_button_clicked", "news_button_clicked"]:
    if key not in st.session_state:
        st.session_state[key] = False

# Main screen: show 4 buttons if no section is active
if not any([
    st.session_state.art_button_clicked,
    st.session_state.entertainment_button_clicked,
    st.session_state.game_button_clicked,
    st.session_state.news_button_clicked
]):
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Dreamify"):
            st.session_state.art_button_clicked = True
        if st.button("PowerPlayAI"):
            st.session_state.game_button_clicked = True
    with col2:
        if st.button("SceneSync"):
            st.session_state.entertainment_button_clicked = True
        if st.button("Flashly"):
            st.session_state.news_button_clicked = True
# Art Section
if st.session_state.art_button_clicked:
    st.header("Art Corner")
    artff.show()  # Your art logic here
if st.button("Back", key="back_art"):
        st.session_state.art_button_clicked = False
# Entertainment Section
elif st.session_state.entertainment_button_clicked:
    home1.show()
    if st.button("Back", key="back_enter"):
        st.session_state.entertainment_button_clicked = False
# Game Section
elif st.session_state.game_button_clicked:
    game.show()
    if st.button("Back", key="back_game"):
        st.session_state.game_button_clicked = False
# News Section
elif st.session_state.news_button_clicked:
    st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.google.com/imgres?q=news%20images&imgurl=https%3A%2F%2Fplus.unsplash.com%2Fpremium_photo-1688561384438-bfa9273e2c00%3Ffm%3Djpg%26q%3D60%26w%3D3000%26ixlib%3Drb-4.0.3%26ixid%3DM3wxMjA3fDB8MHxzZWFyY2h8MXx8bmV3c3xlbnwwfHwwfHx8MA%253D%253D&imgrefurl=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fnews&docid=9GEcrP2J-MjsjM&tbnid=zdMzR3gP9RVyjM&vet=12ahUKEwjViuD75PiMAxX1R2wGHRCtLEoQM3oECH4QAA..i&w=3000&h=2000&hcb=2&ved=2ahUKEwjViuD75PiMAxX1R2wGHRCtLEoQM3oECH4QAA');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)
    newsai.show()

if st.button("Back", key="back_news"):
        st.session_state.news_button_clicked = False




