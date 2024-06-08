import numpy as np
import pandas as pd
import wave
import struct
import nltk
from scipy.signal import lfilter

# Ensure NLTK datasets are downloaded (run once)
nltk.download('cmudict')

# Load CMU Pronouncing Dictionary
cmudict = nltk.corpus.cmudict.dict()

# Load phoneme formant data
phoneme_data = pd.read_csv('data/phoneme_formant_data.csv').set_index('Phoneme')

class FormantModel:
    def __init__(self):
        self.phoneme_data = phoneme_data

    def get_formants(self, phoneme):
        if phoneme not in self.phoneme_data.index:
            return None
        f1 = np.random.normal(self.phoneme_data.loc[phoneme, 'F1_Mean'], self.phoneme_data.loc[phoneme, 'F1_Std'])
        f2 = np.random.normal(self.phoneme_data.loc[phoneme, 'F2_Mean'], self.phoneme_data.loc[phoneme, 'F2_Std'])
        f3 = np.random.normal(self.phoneme_data.loc[phoneme, 'F3_Mean'], self.phoneme_data.loc[phoneme, 'F3_Std'])
        return f1, f2, f3

def generate_waveform(formants, duration=0.1, sampling_rate=16000):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    waveform = sum(np.sin(2 * np.pi * formant * t) for formant in formants)
    # Apply a simple envelope for smoothing
    envelope = np.linspace(0, 1, int(sampling_rate * duration / 2))
    envelope = np.concatenate((envelope, envelope[::-1]))
    return waveform * envelope

def text_to_phonemes(text):
    words = nltk.word_tokenize(text.lower())
    phoneme_sequence = []
    for word in words:
        if word in cmudict:
            phonemes = cmudict[word][0]  # Take the first pronunciation
            phoneme_sequence.extend(phonemes)
        else:
            phoneme_sequence.append(' ')
    return phoneme_sequence

def save_wave(waveform, filename, sampling_rate=16000):
    waveform_integers = np.int16(waveform * 32767)
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sampling_rate)
        wf.writeframes(waveform_integers.tobytes())

if __name__ == "__main__":
    # Load the synthetic corpus text
    with open('data/synthetic_corpus.txt', 'r') as file:
        text = file.read().replace('\n', ' ')
    
    formant_model = FormantModel()
    phoneme_sequence = text_to_phonemes(text)
    
    waveform = np.array([])
    for phoneme in phoneme_sequence:
        if phoneme.isdigit():  # Ignore stress markers from CMUDict
            continue
        formants = formant_model.get_formants(phoneme)
        if formants:
            waveform = np.concatenate((waveform, generate_waveform(formants)))
        else:
            # Add a small silence for unrecognized phonemes or spaces
            waveform = np.concatenate((waveform, np.zeros(int(0.05 * 16000))))
    
    # Save the generated waveform to a file
    save_wave(waveform, 'results/synthesized_speech.wav')
