import streamlit as st
import json

# Load the dictionary mapping English alphabet to Hiragana from a JSON file
with open('alphabet_to_hiragana.json', 'r', encoding='utf-8') as f:
    alphabet_to_hiragana = json.load(f)

def flashcards():
    st.subheader("Flashcards for Practice")
    import random
    romaji, hiragana = random.choice(list(alphabet_to_hiragana.items()))
    st.write(f"What is the Hiragana for {romaji}?")
    if st.button("Show Answer"):
        st.write(f"The Hiragana for {romaji} is {hiragana}")