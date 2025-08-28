import streamlit as st
import pickle
import random
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load tokenizer and model
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = load_model('nextWord_LSTM_model.keras')

# Prediction function
def predict_next_word(text, max_sequence_len=20):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=max_sequence_len-1)
    predicted = model.predict(padded, verbose=0)
    predicted_word_index = predicted.argmax()
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return "No prediction"

# Load lines from hamlet.txt
def get_lines(file_path='hamlet.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except Exception:
        return []

# Load full text for download
def get_full_text(file_path='hamlet.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return "Hamlet text not available."

# Streamlit UI
st.set_page_config(page_title="Next Word Predictor", page_icon="🧠")
st.title("🧠 Next Word Prediction App")

# 📥 Download Hamlet.txt
hamlet_text = get_full_text()
st.download_button(
    label="📥 Download hamlet.txt",
    data=hamlet_text,
    file_name="hamlet.txt",
    mime="text/plain"
)

# Layout: Two columns
left_col, right_col = st.columns(2)


# Left: Surprise line
with left_col:
    st.subheader("🎊 Surprise Me with a Line from Hamlet")
    if st.button("Surprise Me"):
        lines = get_lines()
        if lines:
            random_line = random.choice(lines)
            st.info(f"Random line : _{random_line}_")
            user_input = random_line
        else:
            st.error("Could not load lines from hamlet.txt.")

# Right: Manual input
with right_col:
    st.subheader("✍️ Type Your Own Phrase")
    # use a session_state key so Surprise Me can populate the input
    user_input = st.text_input("Enter your phrase here:", key="user_input", value=st.session_state.get("user_input", ""))

    # 🔮 Predict Button (moved here)
    if st.button("🔮Predict Next Word", key="predict_button"):
        current_input = st.session_state.get("user_input", "").strip()
        if current_input:
            next_word = predict_next_word(current_input)
            st.success(f"Predicted next word: **{next_word}**")
        else:
            st.warning("Please enter a phrase to predict.")