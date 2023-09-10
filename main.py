import streamlit as st

st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_2725.png")

with col2:
    st.title("Jason Widjaja")
    content = """
    Hi, my name is Jason Widjaja.. (ADD MORE STUFF HERE)
    """
    st.info(content)
