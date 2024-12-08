import streamlit as st
import pandas as pd
import gtts
import random
frame="sound.mp3"

def speaktext(txt,lang="en"):
    gtts.gTTS(txt).save(frame)
    st.audio(frame)

def ask():
    st.session_state.prob = prob = random.choice(st.session_state.qL)
    msg = f"What is the capital of {prob}? "
    speaktext(msg)
    st.text_input(msg,'',key="inp", on_change=check)
def check():
    """
    Checks the user's input against the correct answer and provides feedback.
    Updates session state variables (point) and displays the next question button.
    """
    prob = st.session_state.prob
    inp = st.session_state.inp.lower() # Ensure case-insensitive comparison
    ans = st.session_state.D[prob]["Capital"].lower()  # Ensure case-insensitive comparison
    st.session_state.idx +=1
    msg = f"Are you fuckin' stupid? The capital of {prob} is {ans} lol."
    if inp.lower() == ans.lower():
        msg = f"Congratulations! {inp} is the capital of {prob}."
        st.session_state.point+=1
    st.write(msg)
    speaktext(msg)
    st.write(f"Point is {st.session_state.point}")
    st.button("Next", on_click=ask)

if "idx" not in st.session_state:
    """
    Answer the following question.I hope you can do it!
    """
    file = "Countrylist.xlsx"
    df = pd.read_excel(file, index_col="Country")
    st.session_state.D = D = df.to_dict(orient="index")
    st.session_state.qL = list(D)
    st.session_state.idx = st.session_state.point = 0

    ask()  # Call the ask function to begin the quiz

