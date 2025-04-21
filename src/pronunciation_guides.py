import streamlit as st
import json

# Load the dictionary mapping English alphabet to Hiragana from a JSON file
with open('alphabet_to_hiragana.json', 'r', encoding='utf-8') as f:
    alphabet_to_hiragana = json.load(f)
    # Function to display pronunciation guide
    def display_pronunciation_guide():
        st.title("Hiragana Pronunciation Guide")
        
        for letter, hiragana in alphabet_to_hiragana.items():
            if st.button(letter):
                st.write(f"The Hiragana for {letter} is {hiragana}")

    # Call the function to display the guide
    display_pronunciation_guide()