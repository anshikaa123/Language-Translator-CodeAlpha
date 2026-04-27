import streamlit as st
from deep_translator import GoogleTranslator

# Page Setup
st.set_page_config(page_title="AI Language Translator", page_icon="🌍")
st.title("🌍 Global AI Language Translator")

# Translator load karna
translator = GoogleTranslator()

# Sabhi languages ki list nikalna
try:
    langs_dict = translator.get_supported_languages(as_dict=True)
    lang_names = list(langs_dict.keys())
except:
    st.error("Please check your internet connection.")
    st.stop()

# User Input
text_input = st.text_area("Enter text to translate:", height=150, placeholder="Type something here...")

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("From (Source):", options=['auto'] + lang_names)
with col2:
    # Default target language English ya Hindi select kar sakte hain
    dest_lang = st.selectbox("To (Target):", options=lang_names, index=lang_names.index('hindi') if 'hindi' in lang_names else 0)

if st.button("Translate Now"):
    if text_input.strip():
        try:
            # Translation process
            translated = GoogleTranslator(source=src_lang, target=langs_dict[dest_lang]).translate(text_input)
            st.markdown("---")
            st.subheader(f"Result ({dest_lang.title()}):")
            st.success(translated)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text first.")

st.markdown("---")
st.caption("Internship Task | Developed by CodeAlpha Intern")