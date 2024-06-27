import csv
import random
import os

# Get the directory of the current script (which is in the src folder)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the project root directory (one level up from src)
project_root = os.path.dirname(script_dir)

# Create the data directory in the project root
data_dir = os.path.join(project_root, 'data')
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
print(f"Script directory: {script_dir}")
print(f"Project root directory: {project_root}")
print(f"Data directory: {data_dir}")