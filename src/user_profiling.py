import json
import os
import random

class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = self.load_preferences()

    def load_preferences(self):
        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
        try:
            with open(os.path.join(data_dir, 'user_preferences.json'), 'r') as f:
                all_preferences = json.load(f)
            user_pref = next((user for user in all_preferences if user['user_id'] == self.user_id), None)
            if user_pref:
                # Ensure voice_gender is present
                if 'voice_gender' not in user_pref:
                    user_pref['voice_gender'] = random.choice(['male', 'female'])
                return user_pref
            else:
                return self.create_new_user()
        except FileNotFoundError:
            return self.create_new_user()

    def create_new_user(self):
        return {
            "user_id": self.user_id,
            "pitch": random.choice(["low", "medium", "high"]),
            "speed": random.choice(["slow", "medium", "fast"]),
            "accent": random.choice(["neutral", "british", "american", "australian"]),
            "volume": random.randint(1, 10),
            "voice_gender": random.choice(['male', 'female'])
        }

    def update_preference(self, key, value):
        if self.preferences:
            self.preferences[key] = value
            self.save_preferences()
        else:
            print(f"User {self.user_id} not found in preferences.")

    def get_preference(self, key):
        return self.preferences.get(key) if self.preferences else None

    def save_preferences(self):
        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
        try:
            with open(os.path.join(data_dir, 'user_preferences.json'), 'r') as f:
                all_preferences = json.load(f)
        except FileNotFoundError:
            all_preferences = []

        user_index = next((index for (index, d) in enumerate(all_preferences) if d["user_id"] == self.user_id), None)
        if user_index is not None:
            all_preferences[user_index] = self.preferences
        else:
            all_preferences.append(self.preferences)

        with open(os.path.join(data_dir, 'user_preferences.json'), 'w') as f:
            json.dump(all_preferences, f, indent=2)

def main():
    # Example usage
    user_profile = UserProfile('user_001')
    print(f"User {user_profile.user_id} preferences:")
    print(json.dumps(user_profile.preferences, indent=2))

    # Update a preference
    user_profile.update_preference('pitch', 'high')
    print("\nUpdated pitch preference:")
    print(f"New pitch: {user_profile.get_preference('pitch')}")

if __name__ == "__main__":
    main()