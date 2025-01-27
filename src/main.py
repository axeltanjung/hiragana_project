import streamlit as st
import json
import flashcards as flashcards
import quizzes as quizzes
import interactive_chart as interactive_chart
import pronunciation_guides as pronunciation_guides

# Load the dictionary mapping English alphabet to Hiragana from a JSON file
with open('alphabet_to_hiragana.json', 'r', encoding='utf-8') as f:
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
    st.title("English to Hiragana Converter")

    input_text = st.text_input("Enter text to convert to Hiragana:")
    if st.button("Convert"):
        if input_text:
            hiragana_text = convert_to_hiragana(input_text)
            st.write("Hiragana: ", hiragana_text)

    st.sidebar.title("Features")
    feature = st.sidebar.selectbox("Select a feature", ["Interactive Hiragana Chart", "Flashcards", "Quizzes", "Pronunciation Guides"])

    if feature == "Interactive Hiragana Chart":
        interactive_chart.interactive_chart()
    elif feature == "Flashcards":
        flashcards.flashcards()
    elif feature == "Quizzes":
        quizzes.quizzes()
    elif feature == "Pronunciation Guides":
        pass
        # pronunciation_guides.pronunciation_guides()
