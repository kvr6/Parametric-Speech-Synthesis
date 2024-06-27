import csv
import json
import random
from datetime import datetime, timedelta
import os

def generate_phoneme_formant_data():
    phonemes = ['a', 'e', 'i', 'o', 'u', 'p', 't', 'k', 's', 'm', 'n']
    data = []
    for phoneme in phonemes:
        for i in range(3):  # 3 formants per phoneme
            formant_freq = random.randint(200, 3000)
            bandwidth = random.randint(50, 300)
            data.append([phoneme, f'F{i+1}', formant_freq, bandwidth])
    
    return data

def generate_user_preferences():
    users = []
    for i in range(100):  # Generate data for 100 users
        user = {
            "user_id": f"user_{i:03d}",
            "pitch": random.choice(["low", "medium", "high"]),
            "speed": random.choice(["slow", "medium", "fast"]),
            "accent": random.choice(["neutral", "british", "american", "australian"]),
            "volume": random.randint(1, 10)
        }
        users.append(user)
    
    return users

def generate_context_samples():
    contexts = []
    for i in range(1000):  # Generate 1000 context samples
        start_date = datetime(2023, 1, 1)
        random_date = start_date + timedelta(days=random.randint(0, 364))
        context = {
            "timestamp": random_date.isoformat(),
            "user_id": f"user_{random.randint(0, 99):03d}",
            "location": random.choice(["home", "work", "commute", "gym", "restaurant"]),
            "device": random.choice(["smartphone", "tablet", "laptop", "smart_speaker"]),
            "activity": random.choice(["resting", "working", "exercising", "eating", "traveling"]),
            "ambient_noise": random.randint(0, 100)
        }
        contexts.append(context)
    
    return contexts

def generate_sample_dialogues():
    dialogues = [
        "Hello, how can I assist you today?",
        "What's the weather like in New York?",
        "Please set an alarm for 7 AM tomorrow.",
        "Can you play some relaxing music?",
        "What's on my calendar for next week?",
        "How do I make a vegetarian lasagna?",
        "Tell me a joke, please.",
        "What's the latest news in technology?",
        "Remind me to call mom in an hour.",
        "How long will it take to drive to the airport?"
    ]
    return [random.choice(dialogues) for _ in range(1000)]

def main():
    # Ensure data directory exists
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    os.makedirs(data_dir, exist_ok=True)

    # Generate and save phoneme formant data
    phoneme_data = generate_phoneme_formant_data()
    with open(os.path.join(data_dir, 'phoneme_formant_data.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Phoneme', 'Formant', 'Frequency', 'Bandwidth'])
        writer.writerows(phoneme_data)

    # Generate and save user preferences
    user_prefs = generate_user_preferences()
    with open(os.path.join(data_dir, 'user_preferences.json'), 'w') as f:
        json.dump(user_prefs, f, indent=2)

    # Generate and save context samples
    contexts = generate_context_samples()
    with open(os.path.join(data_dir, 'context_samples.json'), 'w') as f:
        json.dump(contexts, f, indent=2)

    # Generate and save sample dialogues
    dialogues = generate_sample_dialogues()
    with open(os.path.join(data_dir, 'sample_dialogues.txt'), 'w') as f:
        f.write('\n'.join(dialogues))

    print("All mock datasets have been generated successfully.")

if __name__ == "__main__":
    main()