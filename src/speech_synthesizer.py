import pyttsx3
import os
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

class SpeechSynthesizer:
    def __init__(self, user_profile, context):
        self.user_profile = user_profile
        self.context = context
        self.engine = pyttsx3.init()

    def apply_personalization(self):
        # Adjust voice properties based on user preferences and context
        voices = self.engine.getProperty('voices')
        voice_gender = self.user_profile.get_preference('voice_gender')
        self.engine.setProperty('voice', voices[0].id if voice_gender == 'male' else voices[1].id)

        pitch = {'low': 50, 'medium': 100, 'high': 150}[self.user_profile.get_preference('pitch')]
        self.engine.setProperty('pitch', pitch)

        rate = {'slow': 150, 'medium': 200, 'fast': 250}[self.user_profile.get_preference('speed')]
        self.engine.setProperty('rate', rate)

        volume = self.user_profile.get_preference('volume') / 10  # Assuming volume is 1-10 in user preferences
        self.engine.setProperty('volume', volume)

    def synthesize_speech(self, text, output_file='synthesized_speech.wav'):
        self.apply_personalization()

        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, output_file)

        self.engine.save_to_file(text, output_path)
        self.engine.runAndWait()

        print(f"Synthesized speech saved to {output_path}")

        # Generate and save spectrogram
        sample_rate, audio = wavfile.read(output_path)
        self.plot_spectrogram(audio, sample_rate)

    def plot_spectrogram(self, audio, sample_rate):
        plt.figure(figsize=(10, 4))
        plt.specgram(audio, Fs=sample_rate, cmap='viridis')
        plt.title('Spectrogram of Synthesized Speech')
        plt.xlabel('Time')
        plt.ylabel('Frequency')
        
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results')
        plt.savefig(os.path.join(output_dir, 'spectrogram.png'))
        plt.close()

def main():
    from user_profiling import UserProfile
    from context_analysis import ContextAnalyzer

    user_profile = UserProfile('user_001')
    context_analyzer = ContextAnalyzer()
    current_context = context_analyzer.get_current_context()

    synthesizer = SpeechSynthesizer(user_profile, current_context)
    synthesizer.synthesize_speech("Hello, this is a test of the personalized speech synthesis system.")

if __name__ == "__main__":
    main()