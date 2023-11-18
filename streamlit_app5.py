import streamlit as st
import seaborn as sns

df = sns.load_dataset('penguins')
st.header('Penguins')
st.write(df)