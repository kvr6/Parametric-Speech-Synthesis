import os
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from gtts import gTTS
from playsound import playsound
from .user_profiling import UserProfile
from .context_analysis import ContextAnalyzer

class SpeechSynthesizer:
    def __init__(self, user_profile, context):
        self.user_profile = user_profile
        self.context = context

    def apply_personalization(self):
        # Note: gTTS doesn't support real-time voice characteristic changes
        # We'll simulate personalization by adjusting the text
        pitch = self.user_profile.get_preference('pitch')
        speed = self.user_profile.get_preference('speed')
        volume = self.user_profile.get_preference('volume')
        voice_gender = self.user_profile.get_preference('voice_gender')
        
        return f"Simulating {pitch} pitch, {speed} speed, volume level {volume}, and {voice_gender} voice. "

    def synthesize_speech(self, text, output_file='synthesized_speech.mp3'):
        personalization_text = self.apply_personalization()
        full_text = personalization_text + text

        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, output_file)

        try:
            tts = gTTS(full_text)
            tts.save(output_path)
            print(f"Synthesized speech saved to {output_path}")

            # Play the audio
            playsound(output_path)

            # Generate and save spectrogram
            self.plot_spectrogram(output_path)
        except Exception as e:
            print(f"Error during speech synthesis: {e}")
            print("Falling back to text output.")
            with open(output_path.replace('.mp3', '.txt'), 'w') as f:
                f.write(f"TTS Error. Text content: {full_text}")

    def plot_spectrogram(self, audio_file):
        # Read the audio file
        sample_rate, audio = wavfile.read(audio_file)
        
        plt.figure(figsize=(10, 4))
        plt.specgram(audio, Fs=sample_rate, cmap='viridis')
        plt.title('Spectrogram of Synthesized Speech')
        plt.xlabel('Time')
        plt.ylabel('Frequency')
        
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results')
        plt.savefig(os.path.join(output_dir, 'spectrogram.png'))
        plt.close()

def main():
    user_profile = UserProfile('user_001')
    context_analyzer = ContextAnalyzer()
    current_context = context_analyzer.get_current_context()

    synthesizer = SpeechSynthesizer(user_profile, current_context)
    synthesizer.synthesize_speech("Hello, this is a test of the personalized speech synthesis system.")

if __name__ == "__main__":
    main()