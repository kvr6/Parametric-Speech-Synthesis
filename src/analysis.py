import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.signal import correlate, spectrogram
from scipy.stats import pearsonr
import os

def load_waveform(file_path):
    """
    Load a waveform from a WAV file.
    """
    sampling_rate, waveform = wav.read(file_path)
    return waveform, sampling_rate

def calculate_intelligibility(synthesized_waveform, reference_waveform):
    """
    Calculate the intelligibility by correlating the synthesized waveform with the reference waveform.
    """
    if len(synthesized_waveform) > len(reference_waveform):
        synthesized_waveform = synthesized_waveform[:len(reference_waveform)]
    else:
        reference_waveform = reference_waveform[:len(synthesized_waveform)]
    
    correlation, _ = pearsonr(synthesized_waveform, reference_waveform)
    return correlation

def plot_waveforms(synthesized_waveform, reference_waveform, sampling_rate):
    """
    Plot the synthesized and reference waveforms for visual comparison.
    """
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(np.linspace(0, len(reference_waveform) / sampling_rate, len(reference_waveform)), reference_waveform, label='Reference')
    plt.title('Reference Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(2, 1, 2)
    plt.plot(np.linspace(0, len(synthesized_waveform) / sampling_rate, len(synthesized_waveform)), synthesized_waveform, label='Synthesized', color='orange')
    plt.title('Synthesized Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

def plot_spectrogram(waveform, sampling_rate, title='Spectrogram'):
    """
    Plot the spectrogram of a waveform.
    """
    f, t, Sxx = spectrogram(waveform, fs=sampling_rate)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.show()

def save_comparison_report(synthesized_file, reference_file, report_file):
    """
    Save a comparison report between synthesized and reference speech.
    """
    synthesized_waveform, sampling_rate = load_waveform(synthesized_file)
    reference_waveform, _ = load_waveform(reference_file)

    # Calculate intelligibility
    intelligibility_score = calculate_intelligibility(synthesized_waveform, reference_waveform)

    with open(report_file, 'w') as report:
        report.write(f"Comparison Report\n\n")
        report.write(f"Intelligibility Score: {intelligibility_score:.2f}\n\n")

    # Plot and save waveforms
    plot_waveforms(synthesized_waveform, reference_waveform, sampling_rate)
    plot_spectrogram(reference_waveform, sampling_rate, title='Reference Spectrogram')
    plot_spectrogram(synthesized_waveform, sampling_rate, title='Synthesized Spectrogram')

def analyze_directory(synthesized_dir, reference_dir, report_dir):
    """
    Analyze all synthesized files against their reference counterparts in the given directories.
    """
    os.makedirs(report_dir, exist_ok=True)

    for file_name in os.listdir(synthesized_dir):
        if file_name.endswith('.wav'):
            synthesized_file = os.path.join(synthesized_dir, file_name)
            reference_file = os.path.join(reference_dir, file_name)

            if os.path.exists(reference_file):
                report_file = os.path.join(report_dir, f"{os.path.splitext(file_name)[0]}_report.txt")
                save_comparison_report(synthesized_file, reference_file, report_file)
            else:
                print(f"Reference file for {file_name} not found.")

# Example usage for testing
if __name__ == "__main__":
    analyze_directory('results/synthesized_samples', 'data/natural_speech_samples', 'results/reports')
