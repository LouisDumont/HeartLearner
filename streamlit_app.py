import time

import numpy as np
import pandas as pd
import streamlit as st

from df_iterator import DfIterator


# TODO:
# - select a specific file from the preloaded one, or load your own
# - select a range of rows on which to iterate (modify loader class too)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")

st.title('Heart Learner')

ex_path = f'preloaded_documents/Vocabulary.ods'
ex_df = pd.read_excel(ex_path)
df_iterator = DfIterator(ex_df, cols=['English', 'French'])


def question_as_str(df_sample, language="english"):
    category_to_predict = df_sample[1][0]
    value = df_sample[0][1]

    if language == "english":
        # TODO: use css to highlight the value
        return f'<h2>What is the <div class="question">{category_to_predict}</div> for <div class="highlight">\"{value}\"</div>?</h2>'


def answer_as_str(df_sample, language="english"):
    answer = df_sample[1][1]
    return f'<h2>Answer: <div class="highlight">{answer}</div></h2>'


def handle_new_question(holder, iterator, wait):
    holder.empty()
    question = iterator.sample_question()
    holder.markdown(question_as_str(question), unsafe_allow_html=True)
    time.sleep(wait)
    holder.markdown(answer_as_str(question), unsafe_allow_html=True)


auto_mode = st.sidebar.checkbox("Use automatic mode?")
slider = st.sidebar.slider("Time before answer", 3, 10, 5)

if auto_mode:
    question_holder = st.empty()

    while True:
        handle_new_question(question_holder, df_iterator, slider)
        time.sleep(5)

else:
    button = st.empty()
    button.button('next')

    question_holder = st.empty()

    if button:
        handle_new_question(question_holder, df_iterator, slider)
