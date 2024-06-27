import csv
import random
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the data directory if it doesn't exist
data_dir = os.path.join(script_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

# List of phonemes (simplified for this example)
phonemes = ['a', 'e', 'i', 'o', 'u', 'p', 't', 'k', 's', 'm', 'n']

# Generate mock data
data = []
for phoneme in phonemes:
    for i in range(3):  # 3 formants per phoneme
        formant_freq = random.randint(200, 3000)
        bandwidth = random.randint(50, 300)
        data.append([phoneme, f'F{i+1}', formant_freq, bandwidth])

# Write to CSV
csv_path = os.path.join(data_dir, 'phoneme_formant_data.csv')
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Phoneme', 'Formant', 'Frequency', 'Bandwidth'])
    writer.writerows(data)

print(f"phoneme_formant_data.csv generated successfully at {csv_path}")