import streamlit as st
from langchain_helper import generate_restaurant_name_and_menu_items
st.title("Restaurant Name Generator")

cusine = st.sidebar.selectbox("Select the type of restaurant", ["Italian", "Mexican", "Chinese", "Japanese", "Indian", "French", "Greek", "Spanish", "Thai", "Lebanese", "Turkish", "Korean", "Vietnamese", "Indonesian", "Malaysian", "Singaporean", "Australian", "New Zealand", "Canadian", "American", "Brazilian", "Argentinian", "Chilean", "Peruvian", "Colombian", "Ecuadorian", "Bolivian", "Paraguayan", "Uruguayan", "Chilean", "Peruvian", "Colombian", "Ecuadorian", "Bolivian", "Paraguayan", "Uruguayan"])

if cusine:
    response = generate_restaurant_name_and_menu_items(cusine)
    restaurant_name = response["restaurant_name"]
    menu_items = response["menu_items"]

    st.header(restaurant_name)

    st.write("Menu Items:")
    st.write(menu_items)
            
else:
    st.write("Please select a cuisine")
