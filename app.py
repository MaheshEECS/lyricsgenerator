import streamlit as st
import google.generativeai as genai
import configparser
from google.generativeai.types import HarmCategory, HarmBlockThreshold

def get_api_key(config_path='config.ini'):
    """Reads the API key from a configuration file."""
    config = configparser.ConfigParser()
    config.read(config_path)
    return config['DEFAULT']['API_KEY']

api_key = get_api_key()

def extract_subtext(text, start_marker="[[", end_marker="]]"):
    """Extracts a substring between a start and end marker."""
    start_index = text.find(start_marker)
    end_index = text.find(end_marker, start_index + len(start_marker))
    
    if start_index != -1 and end_index != -1:
        return text[start_index + len(start_marker):end_index]
    
    return text  # Return the full text if markers are not found

st.set_page_config(page_title="Lyrics Writing Bot", page_icon=":robot_face:", layout="wide")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

def role_to_streamlit(role):
    """Maps a role to a Streamlit role."""
    return "assistant" if role == "model" else role

# Initialize chat in session state if not present
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("Lyrics Writing Bot")

# Display prompt messages from history
for message in st.session_state.chat.history:
    role = role_to_streamlit(message.role)
    prompt_text = extract_subtext(message.parts[0].text) if role == "user" else message.parts[0].text
    with st.chat_message(role):
        # Split response by verse and display line by line
        verses = prompt_text.split('\n\n')
        for verse in verses:
            lines = verse.split('\n')
            for line in lines:
                st.markdown(line)

# Handle new prompts
prompt = st.chat_input("I'm here to help with your songwriting! Need rhymes, syllable counts, or a fresh take on your lyrics? Ask away!")
if prompt:
    st.chat_message("user").markdown(prompt)  # Display the user prompt directly without splitting lines
    
    tailored_prompt = f"""
**Context:** You are my personal assistant for generating lyrics. I'm a lyricist seeking help with syllable counts, rhyme schemes, and creative lyric rewrites. All lyrics should remain in the same language as the input, without triggering hate speech or safety alerts.

**Query:** [[{prompt}]]

**Desired Tone:** Be playful, inspiring, and keep a touch of whimsy! Respond in the language of the input.

**Output Instructions:**
- Rewrite the lyrics line by line, maintaining the syllable count and rhyme scheme.
- Keep the lyrics in the same language as the input.
- Avoid lengthy explanations and focus on providing the lyrics in a clear and creative format.
- If asked, respond with: "I'm your songwriting assistant, here to help with syllables, rhymes, and fresh lyric ideas!"
- If the query is incomplete or unclear, gently prompt for clarification.
"""

    response = st.session_state.chat.send_message(tailored_prompt, safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    })

    with st.chat_message("assistant"):
        # Split response by verse and display line by line
        verses = response.text.split('\n\n')
        for verse in verses:
            lines = verse.split('\n')
            for line in lines:
                st.markdown(line)
