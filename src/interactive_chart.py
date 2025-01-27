import streamlit as st
import json

# Load the dictionary mapping English alphabet to Hiragana from a JSON file
with open('alphabet_to_hiragana.json', 'r', encoding='utf-8') as f:
    alphabet_to_hiragana = json.load(f)

def interactive_chart():
    st.subheader("Interactive Hiragana Chart")
    for romaji, hiragana in alphabet_to_hiragana.items():
        st.write(f"{romaji}: {hiragana}")