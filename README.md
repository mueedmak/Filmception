# 🎬 Filmception

An AI-powered multilingual movie summary translator and genre classification system developed using Natural Language Processing (NLP) and Machine Learning.

Filmception enables users to input a movie summary, translate it into multiple languages, convert the translated text into speech, and predict one or more movie genres using a trained machine learning model.

Developed as a semester project for the **Artificial Intelligence** course at **FAST – National University of Computer and Emerging Sciences (FAST-NUCES)**.

---

## ✨ Features

### 🎭 Movie Genre Prediction

- Predicts one or more movie genres from a movie summary
- Multi-label classification
- TF-IDF feature extraction
- Machine Learning based genre prediction

### 🌍 Multilingual Translation

Translate movie summaries into:

- 🇺🇸 English
- 🇵🇰 Urdu
- 🇸🇦 Arabic
- 🇰🇷 Korean

### 🔊 Text-to-Speech

- Convert translated summaries into speech
- Audio generation for supported languages
- Interactive playback through the application

### 📊 Data Processing

- Movie summary preprocessing
- Text cleaning
- Tokenization
- Stop-word removal
- Lemmatization
- Genre extraction
- Dataset preparation for model training

### 🖥 Graphical User Interface

- User-friendly GUI
- Summary input
- Genre prediction
- Translation
- Audio generation

---

## 🏗 Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- NLTK
- TF-IDF Vectorizer
- Google Translate / Translation APIs
- gTTS (Google Text-to-Speech)
- Tkinter (GUI)
- Jupyter Notebook

---

## 📂 Repository Structure

```text
.
├── Gui.py
├── Data_pre_proc.ipynb
├── genre.ipynb
├── cleaned_movie_data.csv
├── README.md
└── images/
```

---

## Dataset

The project uses the **CMU Movie Summary Dataset** from Kaggle.

Dataset:
https://www.kaggle.com/datasets/msafi04/movies-genre-dataset-cmu-movie-summary

---

## Machine Learning Pipeline

1. Data preprocessing
2. Text cleaning
3. Feature extraction using TF-IDF
4. Model training
5. Multi-label genre prediction
6. Translation
7. Audio generation

---

## Features Implemented

- Dataset preprocessing
- Genre extraction
- TF-IDF feature engineering
- Genre classification
- Multilingual translation
- Text-to-speech conversion
- Interactive GUI

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Natural Language Processing (NLP)
- Machine Learning
- Text preprocessing
- Feature engineering
- Multi-label classification
- Translation systems
- Text-to-Speech
- GUI development in Python

---

## Academic Project

Developed for the **Artificial Intelligence** course at **FAST – National University of Computer and Emerging Sciences (FAST-NUCES)**.

---

## Contributors

- Abdul Mueed Malik
- Fahad Raza
---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/mueedmak/Filmception.git
cd Filmception
```

### 2. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required packages

```bash
pip install pandas numpy scikit-learn nltk gtts googletrans==4.0.0-rc1 matplotlib jupyter
```

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

### 4. Launch the application

```bash
python Gui.py
```

### 5. (Optional) Run the notebooks

For preprocessing:

```bash
jupyter notebook Data_pre_proc.ipynb
```

For genre model development:

```bash
jupyter notebook genre.ipynb
```
