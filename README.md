# Parametric Speech Synthesis
This project demonstrates a comprehensive approach to parametric speech synthesis using formant synthesis techniques. The goal is to generate synthetic speech from a sequence of phonemes by modeling formant frequencies and bandwidths. This work was done as part of a Research Assistant internship with the Department of Computer Science at the Indian Institute of Technology, Bombay.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Code Description](#code-description)
  - [formant_model.py](#formant_modelpy)
  - [synthesizer.py](#synthesizerpy)
  - [analysis.py](#analysispy)
  - [evaluation.py](#evaluationpy)
- [Running the Project](#running-the-project)
- [Results](#results)
  - [Spectrograms](#spectrograms)
  - [Evaluation Report](#evaluation-report)

## Overview

This project explores parametric speech synthesis using formant synthesis techniques. The process involves converting text (phoneme sequences) into speech by modeling formant frequencies and bandwidths for each phoneme. The synthesized speech is then analyzed and evaluated against reference natural speech.

## Project Structure

```plaintext
parametric-speech-synthesis/
│
├── data/
│   ├── phoneme_formant_data.csv      # Formant data for phonemes
│   ├── synthetic_corpus.txt          # Text corpus for synthesis
│   ├── sample_text.txt               # Sample text for synthesis
│   ├── reference_speech.wav          # Reference speech for evaluation
│
├── src/
│   ├── formant_model.py              # Formant modeling script
│   ├── synthesizer.py                # Speech synthesis script
│   ├── analysis.py                   # Script for analyzing synthesized speech
│   ├── evaluation.py                 # Script for evaluating synthesized speech
│
├── results/
│   ├── synthesized_speech.wav        # Output synthesized speech
│   ├── reference_spectrogram.png     # Spectrogram of reference speech
│   ├── synthesized_spectrogram.png   # Spectrogram of synthesized speech
│   ├── evaluation_report.md          # Detailed evaluation report
│
└── README.md                         # Project documentation
```

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or later
- Required Python packages (see `requirements.txt`)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/kaushikvr/parametric-speech-synthesis.git
cd parametric-speech-synthesis
pip install -r requirements.txt
```

## Data Preparation

Here are the data sources required for the project:

| **Source**                   | **Description**                                                              | **Path**                        |
|------------------------------|------------------------------------------------------------------------------|---------------------------------|
| **Phoneme Formant Data**     | Contains mean formant frequencies and bandwidths for different phonemes.     | `data/phoneme_formant_data.csv` |
| **Text Corpus**              | A sample text corpus for synthesis.                                          | `data/synthetic_corpus.txt`     |
| **Reference Speech**         | A natural speech WAV file used as a reference for evaluation.                | `data/reference_speech.wav`     |

## Code Description

### formant_model.py

This script models the formants for phonemes and generates waveforms for each phoneme.

- **FormantModel Class**: Retrieves formant frequencies and bandwidths, generates waveforms for phonemes and transitions.
- **Usage**: Import the class to model formants and generate phoneme waveforms.

```python
# Example usage
from formant_model import FormantModel

formant_model = FormantModel()
phonemes = ['a', 'e', 'i', 'o', 'u']
waveform = formant_model.synthesize_speech(phonemes)
```

### synthesizer.py

This script synthesizes speech from a sequence of phonemes and saves it as a WAV file.

- **Synthesize and Save**: Converts phoneme sequences into speech and saves the output.

```python
# Run the script to generate synthesized speech
python src/synthesizer.py
```

### analysis.py

This script analyzes the synthesized speech by comparing it with reference speech.

- **Metrics**: Calculates SNR, RMSE, and plots waveforms and spectrograms.

```python
# Run the script to analyze synthesized speech
python src/analysis.py
```

### evaluation.py

This script evaluates the performance of the synthesized speech against the reference speech.

- **Evaluation Report**: Generates a detailed evaluation report including quantitative metrics and spectrogram comparisons.

```python
# Run the script to evaluate synthesized speech
python src/evaluation.py
```

## Running the Project

Follow these steps to run the project:

1. **Generate Synthesized Speech**: `python src/synthesizer.py`
2. **Analyze Synthesized Speech**: `python src/analysis.py`
3. **Evaluate Synthesized Speech**: `python src/evaluation.py`

## Results

### Spectrograms

- **Reference Spectrogram**:
  ![Reference Spectrogram](results/reference_spectrogram.png)
  
- **Synthesized Spectrogram**:
  ![Synthesized Spectrogram](results/synthesized_spectrogram.png)

### Evaluation Report

The detailed evaluation report is available in `results/evaluation_report.md`.




