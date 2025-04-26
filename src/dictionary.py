import streamlit as st
import requests
import json

def dictionary_lookup(word, direction="japanese_to_english"):
    # Using Jisho API for dictionary lookup
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['data']
        return None
    except Exception as e:
        st.error(f"Error fetching dictionary data: {str(e)}")
        return None

def display_word_info(word_data, direction):
    if not word_data:
        st.write("No results found.")
        return

    for entry in word_data[:3]:  # Show top 3 results
        with st.expander(f"{entry['japanese'][0]['word']} ({entry['japanese'][0]['reading']})"):
            # Display meanings
            st.write("**Meanings:**")
            for meaning in entry['senses']:
                st.write(f"- {', '.join(meaning['english_definitions'])}")
            
            # Display example sentences if available
            if 'examples' in entry:
                st.write("**Example Sentences:**")
                for example in entry['examples'][:2]:
                    st.write(f"- {example['text']}")
                    st.write(f"  {example['translation']}")

def dictionary():
    st.title("Japanese-English Dictionary")
    
    # Add direction selection
    direction = st.radio(
        "Select translation direction:",
        ["Japanese to English", "English to Japanese"]
    )
    
    if direction == "Japanese to English":
        search_word = st.text_input("Enter a Japanese word to look up:")
        if st.button("Search"):
            if search_word:
                with st.spinner("Searching..."):
                    results = dictionary_lookup(search_word, "japanese_to_english")
                    display_word_info(results, "japanese_to_english")
            else:
                st.warning("Please enter a word to search.")
    else:
        search_word = st.text_input("Enter an English word to look up:")
        if st.button("Search"):
            if search_word:
                with st.spinner("Searching..."):
                    results = dictionary_lookup(search_word, "english_to_japanese")
                    display_word_info(results, "english_to_japanese")
            else:
                st.warning("Please enter a word to search.") 