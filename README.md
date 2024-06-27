# Personalized Voice Assistant

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Component Descriptions](#component-descriptions)
5. [Running the Project](#running-the-project)
6. [Project Outcomes](#project-outcomes)
7. [Future Improvements](#future-improvements)

## Project Overview

This project demonstrates a personalized voice assistant system that adapts its speech characteristics based on user preferences and context. The system uses text-to-speech technology combined with machine learning techniques to create a more engaging and personalized user experience.

Key features:
- User profile management
- Context-aware speech adaptation
- Adaptive learning to improve personalization over time
- Speech synthesis with simulated voice characteristic adjustments

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

## Project Structure

```
personalized-voice-assistant/
│
├── src/
│   ├── __init__.py
│   ├── generate_mock_data.py
│   ├── user_profiling.py
│   ├── context_analysis.py
│   ├── speech_synthesizer.py
│   ├── adaptive_synthesizer.py
│   └── personalization_evaluation.py
│
├── results/
│   ├── synthesized_speech.txt
│   ├── synthesized_speech.mp3
│   └── synthesized_speech.wav
│
├── requirements.txt
└── README.md
```

## Component Descriptions

1. **generate_mock_data.py**: Creates mock datasets for user preferences, context samples, and sample dialogues. This simulates real-world data for testing and development purposes.

2. **user_profiling.py**: Manages user profiles, including loading, creating, and updating user preferences such as pitch, speed, and voice gender.

3. **context_analysis.py**: Analyzes the current context (e.g., time of day, location, activity) to make recommendations for speech characteristics.

4. **speech_synthesizer.py**: Handles text-to-speech conversion using gTTS (Google Text-to-Speech). It applies personalization by simulating adjustments to voice characteristics based on user preferences and context.

5. **adaptive_synthesizer.py**: Implements an adaptive learning mechanism that adjusts user preferences based on simulated user feedback, aiming to improve personalization over time.

6. **personalization_evaluation.py**: Evaluates the performance of the personalization system by simulating multiple users and interactions.

## Running the Project

1. Generate mock data:
   ```
   python -m src.generate_mock_data
   ```

2. Run the speech synthesizer for a single interaction:
   ```
   python -m src.speech_synthesizer
   ```

3. Run the adaptive synthesizer to simulate multiple interactions:
   ```
   python -m src.adaptive_synthesizer
   ```

4. Evaluate the personalization system:
   ```
   python -m src.personalization_evaluation
   ```

## Project Outcomes

After running the scripts, you will find the following files in the `results/` directory:

1. **synthesized_speech.txt**: A text file containing the simulated personalized speech content. This is generated when the speech synthesis encounters an error or when running in a mock mode.

2. **synthesized_speech.mp3**: An audio file of the synthesized speech with simulated personalization. This file is created by the gTTS library.

3. **synthesized_speech.wav**: Another audio file format of the synthesized speech. This may be generated if the system converts the MP3 to WAV for further processing.

The system currently outputs the personalization results and simulated user feedback to the console. In a future iteration, we could implement functionality to save these results to a file for easier analysis.

### Interpretation of Results

The personalization system adapts the voice characteristics based on user preferences and context. The adaptation process is simulated and the results are printed to the console. You should see output indicating:

- The initial user preferences
- The context for each interaction
- The personalized speech content
- Simulated user satisfaction scores
- Adjustments made to user preferences based on the feedback

These outputs demonstrate the system's ability to adapt to user preferences over time, although the actual audio differences may be limited due to the constraints of the gTTS library.

## Future Improvements

1. Implement spectrogram generation for visual representation of the synthesized speech.
2. Create a JSON report file with detailed evaluation metrics.
3. Implement more sophisticated context analysis, possibly incorporating machine learning models.
4. Enhance the adaptation algorithm to more quickly identify and apply effective personalization strategies.
5. Integrate real speech synthesis with adjustable parameters for more accurate voice characteristic modifications.
6. Implement user feedback collection mechanisms for real-world testing and evaluation.
7. Explore reinforcement learning techniques for more effective long-term adaptation.

By continually refining the personalization algorithms and expanding the system's capabilities, we aim to create a voice assistant that provides a truly personalized and engaging user experience.
