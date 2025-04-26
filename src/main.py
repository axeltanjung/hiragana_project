import streamlit as st
import json
import os
import dictionary as dictionary
import kanji as kanji

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, 'alphabet_to_hiragana.json')

# Load the dictionary mapping English alphabet to Hiragana from a JSON file
with open(json_path, 'r', encoding='utf-8') as f:
    alphabet_to_hiragana = json.load(f)

def convert_to_hiragana(text):
    hiragana_text = ""
    i = 0
    while i < len(text):
        # Check for 2-character and 3-character combinations first
        if i + 1 < len(text) and text[i:i+2].lower() in alphabet_to_hiragana:
            hiragana_text += alphabet_to_hiragana[text[i:i+2].lower()]
            i += 2
        elif i + 2 < len(text) and text[i:i+3].lower() in alphabet_to_hiragana:
            hiragana_text += alphabet_to_hiragana[text[i:i+3].lower()]
            i += 3
        # Otherwise check for 1-character mapping
        elif text[i].lower() in alphabet_to_hiragana:
            hiragana_text += alphabet_to_hiragana[text[i].lower()]
            i += 1
        else:
            # If no match, add the character as is (e.g., for non-matching characters like spaces or punctuation)
            hiragana_text += text[i]
            i += 1
    return hiragana_text

if __name__ == "__main__":
    st.title("Japanese Learning Tools")

    st.sidebar.title("Features")
    feature = st.sidebar.selectbox("Select a feature", [
        "Dictionary",
        "Kanji Learning"
    ])

    if feature == "Dictionary":
        dictionary.dictionary()
    elif feature == "Kanji Learning":
        kanji.kanji()
