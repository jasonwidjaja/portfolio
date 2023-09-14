import streamlit as st
import pandas

st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_2725.png")

with col2:
    st.title("Jason Widjaja")
    content = """
    Hello, my name is Jason Widjaja and I'm currently a third year Mechanical 
    Engineering major with a concentration in Robotics. Throughout my tenure at 
    Northeastern, I've had the pleasure of being part of clubs such as NU SEDS,
    Electric Racing, and now Generate which have taught me invaluable skills to 
    becoming a better engineer. 
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
