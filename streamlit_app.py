# Imports -----------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

#Functions -----------------------------------------------------------------------------------------------------
def get_fruity_juice_data(fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  # Flatten with header
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())  
  return fruityvice_normalized

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
  
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("Insert into fruit_load_list values ('" + new_fruit + "')")
    return "Thanks for adding " + new_fruit

#Body -----------------------------------------------------------------------------------------------------
def get_fruity_juice_data(fruit_choice):
st.title('My parents new healthy diner')
st.header('Breakfast Menu')
st.text('🥓Full English')
st.text('🍟Bread Butty')

st.header('🍌🥝Build your own smoothies🍍🍑')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.table(fruits_to_show)

st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
     st.error("Please select a fruit to get information")
  else:
    st.write('The user entered ', fruit_choice)
    back_from_function = get_fruity_juice_data(fruit_choice)
    # Write to table
    st.dataframe(back_from_function)
except URLError as e:
  st.error()

add_my_fruit = st.text_input('What fruit would you like to add?')  

# Add a button to load the fruit
if st.button('Add a fruit to the list"'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  st.text(back_from_function)

#-------------------------------------------------------------------------------------------------------
# My deduced If stmt alternative
# add_my_fruit = st.text_input('What fruit would you like to add?')
# if add_my_fruit != "": 
#  my_cur.execute("insert into fruit_load_list select '" + add_my_fruit + "'")
#  st.text("Thanks for adding " + add_my_fruit)
#  my_cur.execute("select * from fruit_load_list")
#  my_data_row =  my_cur.fetchall()
#  st.header("Fruit List Contains:")
#  st.dataframe(my_data_row)
#-------------------------------------------------------------------------------------------------------





