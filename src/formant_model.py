# formant_model.py

import numpy as np
import pandas as pd
import scipy.signal

class FormantModel:
    def __init__(self, csv_path='data/phenome_formant_data.csv', sampling_rate=16000):
        """
        Initialize the formant model with data from a CSV file.
        
        Parameters:
        csv_path (str): Path to the CSV file containing phenome formant data.
        sampling_rate (int): Sampling rate for the synthesized waveform.
        """
        self.phenome_data = pd.read_csv(csv_path).set_index('Phenome')
        self.sampling_rate = sampling_rate

    def get_formants(self, phenome):
        """
        Retrieve formant frequencies and bandwidths for a given phenome.
        
        Parameters:
        phenome (str): The phenome to retrieve data for.
        
        Returns:
        list: List of tuples containing formant frequency and bandwidth pairs.
        """
        if phenome not in self.phenome_data.index:
            return None
        f1 = np.random.normal(self.phenome_data.loc[phenome, 'F1_Mean'], self.phenome_data.loc[phenome, 'F1_Std'])
        f2 = np.random.normal(self.phenome_data.loc[phenome, 'F2_Mean'], self.phenome_data.loc[phenome, 'F2_Std'])
        f3 = np.random.normal(self.phenome_data.loc[phenome, 'F3_Mean'], self.phenome_data.loc[phenome, 'F3_Std'])
        b1 = np.random.normal(self.phenome_data.loc[phenome, 'F1_BW'], self.phenome_data.loc[phenome, 'BW_Std'])
        b2 = np.random.normal(self.phenome_data.loc[phenome, 'F2_BW'], self.phenome_data.loc[phenome, 'BW_Std'])
        b3 = np.random.normal(self.phenome_data.loc[phenome, 'F3_BW'], self.phenome_data.loc[phenome, 'BW_Std'])
        return [(f1, b1), (f2, b2), (f3, b3)]

    def generate_vowel_waveform(self, formants, duration=0.1):
        """
        Generate the waveform for a vowel based on formant frequencies and bandwidths.
        
        Parameters:
        formants (list): List of formant frequency and bandwidth pairs.
        duration (float): Duration of the generated waveform in seconds.
        
        Returns:
        np.ndarray: The synthesized waveform for the vowel.
        """
        t = np.linspace(0, duration, int(self.sampling_rate * duration), endpoint=False)
        waveform = np.zeros_like(t)
        for (f, b) in formants:
            alpha = np.pi * b / self.sampling_rate
            envelope = np.exp(-alpha * t)
            sinewave = np.sin(2 * np.pi * f * t)
            waveform += envelope * sinewave
        return waveform

    def transition_waveform(self, formants1, formants2, duration=0.05):
        """
        Generate the transition waveform between two phenomes.
        
        Parameters:
        formants1 (list): Formants of the starting phenome.
        formants2 (list): Formants of the ending phenome.
        duration (float): Duration of the transition in seconds.
        
        Returns:
        np.ndarray: The synthesized waveform for the transition.
        """
        t = np.linspace(0, duration, int(self.sampling_rate * duration), endpoint=False)
        waveform = np.zeros_like(t)
        for ((f1, b1), (f2, b2)) in zip(formants1, formants2):
            freq_transition = np.linspace(f1, f2, len(t))
            bw_transition = np.linspace(b1, b2, len(t))
            alpha = np.pi * bw_transition / self.sampling_rate
            envelope = np.exp(-alpha * t)
            sinewave = np.sin(2 * np.pi * freq_transition * t)
            waveform += envelope * sinewave
        return waveform

    def synthesize_speech(self, phenomes, phenome_duration=0.1):
        """
        Synthesize speech from a sequence of phenomes.
        
        Parameters:
        phenomes (list): List of phenomes to synthesize.
        phenome_duration (float): Duration for each phenome's waveform.
        
        Returns:
        np.ndarray: The synthesized speech waveform.
        """
        speech_waveform = []
        for i, phenome in enumerate(phenomes):
            formants = self.get_formants(phenome)
            if formants is None:
                continue
            if i > 0:
                prev_formants = self.get_formants(phenomes[i - 1])
                transition = self.transition_waveform(prev_formants, formants)
                speech_waveform.extend(transition)
            vowel_waveform = self.generate_vowel_waveform(formants, phenome_duration)
            speech_waveform.extend(vowel_waveform)
        return np.array(speech_waveform)
