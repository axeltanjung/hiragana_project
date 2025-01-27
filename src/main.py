import streamlit as st

# /D:/project/hiragana_project/src/main.py

# Dictionary mapping English alphabet to Hiragana
alphabet_to_hiragana = {
    # Additional single characters
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'wa': 'わ', 'wo': 'を',
    'n': 'ん',

    # Diacritical marks (Dakuten and Handakuten)
    'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
    'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
    'da': 'だ', 'ji': 'ぢ', 'zu': 'づ', 'de': 'で', 'do': 'ど',
    'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',

    # Modified sounds (Yōon - combinations with 'ya', 'yu', 'yo')
    'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
    'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
    'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ',
    'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',
    'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
    'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',
    'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',
    'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',
    'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
    'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
    'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',

    # Other Yōon Combinations (Wago/Loanwords)
    'wa': 'わ', 'wi': 'うぃ', 'we': 'うぇ', 'wo': 'を',
    'vu': 'ゔ', 've': 'ゔぇ', 'vi': 'ゔぃ',
    'si': 'し', 'ti': 'ち', 'di': 'ぢ',
    'chi': 'ち', 'tsu': 'つ', 'tu': 'つ',

    'a': 'あ', 'e': 'え', 'i': 'い', 'o': 'お', 'u': 'う'
}


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
