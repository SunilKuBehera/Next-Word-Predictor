# Next-Word-Predictor |
**Next Word Predictor** is an web app that predicts the next word for a given phrase using an LSTM model trained on Shakespeare's Hamlet.

## Features
- Type a phrase and predict the next word.
- "Surprise Me" button picks a random line from `hamlet.txt` and populates the input.
- Download the full `hamlet.txt`.
- Uses a saved Keras model (`nextWord_LSTM_model.keras`) and tokenizer (`tokenizer.pickle`).

## Files
- `app.py` — Streamlit application.
- `hamlet.txt` — Source text used for training / surprise lines.
- `nextWord_LSTM_model.keras` — Trained LSTM model (required to run the app).
- `tokenizer.pickle` — Tokenizer used during training (required).
- `Experiments.ipynb` — Notebook used to preprocess data and train the model.
- `requirements.txt` — Python dependencies.

## Requirements
- Python 3.8–3.10 (recommended)
- See `requirements.txt` (TensorFlow, Streamlit, numpy, pandas, scikit-learn, matplotlib)

Install dependencies (Windows example):
```powershell
python -m pip install -r requirements.txt
```

## Run the app (Windows)
From the project folder:
```powershell
streamlit run app.py
```
## Notes
- The app requires `nextWord_LSTM_model.keras` and `tokenizer.pickle` in the project root. If missing, train the model using `Experiments.ipynb` (the notebook contains preprocessing and model training steps and saves both artifacts).
- The prediction function pads input to a fixed sequence length — ensure the tokenizer and model were created with compatible max sequence length.

## Troubleshooting
- If the app fails to load the model/tokenizer, check file names and paths.
- If predictions are poor, consider retraining with adjusted hyperparameters or more data (see `Experiments.ipynb`).

## License & Credits
- Model trained on public domain text (Shakespeare). Include attributions as needed.
