# Personalized Voice Assistant using Parametric Speech Synthesis

This project demonstrates an advanced approach to creating a personalized voice assistant using parametric speech synthesis techniques. Building upon formant synthesis methods, we've extended the system to adapt voice characteristics based on user preferences and context. This work showcases the application of machine learning and personalization techniques to speech synthesis, originally developed during a Research Assistant internship at the Indian Institute of Technology, Bombay.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Code Description](#code-description)
  - [user_profiling.py](#user_profilingpy)
  - [context_analysis.py](#context_analysispy)
  - [personalized_formant_model.py](#personalized_formant_modelpy)
  - [adaptive_synthesizer.py](#adaptive_synthesizerpy)
  - [personalization_evaluation.py](#personalization_evaluationpy)
- [Running the Project](#running-the-project)
- [Results](#results)
  - [Personalization Metrics](#personalization-metrics)
  - [User Engagement Analysis](#user-engagement-analysis)

## Overview

This project extends parametric speech synthesis to create a personalized voice assistant. It adapts voice characteristics (such as pitch, speed, and accent) based on individual user preferences and context. The system employs machine learning techniques including reinforcement learning and multi-armed bandits to optimize voice parameters for each user.

## Project Structure

```plaintext
personalized-voice-assistant/
│
├── data/
│   ├── phoneme_formant_data.csv      # Base formant data for phonemes
│   ├── user_preferences.json         # User voice preference data
│   ├── context_samples.json          # Sample context data for testing
│   ├── sample_dialogues.txt          # Sample dialogues for synthesis
│
├── src/
│   ├── user_profiling.py             # User preference modeling
│   ├── context_analysis.py           # Context analysis module
│   ├── personalized_formant_model.py # Personalized formant modeling
│   ├── adaptive_synthesizer.py       # Adaptive speech synthesis
│   ├── personalization_evaluation.py # Evaluation of personalization
│
├── results/
│   ├── personalized_speech_samples/  # Personalized speech outputs
│   ├── user_engagement_report.md     # User engagement analysis
│   ├── personalization_metrics.json  # Quantitative personalization metrics
│
└── README.md                         # Project documentation
```

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or later
- Required Python packages (see `requirements.txt`)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/kvr6/personalized-voice-assistant.git
cd personalized-voice-assistant
pip install -r requirements.txt
```

## Data Preparation

Here are the data sources required for the project:

| **Source**              | **Description**                                                   | **Path**                    |
|-------------------------|-------------------------------------------------------------------|---------------------------|
| **Phoneme Formant Data**| Base formant frequencies and bandwidths for different phonemes.   | `data/phoneme_formant_data.csv` |
| **User Preferences**    | JSON file containing user voice preferences.                      | `data/user_preferences.json`   |
| **Context Samples**     | Sample context data for testing personalization.                  | `data/context_samples.json`    |
| **Sample Dialogues**    | Text corpus for synthesizing personalized speech.                 | `data/sample_dialogues.txt`    |

## Code Description

### user_profiling.py

This script models and manages user preferences for voice characteristics.

- **UserProfile Class**: Manages individual user profiles, including voice preferences and interaction history.
- **Usage**: Import to create and update user profiles for personalization.

```python
from user_profiling import UserProfile

user_profile = UserProfile(user_id='user123')
user_profile.update_preference('pitch', 'high')
```

### context_analysis.py

Analyzes the current context to inform voice parameter selection.

- **ContextAnalyzer Class**: Determines appropriate voice characteristics based on time, location, and user activity.

```python
from context_analysis import ContextAnalyzer

analyzer = ContextAnalyzer()
context = analyzer.get_current_context()
```

### personalized_formant_model.py

Extends the original formant model to incorporate user-specific and context-specific parameters.

- **PersonalizedFormantModel Class**: Generates waveforms adapted to user preferences and context.

```python
from personalized_formant_model import PersonalizedFormantModel

model = PersonalizedFormantModel(user_profile, context)
waveform = model.synthesize_speech(phonemes)
```

### adaptive_synthesizer.py

Implements reinforcement learning to optimize voice characteristics based on user engagement.

- **AdaptiveSynthesizer Class**: Continuously refines voice parameters using feedback and engagement metrics.

```python
from adaptive_synthesizer import AdaptiveSynthesizer

synthesizer = AdaptiveSynthesizer(user_profile)
synthesizer.synthesize_and_adapt("Hello, how can I help you today?")
```

### personalization_evaluation.py

Evaluates the effectiveness of personalization by analyzing user engagement and satisfaction metrics.

- **Evaluation Metrics**: Calculates personalization impact score, user satisfaction rating, and engagement time.

```python
python src/personalization_evaluation.py
```

## Running the Project

Follow these steps to run the personalized voice assistant:

1. **Initialize User Profile**: `python src/user_profiling.py --user_id user123`
2. **Analyze Context**: `python src/context_analysis.py`
3. **Generate Personalized Speech**: `python src/adaptive_synthesizer.py --user_id user123 --text "Hello, world!"`
4. **Evaluate Personalization**: `python src/personalization_evaluation.py --user_id user123`

## Results

### Personalization Metrics

- Detailed personalization metrics are available in `results/personalization_metrics.json`

### User Engagement Analysis

- A comprehensive report on user engagement and satisfaction is available in `results/user_engagement_report.md`
