import streamlit as st

st.title('My parents new healthy diner')
st.header('Breakfast Menu')
st.text('🥓Full English')
st.text('🍟Bread Butty')

st.header('🍌🥝Build your own smoothies🍍🍑')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(df, 200, 100)
st.dataframe(my_fruit_list)
