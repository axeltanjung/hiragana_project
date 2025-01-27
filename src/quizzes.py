import streamlit as st
import json

# Load the dictionary mapping English alphabet to Hiragana from a JSON file
with open('alphabet_to_hiragana.json', 'r', encoding='utf-8') as f:
    alphabet_to_hiragana = json.load(f)

def quizzes():
    st.subheader("Quizzes to Test Knowledge")
    import random
    romaji, hiragana = random.choice(list(alphabet_to_hiragana.items()))
    user_answer = st.text_input(f"What is the Hiragana for {romaji}?")
    if st.button("Submit Answer"):
        if user_answer == hiragana:
            st.write("Correct!")
        else:
            st.write(f"Incorrect. The correct answer is {hiragana}")