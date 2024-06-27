import json
import os
import random
from datetime import datetime

class ContextAnalyzer:
    def __init__(self):
        self.context_samples = self.load_context_samples()

    def load_context_samples(self):
        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
        with open(os.path.join(data_dir, 'context_samples.json'), 'r') as f:
            return json.load(f)

    def get_current_context(self):
        # In a real system, this would get actual current context
        # For this mock-up, we'll randomly select a context
        return random.choice(self.context_samples)

    def analyze_context(self, context):
        # Simple analysis based on context
        time = datetime.fromisoformat(context['timestamp']).time()
        recommendations = {
            'volume': 'low' if time.hour < 9 or time.hour > 21 else 'medium',
            'speed': 'slow' if context['activity'] == 'resting' else 'medium',
            'pitch': 'low' if context['ambient_noise'] > 70 else 'medium'
        }
        return recommendations

def main():
    analyzer = ContextAnalyzer()
    current_context = analyzer.get_current_context()
    print("Current context:")
    print(json.dumps(current_context, indent=2))

    recommendations = analyzer.analyze_context(current_context)
    print("\nRecommendations based on context:")
    print(json.dumps(recommendations, indent=2))

if __name__ == "__main__":
    main()