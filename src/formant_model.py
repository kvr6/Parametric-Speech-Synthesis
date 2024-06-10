import numpy as np
import pandas as pd
import scipy.signal

class FormantModel:
    def __init__(self, csv_path='data/phoneme_formant_data.csv', sampling_rate=16000):
        """
        Initialize the formant model with data from a CSV file.
        
        Parameters:
        csv_path (str): Path to the CSV file containing formant data.
        sampling_rate (int): Sampling rate for the synthesized waveform.
        """
        self.phoneme_data = pd.read_csv(csv_path).set_index('Phoneme')
        self.sampling_rate = sampling_rate

    def get_formants(self, phoneme):
        """
        Retrieve formant frequencies and bandwidths for a given phoneme.
        
        Parameters:
        phoneme (str): The phoneme to retrieve data for.
        
        Returns:
        list: List of tuples containing formant frequency and bandwidth pairs.
        """
        if phoneme not in self.phoneme_data.index:
            return None
        f1 = np.random.normal(self.phoneme_data.loc[phoneme, 'F1_Mean'], self.phoneme_data.loc[phoneme, 'F1_Std'])
        f2 = np.random.normal(self.phoneme_data.loc[phoneme, 'F2_Mean'], self.phoneme_data.loc[phoneme, 'F2_Std'])
        f3 = np.random.normal(self.phoneme_data.loc[phoneme, 'F3_Mean'], self.phoneme_data.loc[phoneme, 'F3_Std'])
        b1 = np.random.normal(self.phoneme_data.loc[phoneme, 'F1_BW'], self.phoneme_data.loc[phoneme, 'BW_Std'])
        b2 = np.random.normal(self.phoneme_data.loc[phoneme, 'F2_BW'], self.phoneme_data.loc[phoneme, 'BW_Std'])
        b3 = np.random.normal(self.phoneme_data.loc[phoneme, 'F3_BW'], self.phoneme_data.loc[phoneme, 'BW_Std'])
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
        Generate the transition waveform between two phonemes.
        
        Parameters:
        formants1 (list): Formants of the starting phoneme.
        formants2 (list): Formants of the ending phoneme.
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

    def synthesize_speech(self, phonemes, phoneme_duration=0.1):
        """
        Synthesize speech from a sequence of phonemes.
        
        Parameters:
        phonemes (list): List of phonemes to synthesize.
        phoneme_duration (float): Duration for each phoneme's waveform.
        
        Returns:
        np.ndarray: The synthesized speech waveform.
        """
        speech_waveform = []
        for i, phoneme in enumerate(phonemes):
            formants = self.get_formants(phoneme)
            if formants is None:
                continue
            if i > 0:
                prev_formants = self.get_formants(phonemes[i - 1])
                transition = self.transition_waveform(prev_formants, formants)
                speech_waveform.extend(transition)
            vowel_waveform = self.generate_vowel_waveform(formants, phoneme_duration)
            speech_waveform.extend(vowel_waveform)
        return np.array(speech_waveform)
