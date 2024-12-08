import streamlit as st
import pandas as pd
import gtts
import random
from PIL import Image

def ask():
    st.session_state.prob=prob=random.choice(st.session_state.qL)
    
    msg=f"What is the capital of {prob}?:"
    st.text_input(msg,'',key='inp',on_change=check)

def check():

            prob=st.session_state.prob
            inp=st.session_state.inp
            ans=st.session_state.D[prob]["Capital"]
            msg=f"Congraturation!{inp}is the capital of {prob}"
            if inp.lower()!=ans.lower():
                msg=f"Are you stupid.It is {ans}, not {inp}"
            else:
                st.session_state.point +=1
                st.write(msg)
                st.write(f"Point is {st.session_state.point}")
                st.button("Next",on_click=ask)
if not "idx" in st.session_state:
    file = "Countrylist.xlsx"
    df=pd.read_excel(file,index_col="Country")[:10]
    st.session_state.D=D=df.to_dict(orient="index")
    st.session_state.qL=list(D)
    st.session_state.idx=st.session_state.point=0
    
    ask()
                
            
     