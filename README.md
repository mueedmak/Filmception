# Filmception - Movie Summary Processor 🎬

Filmception is an AI-powered Streamlit web application that processes movie summaries to predict genres, translate text, and convert summaries into speech audio.

## Features
- **Genre Prediction**: Predicts movie genres based on the plot summary using a trained machine learning model.
- **Translation**: Translates the movie summary into different languages (Arabic, Urdu, Korean) using `deep_translator`.
- **Text-to-Speech (TTS)**: Converts the translated summary into an audio file using `gTTS`.

## Project Structure
- `Gui.py`: The main Streamlit application script.
- `Data_pre_proc.ipynb` & `genre.ipynb`: Jupyter Notebooks used for data preprocessing and model training.
- Model Files: `tfidf_vectorizer.pkl`, `genre_model.pkl` (needs to be generated/downloaded), `mlb.pkl` (needs to be generated/downloaded).

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd "AI project"
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install streamlit deep-translator gTTS scikit-learn
   ```

4. Make sure your trained model files (`genre_model.pkl`, `tfidf_vectorizer.pkl`, `mlb.pkl`) are in the root directory.

## Usage
Run the Streamlit application using the following command:
```bash
streamlit run Gui.py
```
