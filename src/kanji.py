import streamlit as st
import requests
import json

def get_kanji_info(kanji, direction="japanese_to_english"):
    # Using Kanji API for kanji information
    url = f"https://kanjiapi.dev/v1/kanji/{kanji}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        st.error(f"Error fetching kanji data: {str(e)}")
        return None

def display_kanji_info(kanji_data, direction):
    if not kanji_data:
        st.write("No results found.")
        return

    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Kanji:**")
        st.write(f"# {kanji_data['kanji']}")
        st.write(f"**Stroke Count:** {kanji_data['stroke_count']}")
        
        if 'meanings' in kanji_data:
            st.write("**Meanings:**")
            for meaning in kanji_data['meanings']:
                st.write(f"- {meaning}")
    
    with col2:
        if 'kun_readings' in kanji_data:
            st.write("**Kun Readings:**")
            for reading in kanji_data['kun_readings']:
                st.write(f"- {reading}")
        
        if 'on_readings' in kanji_data:
            st.write("**On Readings:**")
            for reading in kanji_data['on_readings']:
                st.write(f"- {reading}")

def kanji():
    st.title("Kanji Learning")
    
    # Add direction selection
    direction = st.radio(
        "Select translation direction:",
        ["Japanese to English", "English to Japanese"]
    )
    
    if direction == "Japanese to English":
        search_kanji = st.text_input("Enter a kanji character to learn about:")
        if st.button("Search"):
            if search_kanji:
                with st.spinner("Searching..."):
                    results = get_kanji_info(search_kanji, "japanese_to_english")
                    display_kanji_info(results, "japanese_to_english")
            else:
                st.warning("Please enter a kanji character to search.")
    else:
        search_meaning = st.text_input("Enter an English meaning to find kanji:")
        if st.button("Search"):
            if search_meaning:
                with st.spinner("Searching..."):
                    # For English to Japanese, we'll search for kanji that have the meaning
                    results = get_kanji_info(search_meaning, "english_to_japanese")
                    display_kanji_info(results, "english_to_japanese")
            else:
                st.warning("Please enter a meaning to search.") 