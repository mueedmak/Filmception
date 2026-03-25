import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import pickle
import tempfile

# Function to load model components with error handling
def load_model_components():
    try:
        # Load the TF-IDF vectorizer
        with open("tfidf_vectorizer.pkl", "rb") as f:
            tfidf = pickle.load(f)

        # Load your trained model
        with open("genre_model.pkl", "rb") as f:
            model = pickle.load(f)

        # Load MultiLabelBinarizer
        with open("mlb.pkl", "rb") as f:
            mlb = pickle.load(f)

        return tfidf, model, mlb
    except Exception as e:
        st.error(f"Error loading model components: {str(e)}")
        st.error("Please make sure you have trained and saved the model first!")
        return None, None, None

# Load model components
tfidf, model, mlb = load_model_components()

# Clean the text (lowercase and strip whitespace)
def clean_text(text):
    return text.lower().strip()

# Translate function using deep_translator
def translate_text(text, target_lang):
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

# Function to convert text to speech
def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(tmp_file.name)
    return tmp_file.name

# Function to predict genres
def predict_genres(text):
    if model is None or tfidf is None or mlb is None:
        st.error("Model components not loaded properly!")
        return []
    
    try:
        # Clean the text
        cleaned_text = clean_text(text)
        # Transform the input text
        text_tfidf = tfidf.transform([cleaned_text])
        # Get predictions
        predictions = model.predict(text_tfidf)
        # Get the predicted genres
        predicted_genres = mlb.inverse_transform(predictions)
        return predicted_genres[0]
    except Exception as e:
        st.error(f"Error predicting genres: {str(e)}")
        return []

# Streamlit App Interface
st.title("🎬 Filmception - Movie Summary Processor")

# Input movie summary
summary = st.text_area("Enter movie summary:")

if summary:
    # Add a section for genre prediction
    st.subheader("Genre Prediction")
    if st.button("Predict Genres"):
        predicted_genres = predict_genres(summary)
        if predicted_genres:
            st.write("**Predicted Genres:**")
            for genre in predicted_genres:
                st.write(f"- {genre}")

    st.subheader("Choose an action:")

    # Translate and TTS
    lang = st.selectbox("Select language for translation/audio", ['ar', 'ur', 'ko'])
    if st.button("Translate and Convert to Audio"):
        translated_text = translate_text(summary, lang)
        st.write(f"**Translated ({lang}):** {translated_text}")

        audio_path = text_to_speech(translated_text, lang)
        st.audio(audio_path, format='audio/mp3')
        st.success("Audio file generated!")