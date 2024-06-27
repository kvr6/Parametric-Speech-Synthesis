# Personalized Voice Assistant using Speech Synthesis

This project demonstrates an advanced approach to creating a personalized voice assistant using actual speech synthesis techniques. Building upon formant synthesis methods originally explored during a Research Assistant internship at the Indian Institute of Technology, Bombay, we've extended the system to adapt voice characteristics based on user preferences and context.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Results](#results)
- [Scalability Considerations](#scalability-considerations)

## Overview

This project extends speech synthesis techniques to create a personalized voice assistant. The system adapts voice characteristics (such as pitch, speed, volume, and voice gender) based on individual user preferences and context. By employing adaptive learning techniques, the assistant optimizes voice parameters for each user, creating a highly personalized interaction experience.

Key features of the project include:
- User preference modeling for voice characteristics
- Context-aware adaptation of speech parameters
- Adaptive learning for continuous improvement of personalization
- Realistic speech synthesis using pyttsx3

## Project Structure

```plaintext
personalized-voice-assistant/
│
├── data/
│   ├── phoneme_formant_data.csv      # Base formant data for phonemes
│   ├── user_preferences.json         # User voice preference data
│   ├── context_samples.json          # Sample context data for testing
│   └── sample_dialogues.txt          # Sample dialogues for synthesis
│
├── src/
│   ├── generate_mock_data.py         # Script to generate mock datasets
│   ├── user_profiling.py             # User preference modeling
│   ├── context_analysis.py           # Context analysis module
│   ├── speech_synthesizer.py         # Speech synthesis module
│   ├── adaptive_synthesizer.py       # Adaptive speech synthesis
│   └── personalization_evaluation.py # Evaluation of personalization
│
├── results/
│   ├── synthesized_speech.wav        # Output synthesized speech
│   ├── spectrogram.png               # Spectrogram of synthesized speech
│   └── evaluation_report.json        # Personalization evaluation report
│
├── requirements.txt                  # Project dependencies
└── README.md                         # Project documentation
```

## Prerequisites

- Python 3.8 or later
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/personalized-voice-assistant.git
   cd personalized-voice-assistant
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Project

Follow these steps to run the project and see the results:

1. Generate mock data:
   ```
   python src/generate_mock_data.py
   ```
   This will create mock datasets in the `data/` directory.

2. Run the user profiling script:
   ```
   python src/user_profiling.py
   ```
   This will demonstrate how user profiles are created and managed.

3. Run the context analysis script:
   ```
   python src/context_analysis.py
   ```
   This will show how the system analyzes context for personalization.

4. Run the speech synthesizer:
   ```
   python src/speech_synthesizer.py
   ```
   This will generate a sample synthesized speech file and a spectrogram in the `results/` directory.

5. Run the adaptive synthesizer:
   ```
   python src/adaptive_synthesizer.py
   ```
   This will demonstrate how the system adapts to user feedback over multiple interactions.

6. Run the personalization evaluation:
   ```
   python src/personalization_evaluation.py
   ```
   This will generate an evaluation report in the `results/` directory.

## Results

After running the scripts, you can find the following results:

1. Synthesized speech: `results/synthesized_speech.wav`
   - You can play this file to hear the personalized synthesized speech.

2. Spectrogram: `results/spectrogram.png`
   - This image shows the frequency content of the synthesized speech over time.

3. Evaluation report: `results/evaluation_report.json`
   - This JSON file contains metrics on the performance of the personalization system.

To interpret the results:
- Listen to the synthesized speech files to hear how the voice changes based on personalization.
- Compare spectrograms to see how the frequency content changes with different personalizations.
- Review the evaluation report to see how user satisfaction changes over time and across different users.

## Scalability Considerations

While this demonstration uses mock data and runs locally, the system is designed with scalability in mind:

1. The user profiling system can be extended to use a database for storing large numbers of user profiles.
2. The context analysis module can be adapted to process real-time data streams.
3. The speech synthesis can be offloaded to a cloud service for handling multiple requests simultaneously.
4. The adaptive learning system can be implemented using distributed computing frameworks for large-scale learning.

For production use, consider implementing proper error handling, logging, and integrating with cloud services for improved scalability and reliability.
