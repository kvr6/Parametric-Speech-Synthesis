import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import os

def load_waveform(file_path):
    """
    Load a waveform from a WAV file.
    """
    sampling_rate, waveform = wav.read(file_path)
    waveform = waveform / np.max(np.abs(waveform))  # Normalize waveform
    return waveform, sampling_rate

def calculate_snr(synthesized_waveform, reference_waveform):
    """
    Calculate the Signal-to-Noise Ratio (SNR) between the synthesized and reference waveforms.
    """
    signal_power = np.mean(reference_waveform ** 2)
    noise_power = np.mean((synthesized_waveform - reference_waveform) ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

def calculate_rmse(synthesized_waveform, reference_waveform):
    """
    Calculate the Root Mean Square Error (RMSE) between the synthesized and reference waveforms.
    """
    if len(synthesized_waveform) > len(reference_waveform):
        synthesized_waveform = synthesized_waveform[:len(reference_waveform)]
    else:
        reference_waveform = reference_waveform[:len(synthesized_waveform)]
    rmse = np.sqrt(np.mean((synthesized_waveform - reference_waveform) ** 2))
    return rmse

def plot_frequency_response(waveform, sampling_rate, title='Frequency Response'):
    """
    Plot the frequency response of a waveform.
    """
    N = len(waveform)
    yf = fft(waveform)
    xf = np.linspace(0.0, sampling_rate / 2.0, N // 2)
    
    plt.figure(figsize=(10, 4))
    plt.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid()
    plt.show()

def compare_spectrograms(synthesized_waveform, reference_waveform, sampling_rate):
    """
    Compare the spectrograms of the synthesized and reference waveforms.
    """
    f, t, Sxx_synth = signal.spectrogram(synthesized_waveform, fs=sampling_rate)
    f, t, Sxx_ref = signal.spectrogram(reference_waveform, fs=sampling_rate)

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.pcolormesh(t, f, 10 * np.log10(Sxx_ref), shading='gouraud')
    plt.title('Reference Spectrogram')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')

    plt.subplot(2, 1, 2)
    plt.pcolormesh(t, f, 10 * np.log10(Sxx_synth), shading='gouraud')
    plt.title('Synthesized Spectrogram')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')

    plt.tight_layout()
    plt.show()

def generate_evaluation_report(synthesized_file, reference_file, report_file):
    """
    Generate a detailed evaluation report comparing the synthesized and reference speech.
    """
    synthesized_waveform, sampling_rate = load_waveform(synthesized_file)
    reference_waveform, _ = load_waveform(reference_file)

    # Calculate metrics
    snr = calculate_snr(synthesized_waveform, reference_waveform)
    rmse = calculate_rmse(synthesized_waveform, reference_waveform)

    with open(report_file, 'w') as report:
        report.write(f"Evaluation Report\n\n")
        report.write(f"Signal-to-Noise Ratio (SNR): {snr:.2f} dB\n")
        report.write(f"Root Mean Square Error (RMSE): {rmse:.4f}\n\n")

    # Plot frequency response
    plot_frequency_response(reference_waveform, sampling_rate, title='Reference Frequency Response')
    plot_frequency_response(synthesized_waveform, sampling_rate, title='Synthesized Frequency Response')

    # Compare spectrograms
    compare_spectrograms(synthesized_waveform, reference_waveform, sampling_rate)

def evaluate_directory(synthesized_dir, reference_dir, report_dir):
    """
    Evaluate all synthesized files against their reference counterparts in the given directories.
    """
    os.makedirs(report_dir, exist_ok=True)

    for file_name in os.listdir(synthesized_dir):
        if file_name.endswith('.wav'):
            synthesized_file = os.path.join(synthesized_dir, file_name)
            reference_file = os.path.join(reference_dir, file_name)

            if os.path.exists(reference_file):
                report_file = os.path.join(report_dir, f"{os.path.splitext(file_name)[0]}_evaluation.txt")
                generate_evaluation_report(synthesized_file, reference_file, report_file)
            else:
                print(f"Reference file for {file_name} not found.")

# Example usage for testing
if __name__ == "__main__":
    evaluate_directory('results/synthesized_samples', 'data/natural_speech_samples', 'results/evaluations')
