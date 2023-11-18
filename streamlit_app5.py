import streamlit as st
b0 = st.button('松')
b1 = st.button('竹')
b2 = st.button('梅')
# st.write('コースを選んでください')
if b0:
    st.write('2500円')
elif b1:
    st.write('2000円')
elif b2:
    st.write('1500円')
else:
    st.write('コースを選んでください')