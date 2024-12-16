import streamlit as st
import pandas as pd
import numpy as np
from api_connector import get_response, build_prompt
import time 

st.title('Generate your own Christmas Story!')

st.subheader('Inputs')

character_type = st.text_input(label = 'Character Type', placeholder = 'Like Elf, Santa, Reindeer, Snowman, etc.', )

story_genre = st.selectbox( 'Genre',
                           ('Comedy', 'Action', 'Fantasy', 'Horror', 'Romance', 'Sci-Fi', 'Mystery'),
                           placeholder = 'Select a Genre', 
                           index = None # to get placeholder text to show
                           )

story_length = st.slider('Story Length ', min_value = 300, max_value = 1000, step = 100, format='%d words', value = 500)

if st.button(label = 'Generate Story'):

    st.subheader('Story:')

    if not character_type:
        st.error('Please enter a character type')
    elif not story_genre:
        st.error('Please enter a genre')
    else:
        with st.spinner('Generating, please wait...'):
            st.snow()

            my_prompt = build_prompt(character_type,story_genre)

            my_story = get_response(my_prompt,story_length)

            st.write(my_story)

            # Button for user to download story
            st.download_button('Download your story 📥', my_story, file_name = 'my_generated_story.txt')
