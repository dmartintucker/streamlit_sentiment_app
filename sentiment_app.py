# Dependencies
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer object
sia = SentimentIntensityAnalyzer()

# Initialize state properties to keep track of
st.session_state['text_to_analyze'] = None
st.session_state['sent_scores'] = None

def run_calculation() -> dict:
    sent_scores = sia.polarity_scores(st.session_state['text_to_analyze'])
    return sent_scores

# Content to be rendered
st.title('Sentiment Analyzer')

user_input = st.text_input(value='', label='Enter the text you want to analyze here.')
handle_user_input = st.button('Analyze')

if handle_user_input:
    st.session_state['text_to_analyze'] = user_input
    st.session_state['sent_scores'] = run_calculation()

if (st.session_state['sent_scores'] == None):
    st.write('Enter some text to compute its sentiment.')
else:
    st.write(st.session_state['sent_scores'])
