import numpy as np
import pandas as pd
import json

class FormantModel:
    def __init__(self, sampling_rate=16000):
        """
        Initialize the Formant Model with phoneme data and sampling rate.
        """
        self.phoneme_data = pd.read_csv('data/phoneme_formant_data.csv').set_index('Phoneme')
        self.sampling_rate = sampling_rate

    def get_formants(self, phoneme):
        """
        Retrieve formant frequencies and bandwidths for the given phoneme.
        """
        if phoneme not in self.phoneme_data.index:
            return None
        f1 = np.random.normal(self.phoneme_data.loc[phoneme, 'F1_Mean'], self.phoneme_data.loc[phoneme, 'F1_Std'])
        f2 = np.random.normal(self.phoneme_data.loc[phoneme, 'F2_Mean'], self.phoneme_data.loc[phoneme, 'F2_Std'])
        f3 = np.random.normal(self.phoneme_data.loc[phoneme, 'F3_Mean'], self.phoneme_data.loc[phoneme, 'F3_Std'])
        b1 = np.random.normal(self.phoneme_data.loc[phoneme, 'F1_BW'], self.phoneme_data.loc[phoneme, 'BW_Std'])
        b2 = np.random.normal(self.phoneme_data.loc[phoneme, 'F2_BW'], self.phoneme_data.loc[phoneme, 'BW_Std'])
        b3 = np.random.normal(self.phoneme_data.loc[phoneme, 'F3_BW'], self.phoneme_data.loc[phoneme, 'BW_Std'])
        return (f1, b1), (f2, b2), (f3, b3)

    def generate_vowel_waveform(self, formants, duration=0.1):
        """
        Generate a waveform for vowel sounds based on formant frequencies and bandwidths.
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
        Generate a waveform for a transition between two phonemes.
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

    def synthesize_phoneme(self, phoneme, duration=0.1):
        """
        Generate a waveform for a single phoneme.
        """
        formants = self.get_formants(phoneme)
        if formants:
            return self.generate_vowel_waveform(formants, duration)
        else:
            return np.zeros(int(self.sampling_rate * duration))

    def synthesize_speech(self, phoneme_sequence, duration_per_phoneme=0.1):
        """
        Synthesize a full speech waveform from a sequence of phonemes.
        """
        waveform = np.array([])
        previous_formants = None

        for phoneme in phoneme_sequence:
            formants = self.get_formants(phoneme)
            if formants:
                if previous_formants:
                    # Add transition waveform
                    waveform = np.concatenate((waveform, self.transition_waveform(previous_formants, formants)))
                # Add main phoneme waveform
                waveform = np.concatenate((waveform, self.generate_vowel_waveform(formants, duration=duration_per_phoneme)))
                previous_formants = formants
            else:
                # Add silence for unrecognized phonemes or spaces
                waveform = np.concatenate((waveform, np.zeros(int(duration_per_phoneme * self.sampling_rate))))

        return waveform

    def save_waveform(self, waveform, filename):
        """
        Save the waveform to a WAV file.
        """
        waveform_integers = np.int16(waveform * 32767)
        with wave.open(filename, 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(self.sampling_rate)
            wf.writeframes(waveform_integers.tobytes())

    def synthesize_and_save(self, phoneme_sequence, filename, duration_per_phoneme=0.1):
        """
        Synthesize speech from phoneme sequence and save to file.
        """
        waveform = self.synthesize_speech(phoneme_sequence, duration_per_phoneme)
        self.save_waveform(waveform, filename)

# Example usage for testing
if __name__ == "__main__":
    formant_model = FormantModel()
    
    # Example phoneme sequence
    phonemes = ['a', 'e', 'i', 'o', 'u', 'b', 'd', 'g', 'm', 'n']
    waveform = formant_model.synthesize_speech(phonemes)
    
    # Save to file
    formant_model.save_waveform(waveform, 'results/synthesized_test.wav')
