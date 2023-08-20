# streamlit_sentiment_app

This written tutorial is intended to accompany a tutorial created in August 2023 entitle `How to Build A Sentiment Analyzer App with Python & Streamlit`.

To follow along, you'll need:
1. Terminal (MacOS), PowerShell (Windows), or any other interactive console of your choice
2. A text editor or IDE. I recommend VSCode
3. A web browser for interacting with the app

## Setup

### Getting Python 3.11

This tutorial assumes you have python on Windows/Linux/MacOS system. I'll be running this on 3.11.4

[Download Python 3.11.4](https://www.python.org/downloads/)

or if you're on macOS and using `homebrew`, simply run the following command in Terminal:
```
brew install python@3.11.4
```

### Environment and packages

We'll be making use of 2 packages here: `streamlit` (for building the app) and `nltk` for the sentiment analyzer.

I recommend using a virtual environment such as `poetry`, `pipenv`, `conda`, etc. 

If not, you can simply install the package dependencies with:
```
pip install streamlit nltk
```

If this does not work, you may need to use the `pip3` command:
```
pip3 install streamlit nltk
```

Finally, you'll need to use `nltk` to download the `vader_lexicon`, a dependency of the sentiment analyzer we'll be using in the app.
```
nltk.download('vader-lexicon')
```

And at this point, we should be good to go! As a quick check, we can run `streamlit hello` to verify streamlit installed as expected.

## Building and testing the app

Let's open our code editor and create a file in our current directory and call it `sentiment_app.py`.

```
# Dependencies
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
```

Next, we'll create an instance of the sentiment analyzer object, which will allow us to call it downstream.

```
# Create a callable instance of the sentiment analyzer object
sia = SentimentIntensityAnalyzer()
```
