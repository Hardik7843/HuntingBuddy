import streamlit as st
import pandas as pd
from PIL import Image
import spacy
from collections import defaultdict
import re
from pandas import json_normalize

nlp = spacy.load("model")
logo = Image.open(r"logo.jpg")
page_config = {"page_title": "Hunting Buddy", "page_icon": logo , "layout":"wide"}
st.set_page_config(**page_config)


def examine(raw_text):
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', raw_text)
    doc = nlp(text)
    out =  defaultdict(list)
    for w in doc.ents:
        out[w.label_].append(w.text)
    
    for skill in out.keys():
        # Removing the duplicates in output for each skills
        out[skill] = list(set(out[skill]))
    
    df = pd.json_normalize(out)
    st.dataframe(df, use_container_width = True)


button_key = 1
st.title("Hunting Buddy!🔍")

st.header("")

text = st.text_area("Input" , placeholder = "Feed me Job description which you want to examine!" , label_visibility="collapsed")

click = st.button(":blue[Examine]" )

if click:
    examine(text)


