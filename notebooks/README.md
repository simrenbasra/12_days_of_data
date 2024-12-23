# Notebooks Overview

## 01_set_up
- `.env`: hidden file containing my API key. I am using environment variables to keep the API key hidden (common practice when working with APIs)
- `playground.ipynb`: Notebook where I experiemented connecting to the API chat completion endpoint and receiving responses.

## 02_streamlit
- `api_connector.py`: Connects to the API and includes three functions:
    -`rand_choice` to randomly set inputs, to be called if user presses a button.
    - `build prompt` to build prompts based on user inputs from Streamlit.
    - `get_response` to pass prompts to API a and retrieve output from GPT.
    - both functions are called in `app.py`
- `app.py`: Streamlit app where I capture user inputs and display GPT outputs using the functions in `api_connector.py`.