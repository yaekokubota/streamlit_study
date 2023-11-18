import streamlit as st
import random
omikuji = ['大吉', '中吉', '小吉', '凶']
if st.button('おみくじ'):
    o = random.choice(omikuji)
    st.write(o)