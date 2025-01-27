
# 1Text-To-Audio.py
from gtts import gTTS
import os

# Function to convert text to audio
def text_to_audio(text, language='en', filename='output.mp3'):
    
    try:
        # Convert text to speech
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(filename)
        print(f"Audio saved as {filename}")
        
        # Play the audio (Optional: Works on some systems)
        os.system(f"start {filename}")  # Use 'start' for Windows, 'open' for macOS, 'xdg-open' for Linux
    except Exception as e:
        print(f"Error: {e}")
print("Welcome to the Text-to-Audio Converter!")
# Input text
text = input("Enter the text you want to convert to audio: ")

# Call the function
text_to_audio(text

