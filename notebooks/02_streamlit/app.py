import streamlit as st
import pandas as pd
import numpy as np
from api_connector import get_response, build_prompt

st.title('Generate your own Christmas Story!')

st.header('Inputs')

character_type = st.text_input(label = 'Character Type', placeholder = 'Elf')

story_genre = st.text_input(label = 'Genre', placeholder = 'Comedy')


if st.button(label = 'Generate Story'):

    st.subheader('Story:')

    my_prompt = build_prompt(character_type,story_genre)

    my_story = get_response(my_prompt)

    st.write(my_story)

    # Button for user to download story
    st.download_button("Download your story!", my_story)
