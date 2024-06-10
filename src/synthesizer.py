import numpy as np
import scipy.io.wavfile as wav
import pandas as pd
from formant_model import FormantModel

def text_to_phenomes(text, csv_path='data/phenome_formant_data.csv'):
    """
    Convert text to a sequence of phenomes using the phenome formant data CSV file.
    
    Parameters:
    text (str): The input text.
    csv_path (str): Path to the CSV file containing formant data.
    
    Returns:
    list: List of phenomes.
    """
    # Load the phenome data
    phenome_data = pd.read_csv(csv_path)

    # Prepare a mapping from phenomes to their properties
    phenome_set = set(phenome_data['Phenome'])
    words = text.lower().split()
    phenomes = []

    # Simplified conversion assuming words match phenomes directly
    for word in words:
        if word in phenome_set:
            phenomes.append(word)
        else:
            phenomes.append('_')  # Placeholder for unknown phenomes

    return phenomes

def synthesize_text_to_speech(text, output_file='results/synthesized_speech.wav'):
    """
    Synthesize speech from text and save it as a WAV file.
    
    Parameters:
    text (str): The input text.
    output_file (str): Path to the output WAV file.
    """
    formant_model = FormantModel()
    phenomes = text_to_phenomes(text)
    waveform = formant_model.synthesize_speech(phenomes)
    waveform = (waveform * 32767).astype(np.int16)  # Scale to int16 for WAV
    wav.write(output_file, formant_model.sampling_rate, waveform)

if __name__ == "__main__":
    try:
        with open('data/synthetic_corpus.txt', 'r') as file:
            text = file.read()
        synthesize_text_to_speech(text)
    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure that the 'data/phenome_formant_data.csv' and 'data/synthetic_corpus.txt' files exist.")
