#####################################################
# Imports
#####################################################
import streamlit as st
import pandas as pd
import numpy as np
from api_connector import get_response, build_prompt, rand_choice

#####################################################
# Customising CSS
#####################################################
custom_css = """
    <style>

        [data-testid="stAppViewContainer"] {
            background: #2A3D66;
            color: #D1D1D1;
        }

        h1 {
            text-align: center;
            border-bottom: 3px solid #D1D1D1; 
        }        
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

#####################################################
# Adding Streamlit Elements
#####################################################

st.title('🎄 Christmas Story Generator 🎄')

st.write('\n')

st.markdown('#### 🎬 Set the Scene ...')

st.write('You can either provide your own inputs or click Surprise Me for randomly choosen inputs.')

# button to randomly pick inputs using rand_choice()
# using session_state to set values in text_input elements
if st.button(label ='🎲 Surprise Me!',use_container_width=True):
    st.session_state.char_type = rand_choice()[0]
    st.session_state.genre = rand_choice()[1]
    st.session_state.location = rand_choice()[2]
    st.session_state.theme = rand_choice()[3]

character_type = st.text_input(label = 'Character Type', placeholder = 'Like Elf, Santa, Reindeer, Snowman, etc.',key='char_type' )

story_genre = st.selectbox( 'Genre',
                           ('Comedy', 'Action', 'Fantasy', 'Horror', 'Romance', 'Sci-Fi', 'Mystery'),
                           placeholder = 'Select a Genre', 
                           key= 'genre',
                           index = None # to get placeholder text to show
                           )

location = st.text_input(label = 'Location', placeholder = 'Like Lapland, North Pole, London',key='location' )

theme = st.text_input(label = 'Theme', placeholder = 'Like giving, kindness, togetherness',key='theme' )

story_length = st.slider('Story Length ', min_value = 300, max_value = 1000, step = 100, format='%d words', value = 500, key='story_length' )

if st.button(label = '✨ Write My Story!',use_container_width=True):

    st.subheader('Story:')
    # making character type and story_genre mandatory inputs to create story
    if not character_type:
        st.error('Please enter a character type')
    elif not story_genre:
        st.error('Please enter a genre')

    else:

        # Adding spinner to show user story is generating 
        with st.spinner('Generating, please wait...'):

            # adding snow for some festive fun
            st.snow()
            # calling build_prompt to generate prompt from given inputs
            my_prompt = build_prompt(character_type,story_genre, location, theme)
            # to get response from model
            my_story = get_response(my_prompt,story_length)
            # display output(story) 
            st.write(my_story)

            # button for user to download story, file to be saved as my_generated_story.txt in downloads
            st.download_button('Download your story 📥', my_story, file_name = 'my_generated_story.txt')
